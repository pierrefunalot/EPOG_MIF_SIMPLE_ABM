from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
data = pd.read_csv(OUTPUTS / "macro_history.csv")

fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
axes[0].plot(data["time"], data["nominal_output"], color="#5b2a86")
axes[0].set_ylabel("Nominal output")
axes[0].set_title("Economic activity")
axes[1].plot(data["time"], 100 * data["unemployment_rate"], color="#c44e52")
axes[1].set_ylabel("Unemployment (%)")
axes[1].set_xlabel("Period")
fig.tight_layout()
fig.savefig(OUTPUTS / "activity_and_unemployment.png", dpi=180)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(data["time"], data["household_deposits"], label="Household deposits")
ax.plot(data["time"], data["firm_deposits"], label="Firm deposits")
ax.plot(data["time"], data["bank_loans"], label="Bank loans")
ax.plot(data["time"], data["government_balance"], label="Government balance")
ax.set_xlabel("Period")
ax.set_ylabel("Monetary units")
ax.set_title("Money and credit")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUTPUTS / "money_and_credit.png", dpi=180)
plt.close(fig)

print(f"Figures saved in: {OUTPUTS}")

