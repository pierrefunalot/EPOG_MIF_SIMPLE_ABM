# A minimal evolutionary agent-based economy

This repository contains a deliberately small Python economy with households,
firms, banks and a state. It is a starting point for student projects, not a
forecasting model.

## Before you begin

Install Python 3.10 or later, Visual Studio Code and the Microsoft Python
extension for VS Code. After extracting the archive, open the folder that
directly contains `requirements.txt`, `run.py`, `model`, `equations` and
`markets`.

## Installation on Windows

Open a new VS Code terminal in the project folder and run:

```powershell
py --version
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

These commands use the project's Python directly. Activating the virtual
environment is optional, so PowerShell's script policy cannot block the setup.

Run the model and create the figures:

```powershell
.venv\Scripts\python.exe run.py
.venv\Scripts\python.exe plot_outputs.py
```

## Installation on macOS or Linux

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python run.py
.venv/bin/python plot_outputs.py
```

## Model architecture

```text
parameters.py            calibration values
run.py                   launches one simulation
plot_outputs.py          creates figures from the CSV output

model/
    entities.py          state variables carried by agents
    model.py             creates and stores the economy
    scheduler.py         orders all mechanisms within a period
    collector.py         constructs observable outputs

equations/               one equation or autonomous rule per file
markets/                 interaction, matching, trading and rationing protocols
tests/                   checks equations and the complete model
outputs/                 generated CSV files and figures
```

The central coding convention is:

> One equation or autonomous behavioural mechanism, one Python file; one
> interaction protocol, one market module.

## What happens during one period?

`model/scheduler.py` makes the sequence explicit:

1. firms form expectations and production plans;
2. the labour market matches unemployed households and firms;
3. firms produce and pay wages, borrowing when necessary;
4. the state pays benefits and collects taxes;
5. households and firms meet on the goods market;
6. firms service their bank debt;
7. firms adapt prices;
8. the collector records macroeconomic outcomes.

Loans create firm deposits; principal repayments reduce loans and deposits.
Other payments transfer deposits between agents. Government spending increases
private deposits, whereas taxes reduce them.

## Generated outputs

The `outputs` folder contains `macro_history.csv`, `agents_final.csv`,
`activity_and_unemployment.png` and `money_and_credit.png`.

## How to modify the model

### Change an existing equation

To change consumption behaviour, edit only
`equations/consumption_budget.py`, then rerun the tests and the model.

### Add a parameter

Add its baseline value and type to `parameters.py`, then pass it explicitly to
the equation that uses it.

### Add a new state variable

1. add it to the relevant class in `model/entities.py`;
2. initialise it in `model/model.py`;
3. update it through an equation or market protocol;
4. expose it in `model/collector.py` if it should appear in the outputs.

### Add a new mechanism

1. write the equation in a new file under `equations/`, or the interaction
   protocol in a new file under `markets/`;
2. import it in `model/scheduler.py`;
3. call it at the economically correct point in the period;
4. add a test;
5. compare a baseline run with the modified model.

## Run the tests

Windows:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests
```

macOS or Linux:

```bash
.venv/bin/python -m unittest discover -s tests
```

## Possible extensions

Students can add green and brown technologies, bank credit rationing, a carbon
tax, household networks, ecological preferences, firm imitation, innovation,
entry and exit, several sectors or alternative fiscal rules.

The baseline is intentionally incomplete. Banks do not default, firms cannot
exit, households buy one homogeneous good and the state faces no financing
constraint. These omissions are possible research questions rather than hidden
claims about the economy.
