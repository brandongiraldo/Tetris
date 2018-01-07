# Puyo Puyo Tetris

An implementation of Puyo Puyo Tetris for the web.

# Setup

*Using Python 2.7*

1. `pip install virtualenv`
2. `virtualenv env`
3. `source env/bin/activate`
	* `deactivate` to stop
4. `pip install -r requirements.txt`
5. `python run.py debug`
6. Open http://127.0.0.1:5000/

If adding depdencies to the enviornment, use `pip freeze > requirements.txt` to update those globally.

Server restarts automatically upon changes using debug mode.