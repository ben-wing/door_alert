#!/bin/bash

script_loc=/home/pi/python_door_alert
log_path=/home/pi/log
#used simply to wrap and document errors
errlog=$log_path/sunset_err.log
/usr/bin/python3 $script_loc/GetSunset.py > $log_path/sunset.today 2> $errlog

if [[ $(stat --format=%s $errlog) -ne 0 ]]; then
  mv $errlog ${errlog}-$($script_loc/filedatetime)
else
  cat $log_path/sunset.today >> $log_path/sunset.log 
fi
