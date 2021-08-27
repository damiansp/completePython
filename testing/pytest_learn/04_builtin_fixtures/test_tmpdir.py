TEXT1 = 'contents may settle during shipping'
TEXT2 = 'something different'

def test_tmpdir(tmpdir):
    # tmpdir already has a path name associated with it; join() extends the path
    # to include a filename; the file is created when written to
    a_file = tmpdir.join('something.txt')
    a_sub_dir = tmpdir.mkdir('anything') # create subdir
    another_file = a_sub_dir.join('something_else.txt')
    a_file.write(TEXT1)
    another_file.write(TEXT2)
    assert a_file.read() == TEXT1
    assert another_file.read() == TEXT2


def test_tmpdir_factory(tmpdir_factory):
    # should start with making a dir; a_dir acts like the obj returned by tmpdir
    # fixture
    a_dir = tmpdir_factory.mktemp('mydir')
    # base_tmp will be the parent dir of mydir; don't have to use getbasetemp(),
    # use here just to show it's availability
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)
    a_file = a_dir.join('somthing.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')
    a_file.write(TEXT1)
    another_file.write(TEXT2)
    assert a_file.read() == TEXT1
    assert another_file.read() == TEXT2
