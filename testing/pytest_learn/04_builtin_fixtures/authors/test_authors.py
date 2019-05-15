'''Tests using temp data files'''
import json


def test_alice_in_alice_springs(author_file_json):
    '''Test using a data file'''
    with author_file_json.open() as f:
        authors = json.load(f)
    assert authors['Alice']['City'] == 'Alice Springs'


def test_all_have_cities(author_file_json):
    '''Same file used for both tests'''
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0
