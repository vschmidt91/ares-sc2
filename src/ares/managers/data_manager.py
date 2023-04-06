"""Handle data."""
import json
import os
from os import path
from typing import Dict, List, Optional, Union

from sc2.data import Result

from ares.consts import (
    BUILD_CHOICES,
    CYCLE,
    DATA_DIR,
    DEBUG,
    DURATION,
    LOSS,
    RACE,
    RESULT,
    STRATEGY_USED,
    TEST_OPPONENT_ID,
    USE_DATA,
    WIN,
    ManagerName,
    ManagerRequestType,
)
from ares.managers.manager import Manager
from ares.managers.manager_mediator import IManagerMediator, ManagerMediator


class DataManager(Manager, IManagerMediator):
    """
    Handles opponent data, and chooses a strategy, based on the
    build cycle in config.yml
    """

    def __init__(self, ai, config: Dict, mediator: ManagerMediator) -> None:
        super().__init__(ai, config, mediator)
        self.manager_requests_dict = {
            ManagerRequestType.GET_CHOSEN_OPENING: lambda kwargs: self.chosen_opening
        }
        self.chosen_opening: str = ""
        self.build_cycle: list = self._get_build_cycle()
        self.found_build: bool = False
        self.opponent_history: List = []

        self.file_path: path = path.join(
            DATA_DIR, f"{self.ai.opponent_id}-{self.ai.race.name.lower()}.json"
        )

        self.data_saved: bool = False

    def manager_request(
        self,
        receiver: ManagerName,
        request: ManagerRequestType,
        reason: str = None,
        **kwargs,
    ) -> Optional[Union[str, list[str]]]:
        """Fetch information from this Manager so another Manager can use it.

        Parameters
        ----------
        receiver :
            This Manager.
        request :
            What kind of request is being made
        reason :
            Why the reason is being made
        kwargs :
            Additional keyword args if needed for the specific request, as determined
            by the function signature (if appropriate)

        Returns
        -------
        Optional[Union[BotMode, List[BotMode]]] :
            Either one of the ability dictionaries is being returned or a function that
            returns None was called from a different manager (please don't do that).

        """
        return self.manager_requests_dict[request](kwargs)

    async def initialise(self) -> None:
        if BUILD_CHOICES in self.config:
            if self.config[USE_DATA]:
                self._get_opponent_data(self.ai.opponent_id)
                self._choose_opening()

            else:
                self.chosen_opening = self.build_cycle[0]

    async def update(self, _iteration: int) -> None:
        """Not used by this manager.

        Manager is an abstract class and must have an ``update`` method.

        Parameters
        ----------
        _iteration :
            The current game iteration

        Returns
        -------

        """
        pass

    def _choose_opening(self) -> None:
        """
        Look at the last build used, and choose a strategy depending on result
        TODO: Develop a more sophisticated system rather then cycling on defeat
        @return:
        """
        last_build: str = self.opponent_history[-1][STRATEGY_USED]
        last_result: int = self.opponent_history[-1][RESULT]

        for i, build in enumerate(self.build_cycle):
            if last_build == build:
                self.found_build = True
                # Defeat
                if last_result == 0:
                    index: int = 0 if len(self.build_cycle) <= i + 1 else i + 1
                    self.chosen_opening = self.build_cycle[index]
                else:
                    self.chosen_opening = build
                break
        # incase build from last game wasn't found in build cycle
        if not self.found_build:
            self.chosen_opening = self.build_cycle[0]

    def _get_build_cycle(self) -> List[str]:
        """
        Get the build cycle for the opponent from the config file
        If the opponent id is not present, set a default build cycle instead
        @return:
        """
        if self.config[DEBUG]:
            opponent_id: str = TEST_OPPONENT_ID
        else:
            opponent_id: str = self.ai.opponent_id

        build_cycle: List[str] = []
        if BUILD_CHOICES in self.config:
            # get a build cycle from config depending on ai arena opponent id
            if opponent_id in self.config[BUILD_CHOICES]:
                for build in self.config[BUILD_CHOICES][opponent_id][CYCLE]:
                    build_cycle.append(build)
            # else choose a cycle depending on the enemy race
            elif self.ai.enemy_race.name in self.config[BUILD_CHOICES]:
                for build in self.config[BUILD_CHOICES][self.ai.enemy_race.name][CYCLE]:
                    build_cycle.append(build)

        return build_cycle

    def _get_opponent_data(self, _opponent_id: str) -> None:
        """
        Get saved data on opponent, if none is present setup new data
        @param _opponent_id:
        @return:
        """
        if path.isfile(self.file_path):
            with open(self.file_path, "r") as f:
                self.opponent_history = json.load(f)
        else:
            # no data, create a dummy version
            self.opponent_history = [
                {
                    RACE: str(self.ai.enemy_race),
                    DURATION: 0,
                    STRATEGY_USED: self.build_cycle[0],
                    RESULT: 2,
                }
            ]

    def store_opponent_data(self, result: Union[Result, str]) -> None:
        """
        Called at end of game, save build used and result.
        @param result:
        @return:
        """
        # only write results once
        if self.data_saved:
            return
        if type(result) != str:
            result_id: int = 1
            if result == Result.Victory:
                result_id = 2
            elif result == Result.Defeat:
                result_id = 0
        else:
            if result == WIN:
                result_id = 2
            elif result == LOSS:
                result_id = 0
            else:
                # treat it as a tie if we don't know what happened
                result_id = 1

        self.add_game_to_dict(self.chosen_opening, int(self.ai.time), result_id)
        os.makedirs("data", exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump(self.opponent_history, f)
        self.data_saved = True

    def add_game_to_dict(self, bot_mode: str, game_duration: int, result: int) -> None:
        """
        Append a new game to the dict's list
        @param bot_mode:
        @param game_duration:
        @param result:
        @return:
        """
        game = {
            RACE: str(self.ai.enemy_race),
            DURATION: game_duration,
            STRATEGY_USED: bot_mode,
            RESULT: result,
        }
        self.opponent_history.append(game)
