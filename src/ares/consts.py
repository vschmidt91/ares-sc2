"""Keep constants here for ease of use."""
from enum import Enum, auto
from typing import List, Set

from sc2.data import Race
from sc2.ids.effect_id import EffectId
from sc2.ids.unit_typeid import UnitTypeId as UnitID

"""Strings"""
# general/config
ACTIVE_GRID: str = "ActiveGrid"
AIR: str = "Air"
AIR_AVOIDANCE: str = "AirAvoidance"
AIR_COST: str = "AirCost"
AIR_RANGE: str = "AirRange"
AIR_VS_GROUND: str = "AirVsGround"
ATTACK_DISENGAGE_FURTHER_THAN: str = "AttackDisengageIfTargetFurtherThan"
ATTACK_ENGAGE_CLOSER_THAN: str = "AttackEngageIfTargetCloserThan"
BLINDING_CLOUD: str = "BlindingCloud"
BOOST_BACK_TO_TOWNHALL: str = "BoostBackToTownHall"
BUILD_CHOICES: str = "BuildChoices"
BUILDS: str = "Builds"
CHAT_DEBUG: str = "ChatDebug"
COMBAT: str = "Combat"
CONFIG_FILE: str = "config.yml"
CORROSIVE_BILE: str = "CorrosiveBile"
COST: str = "Cost"
COST_MULTIPLIER: str = "CostMultiplier"
CYCLE: str = "Cycle"
DANGER_THRESHOLD: str = "DangerThreshold"
DANGER_TILES: str = "DangerTiles"
DEBUG: str = "Debug"
DEBUG_GAME_STEP: str = "DebugGameStep"
DEBUG_OPTIONS: str = "DebugOptions"
DEBUG_SPAWN: str = "DebugSpawn"
EFFECTS: str = "Effects"
EFFECTS_RANGE_BUFFER: str = "EffectsRangeBuffer"
GAME_STEP: str = "GameStep"
GROUND: str = "Ground"
GROUND_AVOIDANCE: str = "GroundAvoidance"
GROUND_COST: str = "GroundCost"
GROUND_RANGE: str = "GroundRange"
LIBERATOR_ZONE: str = "LiberatorZone"
LURKER_SPINE: str = "LurkerSpine"
MINERAL_BOOST: str = "MineralBoost"
MINERAL_DISTANCE_FACTOR: str = "MineralDistanceFactor"
MINERAL_STACKING: str = "MineralStacking"
MINING: str = "Mining"
NUKE: str = "Nuke"
OPENING_BUILD_ORDER: str = "OpeningBuildOrder"
ORACLE: str = "Oracle"
PARASITIC_BOMB: str = "ParasiticBomb"
PATHING: str = "Pathing"
PATHING_GRID: str = "PathingGrid"
PLACEMENT: str = "Placement"
RANGE: str = "Range"
RANGE_BUFFER: str = "RangeBuffer"
RESOURCE_DEBUG: str = "ResourceDebug"
SHADE_COMMENCED: str = "SHADE_COMMENCED"
SHADE_OWNER: str = "SHADE_OWNER"
SHOW_BUILDING_FORMATION: str = "ShowBuildingFormation"
SHOW_PATHING_COST: str = "ShowPathingCost"
STORM: str = "Storm"
STRATEGY_MANAGER: str = "StrategyManager"
TOWNHALL_DISTANCE_FACTOR: str = "TownhallDistanceFactor"
UNIT_CONTROL: str = "UnitControl"
UNIT_SQUADS: str = "UnitSquads"
UNITS: str = "Units"
USE_DATA: str = "UseData"
WORKER_ON_ROUTE_TIMEOUT: str = "WorkerOnRouteTimeout"

# building manager
BUILDING: str = "Building"
BUILDING_PURPOSE: str = "building_purpose"
CANCEL_ORDER: str = "CancelOrder"
ID: str = "id"
STRUCTURE_ORDER_COMPLETE: str = "structure_order_complete"
TARGET: str = "target"
TIME_ORDER_COMMENCED: str = "time_order_commenced"

