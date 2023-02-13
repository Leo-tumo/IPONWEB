from Person import Person
from Date import Date
from University import University


class TeacherError(Exception):
    pass


class Teacher(Person):
    def __init__(self, name: str, surname: str, university: University, faculty: str, experience: int
                 , start_work_at: Date, subject: str, salary: int, gender='FEMALE', age=50, address='unknown'):
        super().__init__(name, surname, gender, age, address)
        if not isinstance(university, University):
            raise TeacherError("must be University, not %s" % type(university).__name__)
        self.university = university
        self.faculty = faculty

        self.experience = experience
        if not isinstance(start_work_at, Date):
            raise TeacherError(f"must be Date, not {type(start_work_at).__name__}")
        self.__start_work_at = start_work_at
        if type(subject) != str:
            raise TeacherError("must be str, not %s" % type(subject).__name__)
        self.__subject = subject
        self.salary = salary

    def __repr__(self):
        return f"Teacher(name='{self.name}', last name='{self.surname}, university={self.university}, " \
               f"faculty='{self.__faculty}', experience='{self.experience}', start_work_at='{self.start_work_at}', " \
               f"subject='{self.subject}', salary='{self.salary}')"

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if type(value) != int:
            raise TeacherError(f"must be int, not {type(value).__name__}")
        self.__experience = value

    @property
    def start_work_at(self):
        return self.__start_work_at

    @property
    def subject(self):
        return self.__subject

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        if type(faculty) != str:
            raise TeacherError("must be str, not %s" % type(faculty).__name__)
        self.__faculty = faculty

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if type(salary) != int:
            raise TeacherError("must be int, not %s" % type(salary).__name__)
        self.__salary = salary
