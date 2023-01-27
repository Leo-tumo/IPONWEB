from Person import Person


class DoctorError(Exception):
    pass


class Doctor(Person):
    def __init__(self, first_name, last_name, gender, age, address, department, profession, patronymic, salary):
        super().__init__(first_name, last_name, gender, age, address)
        self.department = department
        self.profession = profession
        if type(patronymic) != str:
            raise DoctorError("must be str, not %s" % type(patronymic).__name__)
        self._patronymic = patronymic
        self.salary = salary

    def __repr__(self):
        return f"Doctor({self.name}, {self.surname}, {self.gender}, {self.age}, {self.address}, {self._department}, " \
               f"{self._profession}, {self.patronymic}, {self._salary})"

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department: str):
        if type(department) != str:
            raise DoctorError("must be str, not %s" % type(department).__name__)
        self._department = department

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, profession: str):
        if type(profession) != str:
            raise DoctorError("must be str, not %s" % type(profession).__name__)
        self._profession = profession

    @property
    def patronymic(self):
        return self._patronymic

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary: int):
        if type(salary) != int:
            raise DoctorError("must be str, not %s" % type(salary).__name__)
        self._salary = salary
