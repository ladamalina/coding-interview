class WallclockAngleCalculator:
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        val_hours = int(hours)
        if val_hours < 0 or val_hours > 12:
            raise ValueError("Invalid argument 'hours': " + str(val_hours))
        else:
            self.__hours = val_hours

    @property
    def mins(self):
        return self.__mins

    @mins.setter
    def mins(self, mins):
        val_mins = int(mins)
        if val_mins < 0 or val_mins > 59:
            raise ValueError("Invalid argument 'mins': " + str(val_mins))
        else:
            self.__mins = val_mins

    def _get_mins_angle(self):
        return self.mins * 360 / 60

    def _get_hours_angle(self):
        one_hour_angle = 360 / 12
        hours_angle = self.hours * one_hour_angle + one_hour_angle * self.mins / 60

        return hours_angle

    def get_angle(self):
        mins_angle = self._get_mins_angle()
        hours_angle = self._get_hours_angle()
        angle = max(mins_angle, hours_angle) - min(mins_angle, hours_angle)
        if angle > 180:
            angle -= 180

        return angle
