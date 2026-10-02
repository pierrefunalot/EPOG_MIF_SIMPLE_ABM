import random

import parameters
from model.collector import final_agent_data
from model.entities import Bank, Firm, Household, State
from model.scheduler import run_period


class Economy:
    """Container for agents, states and simulation history."""

    def __init__(self, config=parameters) -> None:
        self.parameters = config
        self.time: int = 0
        self.rng = random.Random(config.SEED)
        self.history: list[dict[str, float]] = []

        self.banks = [Bank(bank_id=i) for i in range(config.N_BANKS)]
        self.state = State(config.TAX_RATE, config.UNEMPLOYMENT_BENEFIT)

        self.households = [
            Household(
                household_id=i,
                bank_id=i % config.N_BANKS,
                deposits=self.rng.uniform(
                    config.INITIAL_HOUSEHOLD_DEPOSITS_MIN,
                    config.INITIAL_HOUSEHOLD_DEPOSITS_MAX,
                ),
                propensity_to_consume=self.rng.uniform(
                    config.PROPENSITY_TO_CONSUME_MIN,
                    config.PROPENSITY_TO_CONSUME_MAX,
                ),
            )
            for i in range(config.N_HOUSEHOLDS)
        ]

        self.firms = [
            Firm(
                firm_id=i,
                bank_id=i % config.N_BANKS,
                deposits=config.INITIAL_FIRM_DEPOSITS,
                productivity=self.rng.uniform(
                    config.PRODUCTIVITY_MIN, config.PRODUCTIVITY_MAX
                ),
                wage=config.WAGE,
                price=self.rng.uniform(
                    config.INITIAL_PRICE_MIN, config.INITIAL_PRICE_MAX
                ),
                expected_demand=(
                    config.N_HOUSEHOLDS / config.N_FIRMS * 0.65
                ),
            )
            for i in range(config.N_FIRMS)
        ]

    def step(self) -> None:
        run_period(self)
        self.time += 1

    def run(self) -> None:
        for _ in range(self.parameters.PERIODS):
            self.step()

    def final_agent_data(self) -> list[dict]:
        return final_agent_data(self)

