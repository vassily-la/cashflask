#!/bin/sh

export FLASK_APP=/home/vl/Learn/restfl/cashman-flask-project/index.py

source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0
