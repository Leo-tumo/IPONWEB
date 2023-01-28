from Person import Person
from Date import Date
from City import City


class UniversityError(Exception):
    pass


class University:
    def __init__(self, name, founded_at, rector, city):
        self.name = name
        if not isinstance(founded_at, Date):
            raise UniversityError("must be Date class' instance")
        self.__founded_at = founded_at
        self.rector = rector
        if not isinstance(city, City):
            raise UniversityError("must be City class' instance")
        self.__city = city

    def __repr__(self):
        return f'University({self.name}, {self.founded_at}, {self.rector}, {self.city})'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise UniversityError("must be str, not %s" % type(value).__name__)
        self.__name = value

    @property
    def founded_at(self):
        return self.__founded_at

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, value):
        if not isinstance(value, Person):
            raise UniversityError("must be Person class' instance")
        self.__rector = value

    @property
    def city(self):
        return self.__city
