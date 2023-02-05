class PatientError(Exception):
    pass


class Patient:

    def __init__(self, name, surname, age, sex):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise PatientError(f'Must be str no {type(value)}')
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if type(value) != str:
            raise PatientError(f'Must be str no {type(value)}')
        self.__surname = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) != int:
            raise PatientError(f'Must be int no {type(value)}')
        elif value > 100 or value < 18:
            raise PatientError('Age should be 18..100')
        self.__age = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value: str):
        if type(value) != str:
            raise PatientError(f'Must be str no {type(value)}')
        if value.upper() != 'F' or value.upper() != 'M':
            raise PatientError("Unknown sex, choose between classic 'M' & 'F'")
        self.__sex = value

    def __repr__(self):
        return f'{self.name} {self.surname} - {self.sex}, {self.age} years old'

    def __ne__(self, other):
        if self.name == other.name and \
                self.surname == other.surname and \
                self.age == other.age and \
                self.sex == other.sex:
            return False
        return True

