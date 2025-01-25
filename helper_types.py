from enum import Enum


class CargoSizeSurcharge(int, Enum):
    LARGE = 200
    SMALL = 100


class CargoFragility(Enum):
    FRAGILE = True
    NOT_FRAGILE = False


class DeliveryLoadMultiplier(float, Enum):
    EXTREMELY_HIGH = 1.6
    HIGH = 1.4
    ELEVATED = 1.2
    NORMAL = 1.0


class DeliveryOrder:
    def __init__(self,
                 distance: float,
                 size: CargoSizeSurcharge,
                 fragility: CargoFragility,
                 delivery_load_multiplier: DeliveryLoadMultiplier):

        self.distance = distance
        self.size = size
        self.fragility = fragility
        self.delivery_load_multiplier = delivery_load_multiplier
