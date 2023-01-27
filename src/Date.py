class DateError(Exception):
    def __init__(self, msg="date range is 01-01-0001 -> 31:12:9999"):
        self.msg = msg
        super().__init__(self.msg)


class Date:
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day: int, month: int, year: int):
        if type(day) != int:
            raise DateError("must be int, not %s" % type(day).__name__)
        if type(month) != int:
            raise DateError("must be int, not %s" % type(month).__name__)
        if type(year) != int:
            raise DateError("must be int, not %s" % type(year).__name__)
        if 1 > year or year > 9999:
            raise DateError("Year must be a positive integer only")
        self.__year = year
        if month > 12 or month < 1:
            raise DateError(f"wrong month {month}, month can be between 1 and 12")
        self.__month = month
        if day > self.month_days[month] or day < 1:
            if month == 2 and day == 29:
                if not self.is_leap_year():
                    raise DateError(f"Month no '{month}' doesn't have that many days")
            else:
                raise DateError(f"Month no '{month}' doesn't have that many days")
        self.__day = day

    def __repr__(self):
        return f"{self.day:02}-{self.__month:02}-{self.__year:04}"

    def __days_in_month(self):
        if self.is_leap_year() and self.__month == 2:
            return 29
        else:
            return self.month_days[self.__month]

    def add_day(self, days: int):
        self.day += days
        while self.day > self.__days_in_month():
            self.day -= self.__days_in_month()
            self.add_month(1)

    def add_month(self, months: int):
        self.__month += months
        while self.__month > 12:
            self.__month -= 12
            self.add_year(1)
        if self.day > self.__days_in_month():
            self.day -= self.__days_in_month()
            self.__month += 1

    def add_year(self, years: int):
        self.__year += years

    def is_leap_year(self):
        if self.__year % 4 == 0:
            if self.__year % 100 == 0:
                if self.__year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def sub_years(self, value):
        if value >= self.__year:
            DateError("Year must be a positive integer")
        self.__year -= value
        if (not self.is_leap_year()) and self.__month == 2 and self.day == 29:
            self.__day = 28

    def sub_month(self, months=1):
        self.__month -= months
        while self.__month < 1:
            self.__month += 12
            self.sub_years(1)
        if self.__day > self.__days_in_month():
            self.__day -= self.__days_in_month()
            self.__month += 1

    def sub_day(self, days=1):
        self.__day -= days
        while self.__day < self.__days_in_month():
            self.__day += self.__days_in_month()
            self.sub_month(1)

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if type(value) != int:
            raise DateError("must be int, not %s" % type(value).__name__)
        if 0 < value < 13:
            self.__month = value
        else:
            raise DateError("month must be 1..12")
        if self.day > self.__days_in_month():
            self.day -= self.__days_in_month()
            self.add_month(1)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if type(value) != int:
            raise DateError("must be int, not %s" % type(value).__name__)
        if 0 < value <= self.__days_in_month():
            self.__day = value
        else:
            raise DateError(f"This month has {self.__days_in_month()} days")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if type(value) != int:
            raise DateError("must be int, not %s" % type(value).__name__)
        if 0 < value < 10000:
            self.__year = value
        else:
            raise DateError('Year must be 1..9999')

    def __add__(self, other):
        total_d = self.__day + other.day
        total_m = self.__month + other.month
        total_y = self.__year + other.year
        while total_d > self.month_days[total_m % 12]:
            total_d -= self.month_days[total_m % 12]
            total_m += 1
        while total_m > 12:
            total_y += 1
            total_m -= 12
        if total_y > 9999:
            raise DateError('❌❌❌❌❌❌')

        return Date(total_d, total_m, total_y)

    def __sub__(self, other):
        total_d = self.__day - other.day
        total_m = self.__month - other.month
        total_y = self.__year - other.year
        while total_d < 1:
            total_d += self.month_days[total_m]
            total_m -= 1
        while total_m < 1:
            total_y -= 1
            total_m += 12
        if total_y < 1:
            raise DateError('❌❌❌❌❌❌')

        return Date(total_d, total_m, total_y)

    __rsub__ = __sub__
    __radd__ = __add__

    def __eq__(self, other):
        if self.day == other.day and \
                self.month == other.month and \
                self.year == other.year:
            return True
        return False

    def __call__(self, *args, **kwargs):
        if len(args) == 1:
            self.day = args[0].day
            self.month = args[0].month
            self.year = args[0].year
        return self.year, self.month, self.day
