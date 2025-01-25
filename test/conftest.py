import pytest


def pytest_generate_tests(metafunc):
    if "delivery_params" in metafunc.fixturenames:
        delivery_distance = [-1, 1, 2, 15, 35]
        # Expected result of function output
        delivery_cost = [None, 400, 400, 400, 400]
        metafunc.parametrize("delivery_params", [elem for elem in zip(delivery_distance, delivery_cost)],
                             ids=[f"delivery_distance={d}" for d in delivery_distance])
