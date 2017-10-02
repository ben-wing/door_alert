#!/bin/bash
#used simply to wrap and document errors

script_loc=/home/pi/python_door_alert
log_path=/home/pi/log
errlog=$log_path/door_err.log

/usr/bin/python3 $script_loc/Alert.py >> $log_path/door.log 2> $errlog

if [[ $(stat --format=%s $errlog) -ne 0 ]]; then
  mv $errlog ${errlog}-$($script_loc/filedatetime)
fi
