#decoder extraction
import base64
import datetime
ei = 'tci4UszSJeLN7Ab9xYD4CQ'
ei = '2L9xWP3cA8vYmwHRir6ICw'
print "Input ei term = " + ei

num_extra_bytes = (len(ei) % 4) # equals number of extra bytes past last multiple of 4 eg equals 1 for ei length of 21
print num_extra_bytes
if (num_extra_bytes != 0):
    padlength = 4 - num_extra_bytes # eg 4 - 1 results in 3 extra "=" pad bytes being added 
    padstring = ei + padlength*'='
else:
    padstring = ei
    
decoded = base64.urlsafe_b64decode(padstring)
print padstring
print decoded
print decoded

import struct
timestamp = struct.unpack("<i", decoded[0:4])

print timestamp

timestamp = ord(decoded[0]) + ord(decoded[1])*256 + ord(decoded[2])*(256**2) + ord(decoded[3])*(256**3)
print timestamp
reverse = struct.pack("<i", timestamp)
print reverse
#first 4 items properly reversed


print "Extracted timestamp = " + str(timestamp)
import time
from datetime import datetime as dt

datetimestr = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S')
timestamp = time.mktime(dt.strptime(datetimestr,"%Y-%m-%dT%H:%M:%S").timetuple())
print datetimestr
#TIME CORRECTION (SPECIFIC TO YOUR COMPUTER)
timestamp = timestamp - 18000
timestamp = timestamp + 25200
datetimestr = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S')
print datetimestr


#########
#REVERSE ENGINEER
########
#GOAL 2013-12-23T23:35:17 -> tci4UszSJeLN7Ab9xYD4CQ
print "==================================="

#current_time
from time import gmtime, strftime
#CURRENT CLOCK TIME ON PYTHON IS OFF BY 7 HOURS CALIBRATION IS TO ADD 25200 SECONDS
current_time = time.time()+25200
chr()
