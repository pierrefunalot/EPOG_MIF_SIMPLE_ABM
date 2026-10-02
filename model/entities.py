from dataclasses import dataclass, field


@dataclass
class Household:
    household_id: int
    bank_id: int
    deposits: float
    propensity_to_consume: float
    employer_id: int | None = None
    income: float = 0.0
    consumption: float = 0.0


@dataclass
class Firm:
    firm_id: int
    bank_id: int
    deposits: float
    productivity: float
    wage: float
    price: float
    expected_demand: float
    inventory: float = 0.0
    debt: float = 0.0
    employees: set[int] = field(default_factory=set)
    sales_quantity: float = 0.0
    previous_sales: float = 0.0
    revenue: float = 0.0
    wage_bill: float = 0.0
    interest_paid: float = 0.0
    profit: float = 0.0


@dataclass
class Bank:
    bank_id: int
    loans: float = 0.0
    interest_income: float = 0.0


@dataclass
class State:
    tax_rate: float
    unemployment_benefit: float
    balance: float = 0.0
    taxes: float = 0.0
    benefits: float = 0.0

