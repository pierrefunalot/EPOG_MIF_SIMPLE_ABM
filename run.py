from pathlib import Path

import pandas as pd

from model import Economy


ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

economy = Economy()
economy.run()

macro = pd.DataFrame(economy.history)
agents = pd.DataFrame(economy.final_agent_data())

macro.to_csv(OUTPUTS / "macro_history.csv", index=False)
agents.to_csv(OUTPUTS / "agents_final.csv", index=False)

print(macro.tail())
print(f"\nOutputs saved in: {OUTPUTS}")

