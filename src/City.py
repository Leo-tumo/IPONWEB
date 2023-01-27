from Person import Person


class CityError(Exception):
    pass


class City:
    def __init__(self, name, mayor, population, language):
        self._name = name
        self._mayor = mayor
        self._population = population
        self._language = language

    def __repr__(self):
        return f"City({self._name}, {self._mayor}, {self._population}, {self._language})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise CityError("must be str, not %s" % type(value).__name__)
        self._name = value

    @property
    def mayor(self):
        return self._mayor

    @mayor.setter
    def mayor(self, value):
        if not isinstance(value, Person):
            raise CityError("must be Person, not %s" % type(value).__name__)
        self._mayor = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        if type(value) != int:
            raise CityError("must be int, not %s" % type(value).__name__)
        if value < 1:
            raise CityError("It's not even a village")
        self._population = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if type(value) != str:
            raise CityError("must be str, not %s" % type(value).__name__)
        self._language = value
