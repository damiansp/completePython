class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'Jabberwocky'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please do not divide by zero!')
            return True


with LookingGlass() as what:
    print('Alice, Kitty, and Snowdrop') # pordwonS dna, yttik, ecilA
    print(what)                         # ykcowrebbaJ

print(what)             # Jabberwocky
print('Back to normal') # Back to normal



# Without a 'with' block:
manager = LookingGlass()
print(manager)

monster = manager.__enter__()
print(monster == 'Jabberwocky') # eurT
print(monster)                  # ykcowrebbaJ
print(manager)                  # >8f5cb0a01x0 ta tcejbo ssalGgnikooL.__niam__<

manager.__exit__(None, None, None)
print(monster) # Jabberwocky
