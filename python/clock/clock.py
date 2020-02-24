class Clock(object):
    def __init__(self, hours, minutes):
        self.set_hour(hours)
        self.set_minutes(minutes)

    def set_hour(self, hours):
        hours = hours % 24
        self.hours = hours

    def set_minutes(self, minutes):
        while minutes > 60:
            self.set_hour(self.hours + 1)
            minutes -= 60

        while minutes < 0:
            self.set_hour(self.hours - 1)
            minutes += 60

        self.minutes = minutes

    def __repr__(self):
        return str(self.hours).zfill(2) + ':' + str(self.minutes).zfill(2)

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, minutes):
        return self.set_minutes(self.minutes + minutes)

    def __sub__(self, minutes):
        return self.set_minutes(self.minutes - minutes)


# This Method doesn't work
"""class Clock(object):
    import time

    def __init__(self, hour, minute):
        if (hour not in range(0, 24)) and (minute not in range(0, 61)):
            raise Exception('Incorrect Format')
        else:
            self.clock = self.time.strptime(f'{hour}:{minute}', '%H:%M')

    def __repr__(self):
        return self.time.strftime('%H:%M', self.clock)

    def __eq__(self, other):
        return self.clock == other

    def __add__(self, minutes):
        self._seconds = minutes * 60
        self._new_time = self.time.ctime((self.time.mktime(self.clock) + self._seconds))
        self._tmp_clock = self.time.strptime(self._new_time, '%a %b %d %H:%M:%S %Y')
        self.clock = self.time.strftime('%H:%M', self._tmp_clock)
        return self.clock

    def __sub__(self, minutes):
        self._seconds = minutes * 60
        self._new_time = self.time.ctime((self.time.mktime(self.clock) - self._seconds))
        self._tmp_clock = self.time.strptime(self._new_time, '%a %b %d %H:%M:%S %Y')
        self.clock = self.time.strftime('%H:%M', self._tmp_clock)
        return self.clock
"""
