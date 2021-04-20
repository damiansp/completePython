from datetime import datetime, timedelta


class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota={self.quota})'

def fill(bucket, amt):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amt


def deduct(bucket, amt):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False # bucket hasn't been filled this pd
    if bucket.quota - amt < 0:
        return False # bucket filled, but not enough
    bucket.quota -= amt
    return True # bucket had enough; quota consumed


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)
if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
