'''
NOTE: Current implementation will work with ECS Tasks (both Fargate and EC2 
variants). Not yet comaptible with Lambdas.

Don't forget to add:
stats, datadog
to requirements.txt as needed.
'''
import logging

from .keys_handler import get_secret


class Logger:
    def __init__(self, logfile, min_level='info', print_too=True):
        ''' 
        Args:
          - logfile (str): path and file where logs are to be written
          - min_level (str): see `levels` below (given in increasing order) -
              Only messages of this level or higher will be logged
        '''
        self.print_too = print_too
        self.levels = {'debug': logging.DEBUG,
                       'info': logging.INFO,
                       'warning': logging.WARNING,
                       'error': logging.ERROR,
                       'critical': logging.CRITICAL}
        self.level = self.levels[min_level]
        logging.basicConfig(filename=logfile, level=self.level)

    def log(self, msg, level='info'):
        if self.print_too:
            print(msg)
        {
            'debug': logging.debug,
            'info': logging.info,
            'warning': logging.warning,
            'error': logging.error,
            'critical': logging.critical
        }[level](msg.encode('utf-8'))

    def linesep(self):
        self.log('-' * 70)


class StatsdLogger(Logger):
    def __init__(
            self, logfile, prefix=None, min_level='info', print_too=True,
            log_env='qa', process=None,
            host='metrics.aws.cbtnuggets.com', port=8125):
        '''
        Args:
          - logfile (str): path and file where logs are to be written (typically
            process-name.log)
          - min_level (str), print_too (bool): see Logger above
          - prefix (str): name to use for logging, defaults to last segment of
            process name (eg. if logfile = 'task-analytics-myDataToS3.log', then
            prefix = 'myDataToS3')
          - log_env (str): typically = AWS_ENV (= 'qa' or 'prod')
          - process (str): name of task/lambda/etc. if None, taken from logfile
            name

        Ex:
        TASK = 'task-analytics-myProcessToS3'
        AWS_ENV = 'prod' if ENV == 'prod' else 'qa'
        LOGGER = StatsdLogger(logfile=f'{TASK}.log', log_env=AWS_ENV)

        ...in this case:
        - prefix = 'myProcessToS3'
        - process = 'task-analytics-myProcessToS3'
        '''
        from statsd import StatsClient
        
        super().__init__(logfile, min_level, print_too)
        self.client = StatsClient(
            host=host, port=port, prefix=f'{log_env}.{process}')
        self.process = (logfile.replace('.log', '')  if process is None
                        else process)
        self.shortname = self.process.split('-')[-1]
        self.prefix = prefix if prefix is not None else self.shortname

    def log(self, msg, count=1, level='info'):
        super().log(msg, level)
        self.client.incr(f'{self.prefix}_{msg}', count)


class DataDogLogger(StatsdLogger):
    def __init__(
            self, logfile, prefix=None, min_level='info', print_too=True,
            log_env='qa', process=None, host='metrics.aws.cbtnuggets.com',
            port=8125):
        '''Args: Same as StatsdLogger'''
        from datadog import initialize, ThreadStats

        super().__init__(
            logfile, prefix, min_level, print_too, log_env, process, host, port)
        self.process = process
        dd_api_key = get_secret('/shared/datadog/api-key')
        dd_app_key = get_secret('/shared/datadog/app-key')
        dd_options = {'api_key': dd_api_key['apikey'],
                      'app_key': dd_app_key['applicationkey'],
                      'statsd_host': host,
                      'statsd_port': port}
        print('Initializing Data Dog Connection...')
        initialize(**dd_options)
        self.tags = [f'environment:{log_env}', f'process:{process}']
        self.stats = ThreadStats()
        self.stats.start()

    def log(self, msg, count=1, level='info', dd_msg=None):
        super().log(msg, count, level)
        if dd_msg is not None:
            self._push_data_dog_metrics(dd_msg.replace(' ', '_'), count)

    def _push_data_dog_metrics(self, msg, count):
        self.stats.increment(f'{self.process}.{msg}',
                             tags=self.tags + [f'payload:{count}'])

