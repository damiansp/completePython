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


class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_timer = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return (f'NewBucket(max_quota={self.max_quota}, '
                f'quota_consumed={self.quota_consumed}')

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amt):
        delta = self.max_quota - amt
        if amt == 0:
            # quota being reset for new pd.
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # quota being filled for new pd.
            assert self.quota_consumed == 0
            self.max_quota = amt
        else:
            # quota being consumed during pd.
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


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
