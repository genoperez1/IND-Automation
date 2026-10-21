import unittest
from src.cooling_lab import CoolingPlant

class CoolingPlantTests(unittest.TestCase):
    def test_high_temp_starts_pump(self):
        p = CoolingPlant(temperature=28)
        self.assertTrue(p.scan()['pump_running'])

    def test_low_temp_stops_pump(self):
        p = CoolingPlant(temperature=22, pump_running=True)
        self.assertFalse(p.scan()['pump_running'])

    def test_deadband_maintains_state(self):
        p = CoolingPlant(temperature=24, pump_running=True)
        self.assertTrue(p.scan()['pump_running'])

    def test_pump_fault_inhibits_pump(self):
        p = CoolingPlant(temperature=30, pump_fault=True)
        output = p.scan()
        self.assertFalse(output['pump_running'])
        self.assertTrue(output['pump_fault_alarm'])

    def test_sensor_fault_inhibits_pump(self):
        p = CoolingPlant(temperature=30, sensor_valid=False)
        output = p.scan()
        self.assertFalse(output['pump_running'])
        self.assertTrue(output['sensor_fault_alarm'])

    def test_invalid_scan_interval(self):
        with self.assertRaises(ValueError):
            CoolingPlant().scan(dt=0)

if __name__ == '__main__':
    unittest.main()
