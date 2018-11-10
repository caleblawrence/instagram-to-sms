#!/bin/bash

if pgrep -x "flask" > /dev/null
then
   echo "Flaks server is running"
else
   echo "Flask server was not running. Starting it now."
   export FLASK_APP=/home/pi/projects/instagramToSms/flaskImageServer.py
   nohup python -m flask run &
fi
   
ngrok http 5000
