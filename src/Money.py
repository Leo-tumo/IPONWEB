from functools import total_ordering


class MoneyError(Exception):
    pass


@total_ordering
class Money:
    rate = {
        "EUR": 430,
        "AMD": 1,
        "RUB": 5.8,
        "USD": 400
    }

    def __init__(self, val, cur="AMD"):
        self.amount = val
        self.currency = cur

    def __repr__(self):
        return f"Money({self.amount}, {self.currency})"

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if type(value) != int and type(value) != float:
            raise MoneyError("must be int, not %s" % type(value).__name__)
        if value < 0:
            raise MoneyError('Sorry, no debts 💸💸💸')
        self.__amount = value

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if type(value) != str:
            raise MoneyError("must be str, not %s" % type(value).__name__)
        if not value.upper() in self.rate.keys():
            raise MoneyError("We don't accept 💩 currencies")
        self.__currency = value.upper()

    def conv_dram(self):
        return self.__amount / self.rate[self.__currency]

    def convert(self, new_currency):
        old = self.currency
        self.currency = new_currency
        self.amount = self.amount * (self.rate[new_currency] / self.rate[old])
        return self.amount, self.currency

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.__amount + other, self.__currency)
        return Money(round((self.conv_dram() + other.conv_dram()) * self.rate[self.__currency], 2), self.__currency)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.__amount * other, self.__currency)
        else:
            return Money((self.conv_dram() * other.conv_dram()) * self.rate[self.__currency], self.__currency)

    def __sub__(self, other):
        return Money(round((self.conv_dram() - other.conv_dram()) * self.rate[self.__currency], 2), self.__currency)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.__amount / other, self.__currency)
        else:
            return Money((self.conv_dram() / other.conv_dram()) * self.rate[self.__currency], self.__currency)

    def __eq__(self, other):
        return self.conv_dram() == other.conv_dram()

    def __lt__(self, other):
        return self.conv_dram() < other.conv_dram()

    def __str__(self):
        return str(round(self.__amount, 2)) + " " + self.__currency

    @classmethod
    def change_rate(cls, new_rate, new_cur):
        cls.rate[new_cur] = new_rate

    __radd__ = __add__
    __rmul__ = __mul__
