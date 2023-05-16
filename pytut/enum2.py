from enum import Enum
from pprint import pprint


class Color(Enum):
    RED = 1
    CRIMSON = 1
    SCARLET = 1
    GREEN = 2
    BLUE = 3


print(Color.RED is Color.CRIMSON)  # True
print(Color(1))  # RED
for color in Color:
    print(color)  # RED, GREEN, BLuE
pprint(Color.__members__)  # shows all


class ResponseStatus(Enum):
    # in progress
    IN_PROGRESS = 1
    REQUESTING = 1
    PENDING = 1
    # success
    SUCCESS = 2
    OK = 2
    FULFILLED = 2
    # error
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3


code = 'OK'
if ResponseStatus[code] is ResponseStatus.SUCCESS:
    print('The request completed successfully')


@enum.unique  # ensures no accidental duplicates
class Day(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'


