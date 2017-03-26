#!/bin/sh

SCRIPT_DIR=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
export FLASK_APP=${SCRIPT_DIR}/application/app.py
echo $FLASK_APP
flask run --host=0.0.0.0 
