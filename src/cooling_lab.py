"""Educational closed-loop cooling simulation. No real equipment interfaces."""
from dataclasses import dataclass
import argparse


@dataclass
class CoolingPlant:
    temperature: float = 28.0
    setpoint: float = 24.0
    high_alarm: float = 27.0
    hysteresis: float = 1.0
    pump_running: bool = False
    pump_fault: bool = False
    sensor_valid: bool = True
    ambient: float = 32.0

    def scan(self, dt: float = 1.0) -> dict:
        if dt <= 0 or dt > 10:
            raise ValueError('dt must be between 0 and 10 seconds')
        # Simulation fallback only; not a real equipment safety strategy.
        if self.pump_fault or not self.sensor_valid:
            self.pump_running = False
        elif self.temperature >= self.setpoint + self.hysteresis:
            self.pump_running = True
        elif self.temperature <= self.setpoint - self.hysteresis:
            self.pump_running = False
        heat_gain = 0.025 * (self.ambient - self.temperature)
        cooling = 0.22 if self.pump_running else 0.0
        self.temperature += dt * (heat_gain - cooling)
        return {
            'temperature_c': round(self.temperature, 2),
            'pump_running': self.pump_running,
            'high_temperature_alarm': self.temperature >= self.high_alarm,
            'pump_fault_alarm': self.pump_fault,
            'sensor_fault_alarm': not self.sensor_valid,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description='Data center cooling control sandbox')
    parser.add_argument('--steps', type=int, default=60)
    parser.add_argument('--pump-fault-at', type=int, default=-1)
    parser.add_argument('--sensor-fault-at', type=int, default=-1)
    args = parser.parse_args()
    if args.steps < 1 or args.steps > 10000:
        parser.error('--steps must be 1..10000')
    plant = CoolingPlant()
    for i in range(args.steps):
        if i == args.pump_fault_at:
            plant.pump_fault = True
        if i == args.sensor_fault_at:
            plant.sensor_valid = False
        result = plant.scan()
        print(f"scan={i:03d} temp={result['temperature_c']:5.2f}C "
              f"pump={'ON ' if result['pump_running'] else 'OFF'} "
              f"high_alarm={result['high_temperature_alarm']} "
              f"pump_fault={result['pump_fault_alarm']} "
              f"sensor_fault={result['sensor_fault_alarm']}")


if __name__ == '__main__':
    main()
