# Data Center Automation Academy

A **simulation-only** educational repository for learning PLC programming, SCADA, and data center automation. No interfaces to real equipment.

## Lab 01 — Cooling control basics

A temperature controller starts a simulated cooling pump at or above 25°C and stops it at or below 23°C. Between those values, it maintains the previous state (hysteresis). Pump and sensor faults stop the pump and raise alarms. This is an educational control example, **not** a recommended real-world equipment safety strategy.

### Requirements
- macOS, Python 3.10+; no third-party Python packages
- VS Code recommended

### Run
```bash
python3 -m src.cooling_lab --steps 60
python3 -m src.cooling_lab --steps 100 --pump-fault-at 20
python3 -m src.cooling_lab --steps 100 --sensor-fault-at 20
python3 -m unittest discover -s tests -v
```

### Tasks
1. Draw a controller/sensor/pump/block diagram.
2. Explain the distinction between process variable, setpoint, hysteresis, and alarm threshold.
3. Run a baseline, pump fault, and sensor fault. Write observations in `docs/lab01-observations.md`.
4. Modify the high-alarm threshold to 27°C; run tests and explain the outcome.
5. **Challenge:** Add a `manual_reset_required` latched fault mode and new unit tests. Keep actual equipment disconnected.

### Passing criteria
All six existing tests pass; you can explain every transition; at least three observations are documented; you complete a fault scenario and discuss safe fallback behavior.

## Next steps
Introduce PLC-style scan logic and Structured Text; exchange simulator data over a local-only simulated protocol; connect Ignition for tags, trending, alarms and an HMI. Do not deploy this toy logic to physical equipment.
