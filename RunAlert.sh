#!/bin/bash

#used simply to wrap and document errors
errlog=/home/pi/log/door_err.log
/usr/bin/python3 /home/pi/python_door_alert/Alert.py >> /home/pi/log/door.log 2>$errlog

if [[ $(stat --format=%s $errlog) -ne 0 ]]; then
  mv $errlog ${errlog}-$(/home/pi/python_door_alert/filedatetime)
fi
