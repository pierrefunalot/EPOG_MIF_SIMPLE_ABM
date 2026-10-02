def interest_payment(debt: float, interest_rate: float, available_deposits: float) -> float:
    """Interest paid is constrained by the firm's available deposits."""
    return min(interest_rate * debt, available_deposits)

