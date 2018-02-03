# Puyo Puyo Tetris

An implementation of Puyo Puyo Tetris for the web.

# Setup

*Using Python 2.7*

1. `pip install virtualenv`
2. `virtualenv env` This creates a local python environment for the project, all dependencies are added within this environment.
3. `source env/bin/activate` The environment should always be on while developing in the repo.
	* `deactivate` to stop
4. `pip install -r requirements.txt`
5. `python run.py debug`
6. Open http://127.0.0.1:5000/

If adding dependencies to the environment, use `pip freeze > requirements.txt` to update the pip installer for the future.

Server restarts automatically upon changes using debug mode.