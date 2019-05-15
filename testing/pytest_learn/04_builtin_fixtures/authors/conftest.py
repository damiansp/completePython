'''Demo tmpdir_factory'''
import json

import pytest


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    '''Write some authors to a data file'''
    python_author_data = {'Alice': {'City': 'Alice Springs'},
                          'Betty': {'City': 'Boston'},
                          'Clarence': {'City': 'Cleveland'}}
    file_ = tmpdir_factory.mktemp('data').join('author_file.json')
    print(f'file: {str(file_)}')
    with file_.open('w') as f:
        json.dump(python_author_data, f)
    return file_
