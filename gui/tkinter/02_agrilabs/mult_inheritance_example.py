class Displayer():
    def display(self, message):
        print(message)


class LoggerMixin():
    '''NOTE: NOT usable alone (super not defined)'''
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)


# Right-most class (Displayer) is "base" class; Displayer becomes "super" to
# LoggerMixin here:
class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')


subclass = MySubClass()
subclass.display('This string should be written to subclasslog.txt')
