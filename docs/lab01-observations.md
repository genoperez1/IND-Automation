# Lab 01 — Windows observations

**Environment:** Windows version: ____  Python version: ____  Date: ____

## Baseline
Command: `py -m src.cooling_lab --steps 60`

What happened to the temperature and pump state? What explains the transitions?

## Pump fault at scan 20
Command: `py -m src.cooling_lab --steps 100 --pump-fault-at 20`

What changed? Which alarm appears? What should an operator see?

## Sensor fault at scan 20
Command: `py -m src.cooling_lab --steps 100 --sensor-fault-at 20`

Why is an invalid sensor different from a measured high temperature?

## Changed high-alarm threshold
After changing `high_alarm` from 30°C to 27°C, which observations changed? Did all six tests still pass?

## Engineering notes
What redundancy, hardwired interlocks, safe-state definitions, and supervisory alarms would an engineered production system require?
