from collections import UserString


class MutableString(UserString):
    def append(self, s):
        self.data += s

    def remove(self, s):
        self.data = self.data.replace(s, '')


s = MutableString('back')
print('s:', s)
s.append('pack')
print('s:', s)
s.remove('back')
print('s:', s)
