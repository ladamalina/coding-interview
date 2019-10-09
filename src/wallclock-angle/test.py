import unittest
from wallclock_angle_calculator import WallclockAngleCalculator


class WallclockAngleCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.positive_data_provider = {
            "midnight": {
                "hours": 0,
                "mins": 0,
                "expected": 0
            },
            "acute at morning": {
                "hours": 8,
                "mins": 20,
                "expected": 130
            },
            "acute at evening": {
                "hours": 5,
                "mins": 40,
                "expected": 70
            },
            "obtuse at morning": {
                "hours": 10,
                "mins": 10,
                "expected": 65
            },
            "obtuse at evening": {
                "hours": 2,
                "mins": 50,
                "expected": 35
            }
        }

        self.invalid_arguments_provider = {
            "invalid hours": {
                "hours": -2,
                "mins": 55
            },
            "invalid mins": {
                "hours": 1,
                "mins": 61
            }
        }

    def test_angle(self):
        for key, data in self.positive_data_provider.items():
            calculator = WallclockAngleCalculator(data["hours"], data["mins"])
            self.assertEqual(data["expected"], calculator.get_angle())

    def test_invalid_arguments(self):
        for key, data in self.invalid_arguments_provider.items():
            self.assertRaises(ValueError, WallclockAngleCalculator, data["hours"], data["mins"])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WallclockAngleCalculatorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
