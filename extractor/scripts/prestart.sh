#! /usr/bin/env bash

set -e
set -x


PROJECT_ROOT=$(cd "$(dirname "$0")/.." && pwd)


# Let the DB start
PYTHONPATH="$PROJECT_ROOT" python app/backend_pre_start.py


PYTHONPATH="$PROJECT_ROOT" python app/initial_data.py