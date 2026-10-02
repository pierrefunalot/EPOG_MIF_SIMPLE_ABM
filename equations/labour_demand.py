import math


def labour_demand(
    expected_demand: float,
    productivity: float,
    production_buffer: float,
) -> int:
    """Desired workers required to produce expected demand plus a buffer."""
    desired_output = (1.0 + production_buffer) * expected_demand
    return max(1, math.ceil(desired_output / productivity))

