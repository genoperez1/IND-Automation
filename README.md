# Data Center Automation Academy — Windows Edition

A **simulation-only** learning path for PLC concepts, SCADA, and data center automation on Windows 10/11. No interfaces to live equipment.

> This is the Windows learning branch (`windows-setup`). The original work on `main`, `geno-dev`, and `elijah-dev` remains intact.

## Lab 01 — Cooling control basics

Start from a clean Windows environment, run a simple Python cooling plant, inspect pump switching with hysteresis, and simulate faults.

### Prerequisites
- Windows 10 or 11
- Python 3.10 or newer from [python.org](https://www.python.org/downloads/windows/) (enable the Python launcher or add Python to PATH)
- [Git for Windows](https://git-scm.com/downloads/win)
- [Visual Studio Code](https://code.visualstudio.com/) and the Microsoft Python extension

No third-party Python packages required for Lab 01.

### 1. Clone the Windows branch

Open **PowerShell** (or VS Code's PowerShell terminal):

```powershell
git clone --branch windows-setup https://github.com/genoperez1/IND-Automation.git
cd IND-Automation
git status
```

Already have the repository locally?

```powershell
git fetch origin
git switch windows-setup
git pull --ff-only origin windows-setup
```

Save/commit any local work before switching branches.

### 2. Check Python and run the simulation

```powershell
py --version
py -m src.cooling_lab --steps 60
py -m src.cooling_lab --steps 100 --pump-fault-at 20
py -m src.cooling_lab --steps 100 --sensor-fault-at 20
py -m unittest discover -s tests -v
```

If the `py` launcher is unavailable, use `python` instead after confirming `python --version` works. Run these commands from the repository root.

All **six baseline tests** should pass.

### 3. Understand the simulation

- The pump turns on at or above 25°C (24°C setpoint + 1°C hysteresis).
- The pump turns off at or below 23°C (24°C setpoint - 1°C hysteresis).
- Between 23°C and 25°C, pump state stays unchanged.
- A pump fault or invalid sensor inhibits the simulated pump and raises an alarm.
- The default high-temperature alarm threshold is 30°C.

This is a teaching model, **not** a real-world equipment safety strategy. Production cooling controls require engineered safety review and equipment-specific interlocks.

### 4. Complete the lab

1. Draw a block diagram: temperature sensor → controller → simulated pump → thermal plant.
2. Explain process variable, setpoint, hysteresis, and alarm threshold.
3. Run baseline, pump-fault, and sensor-fault cases; record results in `docs/lab01-observations.md`.
4. Change `high_alarm` in `src/cooling_lab.py` from 30°C to 27°C; re-run tests and document what changes.
5. **Challenge:** implement a `manual_reset_required` latched-fault mode and add unit tests.

**Passing criteria:** Six original tests pass; you can explain every switching transition; at least three observations are recorded; a fault scenario and simulated fallback behavior are discussed.

## Git workflow for the Windows branch

```powershell
git status
git switch windows-setup
git add .
git commit -m "Complete Lab 01 observations"
git push -u origin windows-setup
```

Use a separate feature branch for experimental work when collaborating. Do not force-push shared branches.

## Roadmap

Lab 01: Python cooling simulation and faults → PLC-style scan logic and Structured Text → local-only simulated communications → Ignition tags, alarms, trends, and HMI. Later labs will document both Windows-native tools and macOS equivalents where available.

## Important safety boundary

Only use simulated/local data. Never connect these examples to physical PLCs, live data-center systems, or operational networks.
