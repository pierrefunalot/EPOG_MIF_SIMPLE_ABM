from equations.consumption_budget import consumption_budget


def choose_supplier(economy):
    """Cheaper firms are more likely to be selected, but choice is imperfect."""
    weights = [1.0 / firm.price for firm in economy.firms]
    return economy.rng.choices(economy.firms, weights=weights, k=1)[0]


def trade(economy) -> None:
    households = economy.households.copy()
    economy.rng.shuffle(households)

    # Extension point: networks, several goods, brands or ecological quality.
    for household in households:
        budget = consumption_budget(
            household.deposits, household.propensity_to_consume
        )
        firm = choose_supplier(economy)
        desired_quantity = budget / firm.price
        quantity = min(desired_quantity, firm.inventory)
        expenditure = quantity * firm.price

        household.deposits -= expenditure
        household.consumption += expenditure
        firm.deposits += expenditure
        firm.inventory -= quantity
        firm.sales_quantity += quantity
        firm.revenue += expenditure

