import datetime


print('Available date range:', datetime.MINYEAR, datetime.MAXYEAR)

now = datetime.datetime.now()
utc_now = datetime.datetime.utcnow()
print('tzinfo:', now.tzinfo, utc_now.tzinfo)  # None, None

