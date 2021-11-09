# https://docs.python.org/3/library/time.html

from time import strftime, time, gmtime
import time
import datetime
import os
os.system("cls")


# [DATETIME TO STRING]
now = gmtime()
print(strftime("%Y-%m-%d %H:%M:%S", now)) # yyyy-mm-dd hh:mm:ss
print(strftime("%x", now)) # mm/dd/yy
print(strftime("%X", now)) # hh:mm:ss
print(strftime("%a", now)) # Sun, Mon, Tue...
print(strftime("%A", now)) # Sunday, Monday, Tuesday
print(strftime("%b", now)) # Jan, Feb, Mar
print(strftime("%B", now)) # January, February, March
print(strftime("%c", now)) # Tue Nov  9 11:30:51 2021
print(strftime("%w", now)) # weekday 0 - 6
print(strftime("%z", now)) # timezone -0300

# [STRING TO DATETIME]
now = time.strptime("30 Nov 00", "%d %b %y")        # 2 digit [y]ear
print(strftime("%Y-%m-%d %H:%M:%S", now))

now = time.strptime("30 Nov 1999", "%d %b %Y")      # 4 digit [Y]ear
print(strftime("%Y-%m-%d %H:%M:%S", now))

now = time.strptime("23:59", "%H:%M")               # time only
print(strftime("%Y-%m-%d %H:%M:%S", now))

now = time.strptime("30 Nov 1999 23:59", "%d %b %Y %H:%M")      # full datetime
print(strftime("%Y-%m-%d %H:%M:%S", now))

d0 = datetime.fromtimestamp("Sun 10 May 2015 13:54:36").strftime("%A, %B %d, %Y %I:%M:%S") # Best form !!!
print(d0)