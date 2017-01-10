import time
from datetime import datetime as dt
s = "01/12/2011"
datetime = "2013-12-23T23:35:17"
##s = datetime
##print datetime
##the_time = time.mktime(dt.strptime("2013-12-23T23:35:17","%Y-%m-%dT%H:%M:%S").timetuple())
##print the_time
####time.mktime(datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S").timetuple())
##datetimestr = dt.utcfromtimestamp(the_time).strftime('%Y-%m-%dT%H:%M:%S')
##print datetimestr


##(timedelta-dt(1970,1,1)).total_seconds()

##from datetime import datetime
##import time
##s = "16/08/2013 09:51:43"
##d = datetime.strptime(s, "%d/%m/%Y %H:%M:%S")
##time.mktime(d.timetuple())


from datetime import datetime
import time
s = "2013-12-23T23:35:17"
print s
d = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
timestamp = time.mktime(d.timetuple())
print timestamp
wrongtime = 1387859717
correcttime = 1387841717
print correcttime - wrongtime

print datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S')
print datetime.utcfromtimestamp(correcttime).strftime('%Y-%m-%dT%H:%M:%S')



##2013-12-23T23:35:17
##1387859717.0
##-18000
##2013-12-24T04:35:17
##2013-12-23T23:35:17
