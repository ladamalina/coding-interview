import sys
from classes.wallclock_angle_calculator import WallclockAngleCalculator


def main(argv):
    time = argv[0].split(":")
    hours = time[0]
    mins = time[1]
    calculator = WallclockAngleCalculator(hours, mins)
    print '%s %d' % ('Angle is', calculator.get_angle())

if __name__ == "__main__":
    main(sys.argv[1:])
