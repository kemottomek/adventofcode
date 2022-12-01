# adventofcode
adventofcode 2022 edition

## Tools you need before you start

* [Pyenv](https://github.com/pyenv/pyenv)
* [Poetry](https://python-poetry.org/docs)
* [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

## First time set up

To set up the project you need to do the following:

1.As Python 3.10 is required for the project, execute `pyenv install 3.10.5` to install it.
2.Execute `pyenv local 3.10.5` to make Pyenv automatically switch to the above Python when we are in this project's
   directory.
3.Execute `poetry install` - it will create a virtualenv and install packages in it. Poetry will pick up the Python
   version you've set above automatically.
4.Execute `poetry shell` - it will activate the above virtualenv in your current terminal session. **When you close the
   terminal and open it again you will need to execute this command again in order to enter the virtualenv.**

## Using Poetry, Pyenv and Pre-commit

Here is a list of the most useful commands for those tools:

**Poetry**

* `poetry install` - Creates a virtualenv (if it doesn't yet exist) and installs packages from `poetry.lock` in it.
* `poetry lock` - Regenerates `poetry.lock` file based on the requirements specified in `pyproject.toml`.
* `poetry shell` - Sources into virtualenv created by Poetry. It's equivalent of
  the `source <path to your venv>/bin/activate`.

**Pyenv**

* `pyenv install <python version>` - Installs the particular Python version in your system.
* `pyenv global <python version>` - Makes the specified Python version the default in your system. This means that if
  you type `python` in the console, you will get the chosen Python version.
* `pyenv local <python version>` - Makes Pyenv always automatically switch to the specified Python version when you are
  inside this directory (or its children). It achieves it by creating `.python-version` file in the current directory.
  The Python version set by this command takes priority before Python from `pyenv global`.
* `pyenv shell <python version>` - Makes Pyenv use the specified Python version in the current shell. The Python version
  set by this command takes priority before Python from `pyenv local`. You don't need to use this command if you have a
  virtualenv created using Poetry - use `poetry shell` instead. Nevertheless, it can come in handy when doing stuff
  outside the project.