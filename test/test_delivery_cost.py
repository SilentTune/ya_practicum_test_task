import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helper_types import *
from calculate_delivery_cost import calculate_delivery_cost


class TestDeliveryCost:

    def test_delivery_distance(self, delivery_params):
        delivery_distance, expected_cost = delivery_params
        try:
            delivery_cost = calculate_delivery_cost(distance=delivery_distance,
                                                    size=CargoSizeSurcharge.SMALL,
                                                    fragility=CargoFragility.NOT_FRAGILE,
                                                    delivery_load_multiplier=DeliveryLoadMultiplier.NORMAL)
        except ValueError:
            if delivery_distance <= 0:
                assert True, "Function calculation fault"
        else:
            assert expected_cost == delivery_cost, "Function calculation fault"

    def test_minimal_cost_threshold(self):
        assert 400 == calculate_delivery_cost(distance=1,
                                              size=CargoSizeSurcharge.SMALL,
                                              fragility=CargoFragility.NOT_FRAGILE,
                                              delivery_load_multiplier=DeliveryLoadMultiplier.NORMAL)

    @pytest.mark.parametrize("delivery_distance", [10, 350], ids=[f"delivery_distance={dd}" for dd in [10, 350]])
    def test_fragile_cargo_delivery_distance_limit(self, delivery_distance):
        try:
            calculate_delivery_cost(distance=delivery_distance,
                                    size=CargoSizeSurcharge.SMALL,
                                    fragility=CargoFragility.FRAGILE,
                                    delivery_load_multiplier=DeliveryLoadMultiplier.NORMAL)
        except ValueError:
            if delivery_distance > 30:
                assert True
            else:
                assert False

    def test_high_cost_delivery(self):
        distance = 30.0
        delivery_order = DeliveryOrder(
            distance=distance,
            size=CargoSizeSurcharge.LARGE,
            fragility=CargoFragility.FRAGILE,
            delivery_load_multiplier=DeliveryLoadMultiplier.EXTREMELY_HIGH
        )
        expected_output = delivery_order.delivery_load_multiplier * \
                          (200 + delivery_order.size + 300 * delivery_order.fragility.value)
        func_output = calculate_delivery_cost(distance=distance,
                                              size=delivery_order.size,
                                              fragility=delivery_order.fragility,
                                              delivery_load_multiplier=delivery_order.delivery_load_multiplier)

        assert expected_output == func_output, f"{expected_output} != {func_output}"
