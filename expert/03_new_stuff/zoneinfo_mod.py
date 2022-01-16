from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(1976, 11, 3, tzinfo=ZoneInfo('Europe/Rome'))
print(dt)