# build runner / resource_manager
GAS: str = "gas"
MINERAL: str = "mineral"
NAT: str = "NAT"
PROXY: str = "PROXY"
THIRD: str = "THIRD"

# data manager
DATA_DIR: str = "./data"
DURATION: str = "Duration"
LOSS: str = "Loss"
RACE: str = "EnemyRace"
RESULT: str = "Result"
STRATEGY_USED: str = "StrategyUsed"
TEST_OPPONENT_ID: str = "test_123"
TIE: str = "Tie"
WIN: str = "Win"

# main
ADD_SHADES_ON_FRAME: int = (
    120  #: The frame at which point Adept Shades are treated as units
)
BANNED_PHRASES: List[str] = [
    "COCOON",
    "EGG",
    "CHANGELING",
    "FLYING",
    "PHASE",
]  #: UnitTypeIds with these words in them have Cost issues
SHADE_DURATION: int = 160  #: how long a Shade lasts in frames


# pathing manager
AIR_VS_GROUND_DEFAULT: int = 10

# terrain manager
CURIOUS: str = "CURIOUS"
GLITTERING: str = "GLITTERING"
OXIDE: str = "OXIDE"
LIGHTSHADE: str = "LIGHTSHADE"

# unit memory manager
MAX_SNAPSHOTS_PER_UNIT: int = 10

# chat debug
COOLDOWN: Set[str] = {"COOLDOWN"}
CREATE: Set[str] = {"CREATE", "MAKE"}
FOOD: Set[str] = {"FOOD", "SUPPLY"}
GOD: Set[str] = {"GOD"}
KILL: Set[str] = {"DESTROY", "KILL"}
RESOURCES: Set[str] = {"RESOURCES", "MONEY"}
SHOW_MAP: Set[str] = {"REVEAL", "SHOW", "SHOW-MAP"}
TECH_TREE: Set[str] = {"TECH", "TECH-TREE"}
UPGRADES: Set[str] = {"UPGRADES"}

"""Enums"""


class BuildingSize(str, Enum):
    FIVE_BY_FIVE = "FIVE_BY_FIVE"
    THREE_BY_THREE = "THREE_BY_THREE"
    TWO_BY_TWO = "TWO_BY_TWO"


class BuildOrderOptions(str, Enum):
    CHRONO = "CHRONO"
    GAS = "GAS"
    EXPAND = "EXPAND"
    ORBITAL = "ORBITAL"
    SUPPLY = "SUPPLY"
    WORKER = "WORKER"

    @classmethod
    def contains_key(cls, name):
        return name in cls.__members__


class BuildOrderTargetOptions(str, Enum):
    RAMP = "RAMP"

    @classmethod
    def contains_key(cls, name):
        return name in cls.__members__


class BuildingPurpose(Enum):
    """Populate this with reasons a building was built."""

    NORMAL_BUILDING = auto()


class EngagementResult(int, Enum):
    """Possible engagement results."""

    VICTORY_EMPHATIC = 10
    VICTORY_OVERWHELMING = 9
    VICTORY_DECISIVE = 8
    VICTORY_CLOSE = 7
    VICTORY_MARGINAL = 6
    TIE = 5
    LOSS_MARGINAL = 4
    LOSS_CLOSE = 3
    LOSS_DECISIVE = 2
    LOSS_OVERWHELMING = 1
    LOSS_EMPHATIC = 0


