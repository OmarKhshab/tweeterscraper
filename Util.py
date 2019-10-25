import datetime
from datetime import date

def formatDay(day):
    dayRet = datetime.datetime.strptime(day, "%Y-%m-%d")
    return str(dayRet.date())