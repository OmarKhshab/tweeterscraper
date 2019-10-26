import datetime
from datetime import date

def formatDay(day):
    dayRet = datetime.datetime.strptime(day, "%Y-%m-%d") #year - month - day date format
    return str(dayRet.date())