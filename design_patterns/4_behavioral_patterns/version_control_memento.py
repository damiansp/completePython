import time


def main():
    f = File('example.txt')
    repo = Repository()
    f.write('Init content\n')
    repo.commit(f.commit())
    f.write('An update\n')
    repo.commit(f.commit())
    f.write('More updates\n')
    print(f.read())
    f.restore(repo.get_version(1))
    print()
    print(f.read())
    f.restore(repo.get_version(0))
    print()
    print(f.read())


class Commit:
    def __init__(self, content):
        self._content = content
        self._timestamp = time.time()

    def get_content(self):
        return self._content

    def get_timestamp(self):
        return self._timestamp


class File:
    def __init__(self, name):
        self._name = name
        self._content = ''

    def write(self, content):
        self._content += content

    def read(self):
        return self._content

    def commit(self):
        return Commit(self._content)

    def restore(self, commit):
        self._content = commit.get_content()


class Repository:
    def __init__(self):
        self._commits = []

    def commit(self, file_commit):
        self._commits.append(file_commit)

    def get_version(self, idx):
        return self._commits[idx] if 0 <= idx < len(self._commits) else None


if __name__ == '__main__':
    main()
