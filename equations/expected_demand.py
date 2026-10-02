def expected_demand(
    previous_expectation: float,
    previous_sales: float,
    adjustment: float,
) -> float:
    """D^e_i,t = (1-alpha) D^e_i,t-1 + alpha D_i,t-1."""
    return (1.0 - adjustment) * previous_expectation + adjustment * previous_sales

