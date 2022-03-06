# Example of configuring and unpacking large sets of environmental variables
from datetime import timedelta

import environ  # pip3 install environ-config


@environ.config(prefix='')
class Config:

    @environ.config()
    class Bind:
        host = environ.var(default='localhost')
        port = environ.var(default='80', converter=int)

    bind = environ.group(Bind)
    database_uri = environ.var()
    encryption_key = environ.var()
    schedule_interval = environ.var(
        name='SCHEDULE_INTERVAL_SECONDS',
        converter=lambda val: timedelta(seconds=int(val))
        default=50)


if __name__ == '__main__':
    config = Config.from_environ()
    print(config.bind)  # Config.Bind(host='localhost', port=80)
    print(config.schedule_interval)  # datetime.timedelta(seconds=50)
