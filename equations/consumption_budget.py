def consumption_budget(deposits: float, propensity_to_consume: float) -> float:
    """C^d_h,t = c_h D_h,t."""
    return propensity_to_consume * deposits

