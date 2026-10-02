from dataclasses import asdict


def collect_macro_data(economy) -> dict[str, float]:
    employed = sum(h.employer_id is not None for h in economy.households)
    consumption = sum(h.consumption for h in economy.households)

    return {
        "time": economy.time,
        "nominal_output": consumption,
        "unemployment_rate": 1.0 - employed / len(economy.households),
        "average_price": sum(f.price for f in economy.firms) / len(economy.firms),
        "inventories": sum(f.inventory for f in economy.firms),
        "household_deposits": sum(h.deposits for h in economy.households),
        "firm_deposits": sum(f.deposits for f in economy.firms),
        "bank_loans": sum(b.loans for b in economy.banks),
        "government_balance": economy.state.balance,
        "taxes": economy.state.taxes,
        "benefits": economy.state.benefits,
    }


def bank_deposits(economy, bank_id: int) -> float:
    household_deposits = sum(
        h.deposits for h in economy.households if h.bank_id == bank_id
    )
    firm_deposits = sum(
        f.deposits for f in economy.firms if f.bank_id == bank_id
    )
    return household_deposits + firm_deposits


def final_agent_data(economy) -> list[dict]:
    rows = []
    for household in economy.households:
        row = asdict(household)
        row["agent_type"] = "household"
        rows.append(row)
    for firm in economy.firms:
        row = asdict(firm)
        row["employees"] = len(firm.employees)
        row["agent_type"] = "firm"
        rows.append(row)
    for bank in economy.banks:
        row = asdict(bank)
        row["deposits"] = bank_deposits(economy, bank.bank_id)
        row["agent_type"] = "bank"
        rows.append(row)
    return rows