class ManagerRequestType(str, Enum):
    """Populate this with manager requests."""

    # AbilityTrackerManager
    GET_UNIT_TO_ABILITY_DICT = "GET_UNIT_TO_ABILITY_DICT"
    UPDATE_ABILITY_COOLDOWN = "UPDATE_ABILITY_COOLDOWN"
    UPDATE_UNIT_TO_ABILITY_DICT = "UPDATE_UNIT_TO_ABILITY_DICT"

    # BuildingManager
    BUILD_WITH_SPECIFIC_WORKER = "BUILD_WITH_SPECIFIC_WORKER"
    GET_BUILDING_COUNTER = "GET_BUILDING_COUNTER"
    GET_BUILDING_TRACKER_DICT = "GET_BUILDING_TRACKER_DICT"

    # CombatManager
    GET_ATTACK_SQUAD_ENGAGE_TARGET = "GET_ATTACK_SQUAD_ENGAGE_TARGET"
    GET_POSITION_OF_MAIN_ATTACKING_SQUAD = "GET_POSITION_OF_MAIN_ATTACKING_SQUAD"
    GET_PREDICTED_DEFENSIVE_FIGHT_RESULT = "GET_PREDICTED_DEFENSIVE_FIGHT_RESULT"
    GET_PREDICTED_MAIN_FIGHT_RESULT = "GET_PREDICTED_MAIN_FIGHT_RESULT"
    GET_SQUAD_CLOSE_TO_TARGET = "GET_SQUAD_CLOSE_TO_TARGET"
    REMOVE_TAG_FROM_SQUADS = "REMOVE_TAG_FROM_SQUADS"

    # DataManager
    GET_CHOSEN_OPENING = "GET_CHOSEN_OPENING"

    # PathManager
    FIND_LOW_PRIORITY_PATH = "FIND_LOW_PRIORITY_PATH"
    FIND_LOWEST_COST_POINTS = "FIND_LOWEST_COST_POINTS"
    FIND_RAW_PATH = "FIND_RAW_PATH"
    GET_AIR_AVOIDANCE_GRID = "GET_AIR_AVOIDANCE_GRID"
    GET_AIR_GRID = "GET_AIR_GRID"
    GET_AIR_VS_GROUND_GRID = "GET_AIR_VS_GROUND_GRID"
    GET_CACHED_GROUND_GRID = "GET_CACHED_GROUND_GRID"
    GET_CLOSEST_SAFE_SPOT = "GET_CLOSEST_SAFE_SPOT"
    GET_FORCEFIELD_POSITIONS = "GET_FORCEFIELD_POSITIONS"
    GET_GROUND_AVOIDANCE_GRID = "GET_GROUND_AVOIDANCE_GRID"
    GET_GROUND_GRID = "GET_GROUND_GRID"
    GET_MAP_DATA = "GET_MAP_DATA"
    GET_PRIORITY_GROUND_AVOIDANCE_GRID = "GET_PRIORITY_GROUND_AVOIDANCE_GRID"
    GET_WHOLE_MAP_ARRAY = "GET_WHOLE_MAP_ARRAY"
    GET_WHOLE_MAP_TREE = "GET_WHOLE_MAP_TREE"
    IS_POSITION_SAFE = "IS_POSITION_SAFE"
    NEIGHBOURING_TILES_ARE_INPATHABLE = "NEIGHBOURING_TILES_ARE_INPATHABLE"
    PATH_NEXT_POINT = "PATH_NEXT_POINT"

    # PlacementManager
    CAN_PLACE_STRUCTURE = "CAN_PLACE_STRUCTURE"
    REQUEST_BUILDING_PLACEMENT = "REQUEST_BUILDING_PLACEMENT"

    # ResourceManager
    GET_MINERAL_PATCH_TO_LIST_OF_WORKERS = "GET_MINERAL_PATCH_TO_LIST_OF_WORKERS"
    GET_MINERAL_TARGET_DICT = "GET_MINERAL_TARGET_DICT"
    GET_NUM_AVAILABLE_MIN_PATCHES = "GET_NUM_AVAILABLE_MIN_PATCHES"
    GET_WORKER_TAG_TO_TOWNHALL_TAG = "GET_WORKER_TAG_TO_TOWNHALL_TAG"
    GET_WORKER_TO_GAS_BUILDING_DICT = "GET_WORKER_TO_GAS_BUILDING_DICT"
    GET_WORKER_TO_MINERAL_PATCH_DICT = "GET_WORKER_TO_MINERAL_PATCH_DICT"
    REMOVE_GAS_BUILDING = "REMOVE_GAS_BUILDING"
    REMOVE_MINERAL_FIELD = "REMOVE_MINERAL_FIELD"
    REMOVE_WORKER_FROM_MINERAL = "REMOVE_WORKER_FROM_MINERAL"
    SELECT_WORKER = "SELECT_WORKER"
    SET_WORKERS_PER_GAS = "SET_WORKERS_PER_GAS"

    # StrategyManager
    CAN_WIN_FIGHT = "CAN_WIN_FIGHT"
    GET_ENEMY_AT_HOME = "GET_ENEMY_AT_HOME"
    GET_OFFENSIVE_ATTACK_TARGET = "GET_OFFENSIVE_ATTACK_TARGET"
    GET_RALLY_POINT = "GET_RALLY_POINT"
    GET_SHOULD_BE_OFFENSIVE = "GET_SHOULD_BE_OFFENSIVE"

    # TerrainManager
    BUILDING_POSITION_BLOCKED_BY_BURROWED_UNIT = (
        "BUILDING_POSITION_BLOCKED_BY_BURROWED_UNIT"
    )
    GET_BEHIND_MINERAL_POSITIONS = "GET_BEHIND_MINERAL_POSITIONS"
    GET_CLOSEST_OVERLORD_SPOT = "GET_CLOSEST_OVERLORD_SPOT"
    GET_DEFENSIVE_THIRD = "GET_DEFENSIVE_THIRD"
    GET_ENEMY_EXPANSIONS = "GET_ENEMY_EXPANSIONS"
    GET_ENEMY_FOURTH = "GET_ENEMY_FOURTH"
    GET_ENEMY_NAT = "GET_ENEMY_NAT"
    GET_ENEMY_RAMP = "GET_ENEMY_RAMP"
    GET_ENEMY_THIRD = "GET_ENEMY_THIRD"
    GET_FLOOD_FILL_AREA = "GET_FLOOD_FILL_AREA"
    GET_INITIAL_PATHING_GRID = "GET_INITIAL_PATHING_GRID"
    GET_IS_FREE_EXPANSION = "GET_IS_FREE_EXPANSION"
    GET_MAP_CHOKE_POINTS = "GET_MAP_CHOKE_POINTS"
    GET_OL_SPOT_NEAR_ENEMY_NATURAL = "GET_OL_SPOT_NEAR_ENEMY_NATURAL"
    GET_OL_SPOTS = "GET_OL_SPOTS"
    GET_OWN_EXPANSIONS = "GET_OWN_EXPANSIONS"
    GET_OWN_NAT = "GET_OWN_NAT"
    GET_POSITIONS_BLOCKED_BY_BURROWED_ENEMY = "GET_POSITIONS_BLOCKED_BY_BURROWED_ENEMY"

    # UnitCacheManager
    GET_CACHED_ENEMY_ARMY = "GET_CACHED_ENEMY_ARMY"
    GET_ENEMY_ARMY_CENTER_MASS = "GET_ENEMY_ARMY_CENTER_MASS"
    GET_CACHED_ENEMY_ARMY_DICT = "GET_CACHED_ENEMY_ARMY_DICT"
    GET_CACHED_ENEMY_WORKERS = "GET_CACHED_ENEMY_WORKERS"
    GET_OLD_OWN_ARMY_DICT = "GET_OLD_OWN_ARMY_DICT"
    GET_CACHED_OWN_ARMY = "GET_CACHED_OWN_ARMY"
    GET_CACHED_OWN_ARMY_DICT = "GET_CACHED_OWN_ARMY_DICT"
    GET_OWN_STRUCTURES_DICT = "GET_OWN_STRUCTURES_DICT"
    GET_UNITS_FROM_TAGS = "GET_UNITS_FROM_TAGS"
    GET_REMOVED_UNITS = "GET_REMOVED_UNITS"

    # UnitMemoryManager
    GET_ALL_ENEMY = "GET_ALL_ENEMY"
    GET_ENEMY_GROUND = "GET_ENEMY_GROUND"
    GET_ENEMY_FLIERS = "GET_ENEMY_FLIERS"
    GET_ENEMY_TREE = "GET_ENEMY_TREE"
    GET_OWN_TREE = "GET_OWN_TREE"
    GET_UNITS_IN_RANGE = "GET_UNITS_IN_RANGE"

    # UnitRoleManager
    ASSIGN_ROLE = "ASSIGN_ROLE"
    BATCH_ASSIGN_ROLE = "BATCH_ASSIGN_ROLE"
    CLEAR_ROLE = "CLEAR_ROLE"
    GET_ALL_FROM_ROLES_EXCEPT = "GET_ALL_FROM_ROLES_EXCEPT"
    GET_UNIT_ROLE_DICT = "GET_UNIT_ROLE_DICT"
    GET_UNITS_FROM_ROLE = "GET_UNITS_FROM_ROLE"
    GET_UNITS_FROM_ROLES = "GET_UNITS_FROM_ROLES"
    SWITCH_ROLES = "SWITCH_ROLES"


