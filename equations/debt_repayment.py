def debt_repayment(debt: float, repayment_rate: float, available_deposits: float) -> float:
    """R_i,t = min(rho L_i,t, D_i,t)."""
    return min(repayment_rate * debt, available_deposits)

