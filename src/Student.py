from Person import Person
from University import University
from Date import Date


class StudentError(Exception):
    pass


class Student(Person):
    def __init__(self, name, surname, university, faculty, course, started_at, age=20):
        super().__init__(name, surname, age)
        self.university = university
        self.faculty = faculty
        self.course = course
        if not isinstance(started_at, Date):
            raise StudentError("must be Date, not %s" % type(faculty).__name__)
        self.__started_at = started_at

    def __repr__(self):
        return f"Student({self.name}, {self.surname}, {self.university}, {self.faculty}, {self.course}," \
               f" {self.started_at})"

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, university):
        if not isinstance(university, University):
            raise StudentError("must be University, not %s" % type(university).__name__)
        self.__university = university

    @property
    def faculty(self):
        return self.faculty

    @faculty.setter
    def faculty(self, faculty):
        if type(faculty) != str:
            raise StudentError("must be str, not %s" % type(faculty).__name__)
        self.faculty = faculty

    @property
    def course(self):
        return self.course

    @course.setter
    def course(self, course):
        if type(course) != int and 0 < course < 6:
            raise StudentError("must be int in range 1..5, not %s" % type(course).__name__)
        self.course = course

    @property
    def started_at(self):
        return self.__started_at
