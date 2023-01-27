from Date import Date
from Time import Time


class DTError(Exception):
    def __init__(self, msg="Wrong arguments provided"):
        self.msg = msg
        super().__init__(self.msg)


class DateTime:
    def __init__(self, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0):
        self._date = Date(day, month, year)
        self._time = Time(hour, minute, second)

    def __repr__(self):
        return f'{self._date.__repr__()} {self._time.__repr__()}'

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, Date):
            self._date = value
        else:
            raise DTError('argument should be an instance of Date Class')

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if isinstance(value, Time):
            self._time = value
        else:
            raise DTError('argument should be an instance of Time Class')

    def add_year(self, years=1):
        self._date.add_year(years)

    def add_month(self, months=1):
        self._date.add_month(months)

    def add_day(self, days=1):
        self._date.add_day(days)

    def add_hour(self, hours=1):
        if type(hours) != int:
            raise DTError("must be int, not %s" % type(hours).__name__)
        tmp = self._time.hour + hours
        while tmp >= 24:
            tmp -= 24
            self._date.add_day(1)
        self._time.hour = tmp

    def add_minute(self, minutes=1):
        if type(minutes) != int:
            raise DTError("must be int, not %s" % type(minutes).__name__)
        sum_ = minutes + self._time.minute
        while sum_ > 60:
            self.add_hour(1)
            sum_ -= 60
        self._time.minute = sum_

    def add_second(self, seconds=1):
        if type(seconds) != int:
            raise DTError("must be int, not %s" % type(seconds).__name__)
        self._time.add_second(seconds)

    def sub_year(self, years=1):
        if type(years) != int:
            raise DTError("must be int, not %s" % type(years).__name__)
        self._date.sub_years(years)

    def sub_month(self, months=1):
        if type(months) != int:
            raise DTError("must be int, not %s" % type(months).__name__)
        self._date.sub_month(months)

    def sub_day(self, days=1):
        if type(days) != int:
            raise DTError("must be int, not %s" % type(days).__name__)
        self._date.sub_day(days)

    def sub_hour(self, hours=1):
        if type(hours) != int:
            raise DTError("must be int, not %s" % type(hours).__name__)
        tmp = self._time.hour - hours
        while tmp < 0:
            tmp -= 24
            self._date.sub_day(1)
        self._time.hour = tmp

    def sub_minute(self, minutes=1):
        if type(minutes) != int:
            raise DTError("must be int, not %s" % type(minutes).__name__)
        self._time.sub_minute(minutes)

    def sub_second(self, seconds=1):
        if type(seconds) != int:
            raise DTError("must be int, not %s" % type(seconds).__name__)
        self._time.sub_second(seconds)

    def __add__(self, other):
        if isinstance(other, DateTime):
            total_d = self._date + other._date
            total_t = self._time + other._time
            return DateTime(total_d.year, total_d.month, total_d.day,
                            total_t.hour, total_t.minute, total_t.second)
        else:
            raise DTError("Can only add Datetime.")

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, DateTime):
            total_d = self._date - other._date
            total_t = self._time - other._time
            return DateTime(total_d.year, total_d.month, total_d.day,
                            total_t.hour, total_t.minute, total_t.second)
        else:
            raise DTError("Can only add Datetime.")

    __rsub__ = __sub__

    def __eq__(self, other):
        if self._date.day == other.date.day and \
                self._date.month == other.date.month and \
                self._date.year == other.date.year and \
                self._time.second == other.time.second and \
                self._time.minute == other.time.minute and \
                self._time.hour == other.time.hour:
            return True
        else:
            return False
