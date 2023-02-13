class TimeError(Exception):
    def __init__(self, msg="time range is 00:00:00 -> 23:59:59"):
        self.msg = msg
        super().__init__(self.msg)


class Time:
    def __init__(self, hour: int, minute: int, second: int):
        if type(hour) != int:
            raise TimeError("must be int, not %s" % type(hour).__name__)
        elif type(minute) != int:
            raise TimeError("must be int, not %s" % type(minute).__name__)
        elif type(second) != int:
            raise TimeError("must be int, not %s" % type(second).__name__)

        if second > 59 or second < 0 or minute > 59 or minute < 0 or hour > 23 or hour < 0:
            raise TimeError()

        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

    def add_second(self, seconds: int):
        if type(seconds) != int:
            raise TimeError("Only integer allowed")
        self.__second += seconds
        while self.__second >= 60:
            self.__second -= 60
            self.add_minute(1)

    def add_minute(self, minutes: int):
        if type(minutes) != int:
            raise TimeError("Only integer allowed")
        self.__minute += minutes
        while self.__minute >= 60:
            self.__minute -= 60
            self.add_hour(1)

    def add_hour(self, hours: int):
        if type(hours) != int:
            raise TimeError("Only integer allowed")
        self.__hour += hours
        self.__hour = self.__hour % 24

    def __add__(self, other):
        t_second = self.__second + other.second
        t_minute = self.__minute + other.minute
        t_hour = self.__hour + other.hour
        while t_second > 60:
            t_minute += 1
            t_second -= 60
        while t_minute > 60:
            t_hour += 1
            t_minute -= 60
        t_hour %= 24

        return Time(t_hour, t_minute, t_second)

    __radd__ = __add__

    def __sub__(self, other):
        t_second = self.__second - other.second
        t_minute = self.__minute - other.minute
        t_hour = self.__hour - other.hour
        while t_second < 0:
            t_minute -= 1
            t_second += 60
        while t_minute < 0:
            t_hour -= 1
            t_minute += 60
        t_hour %= 24

        return Time(t_hour, t_minute, t_second)

    __rsub__ = __sub__

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        if 0 <= value <= 23:
            self.__hour = value
        else:
            raise TimeError("Invalid hour value. Hour should be between 0 and 23.")

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if 0 <= value <= 59:
            self.__minute = value
        else:
            raise TimeError("Invalid minute value. Minute should be between 0 and 59")

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        if 0 <= value <= 59:
            self.__second = value
        else:
            raise TimeError("Invalid second value. Minute should be between 0 and 59")

    def sub_second(self, seconds: int):
        if type(seconds) != int:
            raise TimeError("must be int, not %s" % type(seconds).__name__)
        self.__second -= seconds
        while self.__second < 0:
            self.__second += 60
            self.sub_minute(1)

    def sub_minute(self, minutes: int):
        if type(minutes) != int:
            raise TimeError("must be int, not %s" % type(minutes).__name__)
        self.__minute -= minutes
        while self.__minute < 0:
            self.__minute += 60
            self.sub_hour(1)

    def sub_hour(self, hours: int):
        if type(hours) != int:
            raise TimeError("must be int, not %s" % type(hours).__name__)
        self.__hour -= hours
        self.__hour = self.__hour % 24

    def __eq__(self, other):
        if self.second == other.second and \
                self.minute == other.minute and \
                self.hour == other.hour:
            return True
        return False

    def __call__(self, *args, **kwargs):
        if len(args):
            self.hour = args[0].hour
            self.minute = args[0].minute
            self.second = args[0].second
        return self.hour, self.minute, self.second

