import pyotp
import time
import calendar

totp = pyotp.TOTP("PJ2XG4DCMFXA====")

#test=totp.at(1608766696)

timestamp=calendar.timegm(time.gmtime())

minValue=1608767387%3600

test=totp.at(timestamp)
print(timestamp,test)