class ManagerName(str, Enum):
    """The names of the various managers."""

    BUILDING_MANAGER = "BuildingManager"
    COMBAT_MANAGER = "CombatManager"
    DATA_MANAGER = "DataManager"
    PATH_MANAGER = "PathManager"
    PLACEMENT_MANAGER = "PlacementManager"
    PRODUCTION_MANAGER = "ProductionManager"
    RESOURCE_MANAGER = "ResourceManager"
    STRATEGY_MANAGER = "StrategyManager"
    TERRAIN_MANAGER = "TerrainManager"
    UNIT_CACHE_MANAGER = "UnitCacheManager"
    UNIT_MEMORY_MANAGER = "UnitMemoryManager"
    UNIT_ROLE_MANAGER = "UnitRoleManager"


class UnitRole(str, Enum):
    """Roles for units"""

    ATTACKING = "ATTACKING"  # units in a combat zone that is not near one of our bases
    BASE_DEFENDER = "BASE_DEFENDER"  # units split off to defend expansions
    BUILDING = "BUILDING"  # workers that have been assigned to create a building
    DEFENDING = "DEFENDING"  # units in a combat zone near one of our bases
    GATHERING = "GATHERING"  # workers that are mining
    HARASSING = "HARASSING"  # units that are harassing
    IDLE = "IDLE"  # not doing anything
    PERSISTENT_BUILDER = "PERSISTENT_BUILDER"  # does not get reassigned automatically
    SCOUTING = "SCOUTING"


