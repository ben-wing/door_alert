import RPi.GPIO as GPIO
import time
import subprocess
#load my own file as properties
import properties

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

formatted_ts=time.strftime('%Y-%m-%dT%H:%M:%S')

input_state = GPIO.input(18)

GPIO.cleanup()

############################################# 
### now that i have current state, send an alert
############################################# 

def get_last_line(file_handle): 
  # cycle to the last line of the file because it used to use the .log file rather than a single line file just for .today
  #why pass?? -> https://stackoverflow.com/a/3346492
  for line in file_handle:
    pass
  last=line.rstrip()
  f.close()
  return last
####

sunset_file='/home/pi/log/sunset.today'
f = open(sunset_file, "r")
sunset_str = get_last_line(f)
#print (sunset_str)
sunset_ts = time.strptime(sunset_str, '%Y-%m-%dT%H:%M:%S%z')

door_file='/home/pi/log/door.log'
#increase scope of door_state, to include it in logging
door_state='closed'
#debug always later than sunset true
#if ( True ):
if ( time.gmtime() >= sunset_ts):
  #print ("gmtime \n={}=\n is after or equal to sunset_ts \n={}=".format(time.gmtime(), sunset_ts))
  f=open(door_file, "r")
  last_door_state = get_last_line(f)
  #print ("last door ={}\n".format(last_door_state))
  (junk, door_state) = last_door_state.split("door ")
  # if else handling based on https://stackoverflow.com/a/12887408/1074093
  (door_state, junk) = door_state.split(",") if \
                       "," in door_state else \
                       (door_state, "")
  
  #print ("door state ={}=".format(door_state))
  #print ("input_state={}=".format(input_state))
  if ( input_state and door_state == 'open'):
    #print ("send a serious alert")
    command='echo \'close it!!\'|mail -s \'door open\' {} >> logs/door_mail.log'
    #print("command is ={}=".format(command.format(properties.address)))
    #TODO: try out using mailgun
    ret = subprocess.call(['ssh', 'meta.sdf.org', command.format(properties.address)])

if input_state == False:
  print( '{}--door closed'.format(formatted_ts))
else: 
  if door_state == 'open':
    print( '{}--door open,alerted'.format(formatted_ts))
  else: 
    print( '{}--door open'.format(formatted_ts))

