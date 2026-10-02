def match_workers(economy, desired_workers: dict[int, int]) -> None:
    """Dismiss excess workers, then fill vacancies through random matching."""
    for firm in economy.firms:
        excess = len(firm.employees) - desired_workers[firm.firm_id]
        if excess > 0:
            dismissed = economy.rng.sample(list(firm.employees), excess)
            for household_id in dismissed:
                firm.employees.remove(household_id)
                economy.households[household_id].employer_id = None

    unemployed = [h for h in economy.households if h.employer_id is None]
    economy.rng.shuffle(unemployed)

    # Extension point: introduce skills, networks, geography or discrimination.
    for firm in economy.firms:
        vacancies = desired_workers[firm.firm_id] - len(firm.employees)
        for _ in range(max(0, vacancies)):
            if not unemployed:
                return
            household = unemployed.pop()
            household.employer_id = firm.firm_id
            firm.employees.add(household.household_id)

