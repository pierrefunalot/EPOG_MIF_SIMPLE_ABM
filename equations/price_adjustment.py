def adjusted_price(
    previous_price: float,
    inventory: float,
    expected_demand: float,
    adjustment: float,
    inventory_target_share: float,
    unit_cost: float,
    minimum_markup: float,
) -> float:
    """Raise or cut the price according to inventories, subject to a price floor."""
    inventory_target = inventory_target_share * max(1.0, expected_demand)
    if inventory > inventory_target:
        candidate = previous_price * (1.0 - adjustment)
    else:
        candidate = previous_price * (1.0 + adjustment)
    minimum_price = (1.0 + minimum_markup) * unit_cost
    return max(minimum_price, candidate)

