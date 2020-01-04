# door_alert
python code to send texts from a Pi ZeroW when my garage door is open after sunset

i attached a reed switch to my Pi Zero W which returns "False" when the door is closed, and "True" when the door is open.

i have 2 crontab entries to run this code
```
# m h  dom mon dow   command
13 8  *   *   *     /usr/bin/python3 /home/pi/python_door_alert/GetSunset.py >> /home/pi/log/sunset.log
*/5 *  *   *   *     /usr/bin/python3 /home/pi/python_door_alert/Alert.py >> /home/pi/log/door.log
```
**( ``/home/pi/log`` directory must be created manually)**

``GetSunset.py`` uses a web service provided by [sunrise-sunset.org](http://bit.ly/2wr8hWl) and is is run once per day to determine when sunset occurs

``Alert.py`` runs every 5 minutes and logs whether the door is open or closed. if it is after sunset an alert is sent to the address configured in ``properties.py`` telling me to close the door.
requires RPi.GPIO package (apt install python3-rpi.gpio)

**( [MetaARPA account at SDF](http://bit.ly/2whFtiN) with manually configured passphraseless SSH trust necessary for sending email with the same method i use)
