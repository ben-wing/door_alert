#!/bin/bash

cd /home/pi/log

yesterday=$( date -d "yesterday 13:00" '+%Y%m' )
echo  $yesterday

for file in door.log sunset.log
do
  mv $file $file-$yesterday
  gzip $file-$yesterday
done
