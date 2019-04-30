# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required, owner & done are optional, id set by DB

@pytest.fixture()
def tasks_just_a_few():
    '''All summaries and owners are unique'''
    return (Task('write some code', 'Cody', True),
            Task('review cody\'s code', 'Reggie', False),
            Task('fix reggie\'s flaws', 'Fiona', False))

@pytest.fixture()
def tasks_mult_per_owner():
    '''Several owners with several tasks each'''
    return(Task('make cookies', 'Raphael'),
           Task('emote', 'Raphael'),
           Task('move to berlin', 'Raphael'),
           Task('multilpy', 'Michelle'),
           Task('magnify', 'Michelle'),
           Task('minimize', 'Michelle'),
           Task('dance', 'Daniel'),
           Task('destroy', 'Daniel'),
           Task('devestate', 'Daniel'))
