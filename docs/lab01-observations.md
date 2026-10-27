# Lab 01 — Windows observations

**Environment:** Windows version: __11__  Python version: _3.13.14_  Date: _10/26/2026_

## Baseline
Command: `py -m src.cooling_lab --steps 60`

> What happened to the temperature and pump state? What explains the transitions?
>> The temperature continued to lower, while the pump and alarm states stayed the same.
>> This is due to hysteresis, which is the intentional delay between shut-off and turn-on -- it prevents rapid cycling.

## Pump fault at scan 20
Command: `py -m src.cooling_lab --steps 100 --pump-fault-at 20`

> What changed? Which alarm appears? What should an operator see?
>> pump_fault alarm triggered the 

## Sensor fault at scan 20
Command: `py -m src.cooling_lab --steps 100 --sensor-fault-at 20`

> Why is an invalid sensor different from a measured high temperature?
>> There is no measurement of temperature that would satisfy the on -off resulting in the last state to remain. Also doesn't show reliable data.

## Changed high-alarm threshold
> After changing `high_alarm` from 30°C to 27°C, which observations changed? Did all six tests still pass?
>> Changing the high_alarm to 27 caused the alarm to trigger at scan 26 instead of 60. All test still passed due to them not testing high temp alarms.
## Engineering notes
> What redundancy, hardwired interlocks, safe-state definitions, and supervisory alarms would an engineered production system require?
>> By having multiple alarm set points it allows engineers a early warning before a high alarm happens.