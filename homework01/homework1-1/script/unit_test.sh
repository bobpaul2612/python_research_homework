#!bin/sh
PYTHONPATH=./app/ coverage run --source=./app -m pytest
coverage report -m