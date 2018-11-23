#!/bin/sh
echo ''
echo '#### #### installing requirements #### ####'
pip install -r requirements.txt
echo '#### #### end installing requirements #### ####'
echo ''

echo ''
echo '#### #### importing PYTHONPATH environment variables #### ####'
#echo $PWD/src
export PYTHONPATH=$PYTHONPATH:$PWD/src
echo '#### #### done with importing PYTHONPATH environment variables #### ####'
echo ''

echo ''
echo '#### #### starting server daemon pid is in '$PWD'/log/app.pid file #### ####'
# FLASK_APP=src/app.py flask run
# Running on http://localhost:5000/
gunicorn --config rsc/gunicorn.conf app:app