class UnitTreeQueryType(str, Enum):
    """Identifiers for which unit trees to query for UnitMemoryManager"""

    AllOwn = "AllOwn"
    AllEnemy = "AllEnemy"
    EnemyFlying = "EnemyFlying"
    EnemyGround = "EnemyGround"


"""Sets"""
ADD_ONS: dict[UnitID:UnitID] = {
    UnitID.BARRACKSREACTOR: UnitID.BARRACKS,
    UnitID.FACTORYTECHREACTOR: UnitID.FACTORY,
    UnitID.STARPORTREACTOR: UnitID.STARPORT,
    UnitID.BARRACKSTECHLAB: UnitID.BARRACKS,
    UnitID.FACTORYTECHLAB: UnitID.FACTORY,
    UnitID.STARPORTTECHLAB: UnitID.STARPORT,
}

ALL_STRUCTURES: Set[UnitID] = {
    UnitID.ARMORY,
    UnitID.ASSIMILATOR,
    UnitID.ASSIMILATORRICH,
    UnitID.AUTOTURRET,
    UnitID.BANELINGNEST,
    UnitID.BARRACKS,
    UnitID.BARRACKSFLYING,
    UnitID.BARRACKSREACTOR,
    UnitID.BARRACKSTECHLAB,
    UnitID.BUNKER,
    UnitID.BYPASSARMORDRONE,
    UnitID.COMMANDCENTER,
    UnitID.COMMANDCENTERFLYING,
    UnitID.CREEPTUMOR,
    UnitID.CREEPTUMORBURROWED,
    UnitID.CREEPTUMORQUEEN,
    UnitID.CYBERNETICSCORE,
    UnitID.DARKSHRINE,
    UnitID.ELSECARO_COLONIST_HUT,
    UnitID.ENGINEERINGBAY,
    UnitID.EVOLUTIONCHAMBER,
    UnitID.EXTRACTOR,
    UnitID.EXTRACTORRICH,
    UnitID.FACTORY,
    UnitID.FACTORYFLYING,
    UnitID.FACTORYREACTOR,
    UnitID.FACTORYTECHLAB,
    UnitID.FLEETBEACON,
    UnitID.FORGE,
    UnitID.FUSIONCORE,
    UnitID.GATEWAY,
    UnitID.GHOSTACADEMY,
    UnitID.GREATERSPIRE,
    UnitID.HATCHERY,
    UnitID.HIVE,
    UnitID.HYDRALISKDEN,
    UnitID.INFESTATIONPIT,
    UnitID.LAIR,
    UnitID.LURKERDENMP,
    UnitID.MISSILETURRET,
    UnitID.NEXUS,
    UnitID.NYDUSCANAL,
    UnitID.NYDUSCANALATTACKER,
    UnitID.NYDUSCANALCREEPER,
    UnitID.NYDUSNETWORK,
    UnitID.ORACLESTASISTRAP,
    UnitID.ORBITALCOMMAND,
    UnitID.ORBITALCOMMANDFLYING,
    UnitID.PHOTONCANNON,
    UnitID.PLANETARYFORTRESS,
    UnitID.POINTDEFENSEDRONE,
    UnitID.PYLON,
    UnitID.PYLONOVERCHARGED,
    UnitID.RAVENREPAIRDRONE,
    UnitID.REACTOR,
    UnitID.REFINERY,
    UnitID.REFINERYRICH,
    UnitID.RESOURCEBLOCKER,
    UnitID.ROACHWARREN,
    UnitID.ROBOTICSBAY,
    UnitID.ROBOTICSFACILITY,
    UnitID.SENSORTOWER,
    UnitID.SHIELDBATTERY,
    UnitID.SPAWNINGPOOL,
    UnitID.SPINECRAWLER,
    UnitID.SPINECRAWLERUPROOTED,
    UnitID.SPIRE,
    UnitID.SPORECRAWLER,
    UnitID.SPORECRAWLERUPROOTED,
    UnitID.STARGATE,
    UnitID.STARPORT,
    UnitID.STARPORTFLYING,
    UnitID.STARPORTREACTOR,
    UnitID.STARPORTTECHLAB,
    UnitID.SUPPLYDEPOT,
    UnitID.SUPPLYDEPOTLOWERED,
    UnitID.TECHLAB,
    UnitID.TEMPLARARCHIVE,
    UnitID.TWILIGHTCOUNCIL,
    UnitID.ULTRALISKCAVERN,
    UnitID.WARPGATE,
}

