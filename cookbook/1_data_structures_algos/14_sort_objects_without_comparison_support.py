from operator import attrgetter


class User:
    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return f'User({self.uid})'


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.uid))

print(sorted(users, key=attrgetter('uid')))
print(max(users, key=attrgetter('uid')))
