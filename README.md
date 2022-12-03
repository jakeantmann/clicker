# Clicker

This is a mock standalone cli for a nonexistent data analysis project. I created this to learn about [click](https://click.palletsprojects.com). I also wanted to make the tool available as a standalone cli tool, meaning instead of having to call `python -m clicker`, you can just call `clicker`

## Installation

To try this out, clone the repo. It's best to test things like this in a venv:

- Enter the repo folder
- Create the venv by running `python -m venv .`
- Activate the venv (see the table [here](https://docs.python.org/3/library/venv.html#how-venvs-work) to find out how to activate the venv for your OS)

Now, to get this working within a venv, you'll need pipx. This isn't hard to set up:

- Install with `pip install pipx`
- Add the local python installation to the local path with `pipx ensurepath`
- Install the package with `pipx install .`
- If you want it to be editable, instead use `pipx install .`. Think of this as a development mode.

If you want to run this outside of a venv because you have no fear, you can clone the repo/enter the repo folder as usual, and then just run `pip install .`. As per before, editable mode is `pip install -e.`

If editable mode isn't working for you, try upgrading pip and setuptools with `pip install --upgrade pip` and `pip install --upgrade setuptools`. This project doesn't use a `setup.py`, which works with setuptools>=64 and pip >= 21.3

## Usage

- To use the tool, you just need to run `clicker <command> <args>`
- If you want to see the available commands, run `clicker` or `clicker --help`
- Say you decide to run `clicker analysis`, but you want to look at the available arguments. You can run `clicker analysis --help` to find these.

That's all, folks!
