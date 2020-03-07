#!bin/sh
PATHONPATH=./app/ coverage run --source=./app/ -m pytest
coverage report -m