#! /usr/bin/env bash

set -e
set -x


# Let the DB start
PYTHONPATH="..:." python app/backend_pre_start.py


PYTHONPATH="..:." python app/initial_data.py