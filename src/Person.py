class PersonError(Exception):
    pass


class Person:

    def __init__(self, name, surname, gender='MALE', age=23, address='unknown'):
        self._name = name
        self._surname = surname
        self._gender = gender
        self._age = age
        self._address = address
        self.friends: list[Person] = []
        self.jobs: list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise PersonError("must be str, not %s" % type(value).__name__)
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if type(value) != int:
            raise PersonError("must be int, not %s" % type(value).__name__)
        if value < 0 or value > 130:
            raise PersonError('age range is 0..130')
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if type(value) != str:
            raise PersonError("must be str, not %s" % type(value).__name__)
        if value.upper() not in ['MALE', 'FEMALE']:
            raise PersonError('Choose between MALE & FEMALE')
        self._name = value.upper()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if type(value) != str:
            raise PersonError("must be str, not %s" % type(value).__name__)
        self._surname = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if type(value) != str:
            raise PersonError("must be str, not %s" % type(value).__name__)
        self._address = value

    def __repr__(self):
        return f'Person({self._name}, {self._surname}, {self._gender}, {self._age}, {self._address})'

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)

    def add_job(self, job):
        self.jobs.append(job)
        job.company.employees_count += 1

    def remove_job(self, job):
        self.jobs.remove(job)
        job.company.employees_count -= 1

    def display_job(self):
        for job in self.jobs:
            print(job)