BURROWED_ALIAS: Set[UnitID] = {
    UnitID.BANELINGBURROWED,
    UnitID.CREEPTUMORBURROWED,
    UnitID.DRONEBURROWED,
    UnitID.HYDRALISKBURROWED,
    UnitID.INFESTORBURROWED,
    UnitID.INFESTORTERRANBURROWED,
    UnitID.LURKERMPBURROWED,
    UnitID.QUEENBURROWED,
    UnitID.RAVAGERBURROWED,
    UnitID.ROACHBURROWED,
    UnitID.SWARMHOSTBURROWEDMP,
    UnitID.ULTRALISKBURROWED,
    UnitID.WIDOWMINEBURROWED,
    UnitID.ZERGLINGBURROWED,
}

CHANGELING_TYPES: Set[UnitID] = {
    UnitID.CHANGELING,
    UnitID.CHANGELINGZERGLING,
    UnitID.CHANGELINGZERGLINGWINGS,
    UnitID.CHANGELINGMARINE,
    UnitID.CHANGELINGMARINESHIELD,
    UnitID.CHANGELINGZEALOT,
}

CREEP_TUMOR_TYPES: Set[UnitID] = {
    UnitID.CREEPTUMOR,
    UnitID.CREEPTUMORQUEEN,
    UnitID.CREEPTUMORBURROWED,
}

DETECTORS: Set[UnitID] = {
    UnitID.OBSERVER,
    UnitID.OBSERVERSIEGEMODE,
    UnitID.PHOTONCANNON,
    UnitID.RAVEN,
    UnitID.MISSILETURRET,
    EffectId.SCANNERSWEEP,
    UnitID.OVERSEER,
    UnitID.OVERSEERSIEGEMODE,
    UnitID.SPORECRAWLER,
}

