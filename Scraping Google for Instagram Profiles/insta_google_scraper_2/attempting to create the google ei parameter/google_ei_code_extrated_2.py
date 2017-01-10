#########
#REVERSE ENGINEER
########



import datetime
from datetime import datetime as dt
import time
from time import gmtime, strftime

#CURRENT CLOCK TIME ON PYTHON IS OFF BY 7 HOURS CALIBRATION IS TO ADD 25200 SECONDS
current_time_stamp = time.time()+25200
print current_time

#TIME CHECK
##datetimestr = datetime.datetime.utcfromtimestamp(current_time).strftime('%Y-%m-%dT%H:%M:%S')
##print datetimestr
##timestamp = time.mktime(dt.strptime(datetimestr,"%Y-%m-%dT%H:%M:%S").timetuple())
##print timestamp


