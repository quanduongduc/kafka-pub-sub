#!/usr/bin/env bash

set -e
current_dir=$(pwd)

PYTHONPATH=$current_dir/src

python $current_dir/src/mailer/main.py