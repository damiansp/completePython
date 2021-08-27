class A:
    def ping(self):
        print('ping:', self)

class B(A):
    def pong(self):
        print('pong:', self)

class C(A):
    def pong(self):
        print('PONG:', self)

class D(B, C):
    def ping(self):
        super().ping() # same as A.ping(self)
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
print(d.pong())  # pong
print()
print(C.pong(d)) # PONG
print()
print(d.ping())  # ping, post-ping
print()
print(d.pingpong()) # ping, post-ping, ping, pong, pong, PONG
