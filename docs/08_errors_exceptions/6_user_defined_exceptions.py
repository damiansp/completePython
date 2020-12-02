class Error(Exception):
    '''Base class for exceptions in this module'''
    pass


class InputError(Error):
    '''Exception raised for errors in the input.
    Attr:
      expression -- input expression in which err occurred
      message -- explanation to user
    '''
    def __init__(self, expression, message):
        self.expr = expression
        self.msg = message


class TransitionError(Error):
    '''Raised when an operation attempts a state transition that's not allowed
    Attr:
      prev -- state at beginning of transition
      next -- attempted new state
      msg -- explanataion of why transition not allowed
    '''
    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg

