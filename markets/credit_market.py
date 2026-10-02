from equations.debt_repayment import debt_repayment
from equations.interest_payment import interest_payment


def grant_loan(economy, firm, amount: float) -> None:
    """A new bank loan simultaneously creates a firm deposit."""
    if amount <= 0.0:
        return
    firm.deposits += amount
    firm.debt += amount
    economy.banks[firm.bank_id].loans += amount


def service_debt(economy, firm) -> None:
    """Pay interest, then repay a fraction of principal."""
    bank = economy.banks[firm.bank_id]

    firm.interest_paid = interest_payment(
        firm.debt, economy.parameters.INTEREST_RATE, firm.deposits
    )
    firm.deposits -= firm.interest_paid
    bank.interest_income += firm.interest_paid

    repayment = debt_repayment(
        firm.debt, economy.parameters.DEBT_REPAYMENT_RATE, firm.deposits
    )
    firm.deposits -= repayment
    firm.debt -= repayment
    bank.loans -= repayment