EGG_BUTTON_NAMES: Set[str] = {"Drone", "Overlord"}

# we ignore these when detecting if an expansion location is blocked
FLYING_IGNORE: Set[UnitID] = {
    UnitID.OBSERVER,
    UnitID.OVERLORD,
    UnitID.OVERSEER,
    UnitID.BARRACKSFLYING,
    UnitID.COMMANDCENTERFLYING,
    UnitID.ORBITALCOMMANDFLYING,
    UnitID.FACTORYFLYING,
    UnitID.STARPORTFLYING,
    UnitID.PHOENIX,
}

GAS_BUILDINGS = {UnitID.ASSIMILATOR, UnitID.EXTRACTOR, UnitID.REFINERY}

# These are not really rocks, but end up in the destructible collection
IGNORE_DESTRUCTABLES: Set[UnitID] = {
    UnitID.INHIBITORZONESMALL,
    UnitID.INHIBITORZONEFLYINGLARGE,
    UnitID.INHIBITORZONEFLYINGMEDIUM,
    UnitID.INHIBITORZONEFLYINGLARGE,
    UnitID.INHIBITORZONELARGE,
    UnitID.INHIBITORZONEMEDIUM,
    UnitID.ACCELERATIONZONEFLYINGLARGE,
    UnitID.ACCELERATIONZONEFLYINGMEDIUM,
    UnitID.ACCELERATIONZONEFLYINGSMALL,
    UnitID.ACCELERATIONZONELARGE,
    UnitID.ACCELERATIONZONEMEDIUM,
    UnitID.ACCELERATIONZONESMALL,
    UnitID.CLEANINGBOT,
}

IGNORE_IN_COST_DICT: Set[UnitID] = {
    UnitID.BROODLING,
    UnitID.INTERCEPTOR,
    UnitID.LARVA,
    UnitID.LOCUSTMP,
    UnitID.LOCUSTMPFLYING,
    UnitID.MULE,
    UnitID.POINTDEFENSEDRONE,
    UnitID.INFESTEDTERRANSEGG,
    UnitID.INFESTEDTERRAN,
    UnitID.INFESTORBURROWED,
    UnitID.REFINERYRICH,
    UnitID.ASSIMILATORRICH,
    UnitID.EXTRACTORRICH,
}

IGNORED_UNIT_TYPES_MEMORY_MANAGER: Set[UnitID] = set()

# roles where most of our force is likely to be
MAIN_COMBAT_ROLES: Set[UnitRole] = {
    UnitRole.ATTACKING,
    UnitRole.DEFENDING,
}

TOWNHALL_TYPES: Set[UnitID] = {
    UnitID.HATCHERY,
    UnitID.LAIR,
    UnitID.HIVE,
    UnitID.COMMANDCENTER,
    UnitID.COMMANDCENTERFLYING,
    UnitID.ORBITALCOMMAND,
    UnitID.ORBITALCOMMANDFLYING,
    UnitID.PLANETARYFORTRESS,
    UnitID.NEXUS,
}

UNITS_TO_AVOID_TYPES: Set[UnitID] = {
    UnitID.CREEPTUMOR,
    UnitID.CREEPTUMORBURROWED,
    UnitID.CREEPTUMORQUEEN,
    UnitID.LURKERMPBURROWED,
    UnitID.INFESTORBURROWED,
    UnitID.ROACHBURROWED,
    UnitID.SPORECRAWLER,
}

UNITS_TO_IGNORE: Set[UnitID] = set()
UNIT_TYPES_WITH_NO_ROLE: Set[UnitID] = set()
WORKER_TYPES: Set[UnitID] = {UnitID.DRONE, UnitID.PROBE, UnitID.SCV}

race_supply: dict[Race, UnitID] = {
    Race.Protoss: UnitID.PYLON,
    Race.Terran: UnitID.SUPPLYDEPOT,
    Race.Zerg: UnitID.OVERLORD,
}
