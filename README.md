[![Linting](https://github.com/AresSC2/ares-sc2/actions/workflows/lint.yml/badge.svg)](https://github.com/AresSC2/ares-sc2/actions/workflows/lint.yml)
[![Testing](https://github.com/AresSC2/ares-sc2/actions/workflows/test.yml/badge.svg)](https://github.com/AresSC2/ares-sc2/actions/workflows/test.yml)

# ares-sc2

## Dev notes (all to go in docs when ready):

### Random bits explaining some decisions
 - Application layout - [Python Packaging Authority](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
recommend the `src` layout
 - Standard to store version number in the package's `__init__.py` [PEP8](https://peps.python.org/pep-0008/)
 - Also store the version in `pyproject.toml`
 - `Makefile` contains most of the commonly used commands from this write up. This file is used by github workflow


### Setting up dev environment
TODO


### Poetry
Takes care of env, dependency, building and publishing
#### Useful commands
See [Basic usage](https://python-poetry.org/docs/basic-usage/)


Init new project, generates `pyproject.toml` that contains the entire package configuration. Fine to edit this

```poetry init --name ares-sc2 --no-interaction```

Run in virtual env (poetry uses venv) [Managing poetry environments](https://python-poetry.org/docs/managing-environments/):

```poetry run python src/ares/main.py```

Run tests

```poetry run pytest```

Create and activate an environment (can also use PyCharm to create new env):

```poetry env use python```

On Linux possibly:
```poetry env use python3.10```

Find environment in file system:

```poetry env list --full-path```

Use this path to add existing env in PyCharm

Can get a shell into the environment:

```poetry shell```

Install dependencies:

```poetry add burnysc2```

Create a `lock` file. Should be added to git. Ensures all people working on project using the same library versions.
Automatically generated and shouldn't be edited

```poetry lock```

Install all dependencies based on the lock file

This command will read the TOML file, resolve all the dependencies and finally install them in a virtual environment 
that poetry will create by default under {cache-dir}/virtualenvs/. 

```poetry install```

Install without dev tools

```poetry install --without lint```

List all installed dependencies:

```poetry show```

List current and latest available version

```poetry show -l```

Same as above, but only show outdated

```poetry show -o```

Update dependencies:

```poetry update```

Poetry can organise dependencies by groups, since dev tools etc are not required in the package release, eg:

```poetry add --group lint isort black flake8 mypy```


#### Notes about `pyproject.toml`
 - what backend to build the package: build-system (Instead of setup.py/setup.cfg or others, the backend to build the package is poetry)
 - some metadata for the project: tool.poetry (the initial version of the package*, description etc.)
 - the dependencies for the app: tool.poetry.dependencies
 - gotcha - The name in `pyproject.toml` should be the same as the package

### Linting and autoformatting
black for main autoformatting
isort for import formatting
flake8 for checking code base against coding style (PEP8)
mypy for checking type annotations 

isort and black don't agree on some things, add following to `pyproject.toml`
```
[tool.isort]
profile = "black"
```

flake8 also needs to use black settings, we do this with a `.flake8` settings file

For mypy we configure via `pyproject.toml`, see [docs](https://mypy.readthedocs.io/en/stable/config_file.html#using-a-pyproject-toml)
See more [here](https://mypy.readthedocs.io/en/stable/running_mypy.html)

#### Using these tools on command line

Can pass in `--check` for some of these

`isort .`
`black.`
`flake8 .`
`mypy .`

We put all these into a `makefile`, which allows us to do:
`make format`
`make lint`

However, using makefiles on Windows requires a bit more setup

#### Configure PyCharm to run these automatically
black, isort and flake8 [See guide here](https://johschmidt42.medium.com/automate-linting-formatting-in-pycharm-with-your-favourite-tools-de03e856ee17)

mypy - PyCharm will help with type annotations, just ensure they are being used, and run `mypy .` before committing
to ensure the github lint workflow tests pass
Could look for some extra tools here if needed later

#### Github workflow
All formatters and linters are run in a github workflow, we use the `makefile` here.

#### Precommit hooks

Possible but investigate later

### Unit tests
Read [this](https://realpython.com/pytest-python-testing/), no point repeating it here
`poetry add --group test pytest`

Each test should be small and self-contained

#### Coverage
Indicates how much code is covered by tests

Run coverage through `pytest`:
`pytest --cov=src --cov-report term-missing --cov-report=html`

[Offical docs](https://coverage.readthedocs.io/en/6.5.0/config.html)


#### Automatic documentation
Using [mkdocs](https://www.mkdocs.org/) for no particular reason other than found a good tutorial using it

`poetry add --group docs mkdocs mkdocs-material`

Sphinx is another alternative

To build docs locally:
`mkdocs build`

Push to github pages: (can't test till public repo)
`mkdocs gh-deploy -m "docs: update documentation" -v --force`

#### Docstrings

Using numpy style

`poetry add --group docs "mkdocstrings[python]"`

Pytest will run tests on any Examples in docstrings
`pytest --doctest-modules`

