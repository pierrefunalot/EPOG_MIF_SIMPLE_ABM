from equations.expected_demand import expected_demand
from equations.firm_profit import firm_profit
from equations.income_tax import income_tax
from equations.labour_demand import labour_demand
from equations.price_adjustment import adjusted_price
from equations.production import production
from equations.unemployment_benefit import unemployment_benefit
from equations.wage_bill import wage_bill
from markets.credit_market import grant_loan, service_debt
from markets.goods_market import trade
from markets.labour_market import match_workers
from model.collector import collect_macro_data


def run_period(economy) -> None:
    """Order all events in one model period."""
    desired_workers = form_expectations_and_plans(economy)
    reset_period_flows(economy)
    match_workers(economy, desired_workers)
    produce_and_pay_wages(economy)
    implement_fiscal_policy(economy)
    trade(economy)
    settle_firm_accounts(economy)
    adapt_firms(economy)
    economy.history.append(collect_macro_data(economy))


def form_expectations_and_plans(economy) -> dict[int, int]:
    plans = {}
    for firm in economy.firms:
        if economy.time > 0:
            firm.expected_demand = expected_demand(
                firm.expected_demand,
                firm.sales_quantity,
                economy.parameters.EXPECTATION_ADJUSTMENT,
            )
        plans[firm.firm_id] = labour_demand(
            firm.expected_demand,
            firm.productivity,
            economy.parameters.PRODUCTION_BUFFER,
        )
    return plans


def reset_period_flows(economy) -> None:
    economy.state.taxes = 0.0
    economy.state.benefits = 0.0
    for household in economy.households:
        household.income = 0.0
        household.consumption = 0.0
    for firm in economy.firms:
        firm.previous_sales = firm.sales_quantity
        firm.sales_quantity = 0.0
        firm.revenue = 0.0
        firm.wage_bill = 0.0
        firm.interest_paid = 0.0
    for bank in economy.banks:
        bank.interest_income = 0.0


def produce_and_pay_wages(economy) -> None:
    for firm in economy.firms:
        firm.inventory += production(firm.productivity, len(firm.employees))
        firm.wage_bill = wage_bill(firm.wage, len(firm.employees))
        grant_loan(economy, firm, max(0.0, firm.wage_bill - firm.deposits))
        firm.deposits -= firm.wage_bill
        for household_id in firm.employees:
            household = economy.households[household_id]
            household.deposits += firm.wage
            household.income += firm.wage


def implement_fiscal_policy(economy) -> None:
    for household in economy.households:
        benefit = unemployment_benefit(
            household.employer_id is not None,
            economy.state.unemployment_benefit,
        )
        household.deposits += benefit
        household.income += benefit
        economy.state.benefits += benefit
        economy.state.balance -= benefit

        tax = income_tax(household.income, economy.state.tax_rate)
        household.deposits -= tax
        economy.state.taxes += tax
        economy.state.balance += tax


def settle_firm_accounts(economy) -> None:
    for firm in economy.firms:
        service_debt(economy, firm)
        firm.profit = firm_profit(firm.revenue, firm.wage_bill, firm.interest_paid)


def adapt_firms(economy) -> None:
    for firm in economy.firms:
        firm.price = adjusted_price(
            previous_price=firm.price,
            inventory=firm.inventory,
            expected_demand=firm.expected_demand,
            adjustment=economy.parameters.PRICE_ADJUSTMENT,
            inventory_target_share=economy.parameters.INVENTORY_TARGET_SHARE,
            unit_cost=firm.wage / firm.productivity,
            minimum_markup=economy.parameters.MINIMUM_MARKUP,
        )
        # Extension point: imitation, innovation, entry, exit or new routines.
