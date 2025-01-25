from helper_types import *


def calculate_delivery_cost(distance: float,
                            size: CargoSizeSurcharge,
                            fragility: CargoFragility,
                            delivery_load_multiplier: DeliveryLoadMultiplier) -> float:

    base_cost = 0
    fragile_cargo_surcharge = 300 * fragility.value
    min_cost = 400

    if distance > 30:
        if fragility.value:
            raise ValueError("Fragile cargo is not allowed to be delivered so far away")
        base_cost += 300
    elif 10 <= distance <= 30:
        base_cost += 200
    elif 2 <= distance < 10:
        base_cost += 100
    elif distance <= 0:
        raise ValueError("Delivery distance must be > 0")
    else:
        base_cost += 50

    print(delivery_load_multiplier.value, base_cost, size, fragile_cargo_surcharge)
    total_cost = delivery_load_multiplier.value * (base_cost + size + fragile_cargo_surcharge)

    return max(min_cost, total_cost)
