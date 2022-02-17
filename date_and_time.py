""" Time Module """
from time import strftime

time.localtime() # - Returns the current time
myTime = time.strftime("%A, %b /%d/ %y  %I:%M %p") # - Print date in specified format
fullWeekDay = "%A" # - Day of the week, e.g. Monday, Tuesday, Wednesday
abbrevWeekDay = "%a" # - Abbreviated day of the week, e.g. Mon, Tue, Wed
fullMonthName = "%B" # - Month name e.g. January, February, March, April
abbrevMonthName = "%b" # - Month name abbreviated e.g. Jan, Jun, Mar, Apr
hourMilitary = "%H" # - Current hour in military time: 00 - 23
hourRegular = "%I" # - Current hour in regular time: 01 - 12
minutes = "%M" # - The minutes as a number between 00 and 59
amORpm = "%p" # - AM or PM
seconds = "%S" # - Seconds as number between 00 and 61
abbrevYear = "%y" # - Year without century as a number between 00 and 99
fullYear = "%Y" # - Year as a decimal number
timeZone = "%Z" # - Time zone name
nanoseconds = "%f'

def myTime():
    """ Return current time in format 3:30 PM """
    return strftime("%I:%M %p")

def myMilitaryTime():
    """ Return current time in format 15:30 """
    return strftime("%H:%M")

def myDate():
    """ Return current date in format MM/DD/YYYY """
    return strftime("%m/%d/%Y")

def backwardsDate():
    """ Return current date in format YYYY.MM.DD """
    return strftime("%Y.%m.%d")

def timeStamp():
    """ Return current date in format Monday, January 2018 """
    return strftime("%A, %B %Y")
    
from datetime imoprt datetime
def convert_timestamp_to_epoch():
    timestamp = "2021-09-24T07:23:14.174+00:00"
    epoch_time = int(datetime.fromisoformat(device_time).timestamp())
    return epoch_time
    
####################
# Time stamp
####################
timestamp = strftime("D-%Y-%m-%d__T-%H-%M-%S")
