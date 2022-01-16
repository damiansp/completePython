from enum import Enum, Flag, auto


class Weekday(Enum):
    MON = 0 # or MON = auto() # to auto iterate
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6


class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    PROCESSED = auto()


class Order:
    def __init__(self):
        self.status = OrderStatus.PENDING

    def process(self):
        if self.status == OrderStatus.PROCESSED:
            raise ValueError(
                "Can't process order that has already been processed")
        self.status = OrderStatus.PROCESSING
        # ...process...
        self.status = OrderStatus.PROCESSED

        
class Side(Flag):
    GUAC = auto()
    TORTILLA = auto()
    FRIES = auto()
    BEER = auto()
    POTATO_SALAD = auto()

mexi_sides = Side.GUAC | Side.BEER | Side.TORTILLA # union
bavarian_sides = Side.BEER | Side.POTATO_SALAD
common_sides = mexi_sides & bavarian_sides         # intersection
print(Side.GUAC in mexi_sides)     # True
print(Side.GUAC in bavarian_sides) # False
print(common_sides)                # Side.BEER
