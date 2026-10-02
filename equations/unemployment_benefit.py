def unemployment_benefit(is_employed: bool, benefit: float) -> float:
    """An unemployed household receives the fixed benefit; an employed one receives zero."""
    return 0.0 if is_employed else benefit

