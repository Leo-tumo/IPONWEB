from DateTime import DateTime, Date, Time
from MyRange import MyRange, MyRangeError
from Money import Money
from Doctor import Doctor
from Person import Person
from City import City
from University import University
from Teacher import Teacher
import unittest

LOG = print


#############################################################################
############################## DATETIME #####################################
#############################################################################


class TestDateTime(unittest.TestCase):
    def setUp(self):
        self.date = Date(1, 1, 2022)
        self.time = Time(12, 0, 0)
        self.datetime = DateTime(2022, 1, 1, 12)

    def test_init(self):
        self.assertEqual(self.datetime.date, self.date)
        self.assertEqual(self.datetime.time, self.time)

    def test_repr(self):
        self.assertEqual(repr(self.datetime), str(self.datetime))

    def test_get_date(self):
        self.assertEqual(self.datetime.date, self.date)

    def test_set_date(self):
        new_date = Date(1, 1, 2022)
        self.datetime.date(new_date)
        self.assertEqual(self.datetime.date, new_date)

    def test_get_time(self):
        self.assertEqual(self.datetime.time, self.time)

    def test_set_time(self):
        new_time = Time(13, 0, 0)
        self.datetime.time(new_time)
        self.assertEqual(self.datetime.time, new_time)

    def test_add_year(self):
        self.datetime.add_year()
        self.assertEqual(self.datetime.date.year, 2023)

    def test_add_month(self):
        self.datetime.add_month()
        self.assertEqual(self.datetime.date.month, 2)

    def test_add_day(self):
        self.datetime.add_day()
        self.assertEqual(self.datetime.date.day, 2)

    def test_add_hour(self):
        self.datetime.add_hour()
        self.assertEqual(self.datetime.time.hour, 13)

    def test_add_minute(self):
        self.datetime.add_minute()
        self.assertEqual(self.datetime.time.minute, 1)

    def test_add_second(self):
        self.datetime.add_second()
        self.assertEqual(self.datetime.time.second, 1)

    def test_sub_year(self):
        self.datetime.sub_year()
        self.assertEqual(self.datetime.date.year, 2021)

    def test_sub_month(self):
        self.datetime.sub_month()
        self.assertEqual(self.datetime.date.month, 12)

    def test_sub_day(self):
        self.datetime.sub_day()
        self.assertEqual(self.datetime.date.day, 31)

    def test_sub_hour(self):
        self.datetime.sub_hour()
        self.assertEqual(self.datetime.time(), (11, 0, 0))
        self.datetime.sub_hour()
        self.assertEqual(self.datetime.time(), (10, 0, 0))
        self.datetime.sub_hour(5)
        self.assertEqual(self.datetime.time(), (5, 0, 0))
        self.datetime.sub_hour(-3)
        self.assertEqual(self.datetime.time(), (8, 0, 0))


#############################################################################
############################## MYRANGE ######################################
#############################################################################

class TestMyRange(unittest.TestCase):
    def test_init(self):
        r = MyRange(1, 10)
        self.assertEqual(r.current, 1)
        self.assertEqual(r.end, 10)
        self.assertEqual(r.step, 1)

        r = MyRange(1, 10, 2)
        self.assertEqual(r.current, 1)
        self.assertEqual(r.end, 10)
        self.assertEqual(r.step, 2)

    def test_repr(self):
        r = MyRange(1, 10)
        self.assertEqual(repr(r), 'MyRange(1, 10, 1)')

    def test_iter(self):
        r = MyRange(1, 10)
        self.assertEqual(list(r), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_next(self):
        r = MyRange(1, 10)
        self.assertEqual(next(r), 1)
        self.assertEqual(next(r), 2)
        self.assertEqual(next(r), 3)

    def test_len(self):
        r = MyRange(1, 10)
        self.assertEqual(len(r), 9)

    def test_getitem(self):
        r = MyRange(1, 10)
        self.assertEqual(r[0], 1)
        self.assertEqual(r[1], 2)
        self.assertEqual(r[8], 9)

    def test_getitem_indexerror(self):
        r = MyRange(1, 10)
        with self.assertRaises(MyRangeError):
            r[9]

    def test_reversed(self):
        r = MyRange(1, 10)
        self.assertEqual(list(reversed(r)), [9, 8, 7, 6, 5, 4, 3, 2, 1])


#############################################################################
################################ MONEY ######################################
#############################################################################


class TestMoney(unittest.TestCase):
    def setUp(self):
        self.money = Money(10.5, "USD")

    def test_init(self):
        self.assertEqual(self.money.amount, 10.5)
        self.assertEqual(self.money.currency, "USD")

    def test_repr(self):
        self.assertEqual(repr(self.money), "Money(10.5, USD)")

    def test_get_amount(self):
        self.assertEqual(self.money.amount, 10.5)

    def test_set_amount(self):
        self.money.amount = 20
        self.assertEqual(self.money.amount, 20)

    def test_get_currency(self):
        self.assertEqual(self.money.currency, "USD")

    def test_set_currency(self):
        self.money.currency = "EUR"
        self.assertEqual(self.money.currency, "EUR")

    def test_conversion(self):
        self.money += 29.5
        self.assertEqual(self.money.convert("EUR"), (43, "EUR"))

    def test_add(self):
        other_money = Money(5, "USD")
        result = self.money + other_money
        self.assertEqual(result, Money(15.5, "USD"))

    def test_sub(self):
        other_money = Money(5, "USD")
        result = self.money - other_money
        self.assertEqual(result, Money(5.5, "USD"))

    def test_truediv(self):
        result = self.money / 2
        self.assertEqual(result, Money(5.25, "USD"))

    def test_eq(self):
        other_money = Money(10.5, "USD")
        self.assertTrue(self.money == other_money)

    def test_ne(self):
        other_money = Money(5, "USD")
        self.assertTrue(self.money != other_money)

    def test_lt(self):
        other_money = Money(5, "USD")
        self.assertTrue(other_money < self.money)

    def test_gt(self):
        other_money = Money(5, "USD")
        self.assertTrue(self.money > other_money)

    def test_le(self):
        other_money = Money(10.5, "USD")
        self.assertTrue(other_money <= self.money)

    def test_ge(self):
        other_money = Money(10.5, "USD")
        self.assertTrue(self.money >= other_money)


#############################################################################
################################ DOCTOR #####################################
#############################################################################

import unittest


class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor("John", "Doe", "Male", 40, "California", "Surgery", "Surgeon", "Smith", 100000)

    def test_init(self):
        self.assertEqual(self.doctor.name, "John")
        self.assertEqual(self.doctor.surname, "Doe")
        self.assertEqual(self.doctor.department, "Surgery")
        self.assertEqual(self.doctor.profession, "Surgeon")
        self.assertEqual(self.doctor.patronymic, "Smith")
        self.assertEqual(self.doctor.salary, 100000)

    def test_repr(self):
        self.assertEqual(repr(self.doctor), "Doctor(John, Doe, Male, 40, California, Surgery, Surgeon, Smith, 100000)")

    def test_set_department(self):
        self.doctor.department = "Orthopedics"
        self.assertEqual(self.doctor.department, "Orthopedics")

    def test_get_department(self):
        self.assertEqual(self.doctor.department, "Surgery")

    def test_set_profession(self):
        self.doctor.profession = "Orthopedic Surgeon"
        self.assertEqual(self.doctor.profession, "Orthopedic Surgeon")

    def test_get_profession(self):
        self.assertEqual(self.doctor.profession, "Surgeon")

    def test_get_patronymic(self):
        self.assertEqual(self.doctor.patronymic, "Smith")

    def test_set_salary(self):
        self.doctor.salary = 120000
        self.assertEqual(self.doctor.salary, 120000)

    def test_get_salary(self):
        self.assertEqual(self.doctor.salary, 100000)


#############################################################################
################################# CITY ######################################
#############################################################################


class CityTests(unittest.TestCase):
    def test_init(self):
        mayor = Person("Jane", "Doe", "female", 49, "Charbax")
        city = City("New York", mayor, 8000000, "English")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.mayor, mayor)
        self.assertEqual(city.population, 8000000)
        self.assertEqual(city.language, "English")

    def test_repr(self):
        mayor = Person("Jane", "Doe", "female", 49, "Charbax")
        city = City("New York", mayor, 8000000, "English")
        self.assertEqual(repr(city), "City(New York, Person(Jane, Doe, female, 49, Charbax), 8000000, English)")

    def test_get_and_set_name(self):
        mayor = Person("Jane", "Doe", "female", 12, "Home")
        city = City("New York", mayor, 8000000, "English")
        self.assertEqual(city.name, "New York")
        city.name = "Los Angeles"
        self.assertEqual(city.name, "Los Angeles")

    def test_get_and_set_mayor(self):
        mayor = Person("Jane", "Doe", "female", 44, "AA")
        city = City("New York", mayor, 8000000, "English")
        self.assertEqual(city.mayor, mayor)
        mayor2 = Person("John", "Doe", "male", 44, "AA")
        city.mayor = mayor2
        self.assertEqual(city.mayor, mayor2)

    def test_get_and_set_population(self):
        mayor = Person("Jane", "Doe", "female", 20, "Masiv")
        city = City("New York", mayor, 8000000, "English")
        self.assertEqual(city.population, 8000000)
        city.population = 9000000
        self.assertEqual(city.population, 9000000)

    def test_get_and_set_language(self):
        mayor = Person("Jane", "Doe", "female", 49, "Charbax")
        city = City("New York", mayor, 8000000, "English")
        self.assertEqual(city.language, "English")
        city.language = "Greek"
        self.assertEqual(city.language, "Greek")


#############################################################################
############################## UNIVERSITY ###################################
#############################################################################

class TestUniversity(unittest.TestCase):

    def setUp(self):
        self.mayor = Person('S', 'S', 'MALE', '20', 'S')
        self.city = City("New York", self.mayor, 900, 'HY')
        self.rector = Person("John", "Doe", "MALE", '29', "home")
        self.university = University("NYU", Date(18, 4, 1831), self.rector, self.city)

    def test_init(self):
        self.assertEqual(self.university.name, "NYU")
        self.assertEqual(self.university.founded_at, Date(18, 4, 1831))
        self.assertEqual(self.university.rector, self.rector)
        self.assertEqual(self.university.city, self.city)

    def test_repr(self):
        self.assertEqual(repr(self.university), "University(NYU, 18-04-1831, Person(John, Doe, MALE, 29, home), "
                                                "City(New York, Person(S, S, MALE, 20, S), 900, HY))")

    def test_get_name(self):
        self.assertEqual(self.university.name, "NYU")

    def test_set_name(self):
        self.university.name = "Columbia University"
        self.assertEqual(self.university.name, "Columbia University")

    def test_get_founded_at(self):
        self.assertEqual(self.university.founded_at, Date(18, 4, 1831))

    def test_set_rector(self):
        new_rector = Person("Jane", "Smith", "Female", 18, 'unknown')
        self.university.rector = new_rector
        self.assertEqual(self.university.rector, new_rector)

    def test_get_rector(self):
        self.assertEqual(self.university.rector, self.rector)


#############################################################################
############################### TEACHER #####################################
#############################################################################

class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.city = City("New York")
        self.university = University("NYU", Date(18, 4, 1831), Person("Leo", "Tm"), self.city)
        self.teacher = Teacher("Jasmine", "Kaminska", self.university, "Engineering", 5, Date(1, 9, 2016),
                               "Computer Science", 75000)

    def test_init(self):
        self.assertEqual(self.teacher.name, "Jasmine")
        self.assertEqual(self.teacher.surname, "Kaminska")
        self.assertEqual(self.teacher.university, self.university)
        self.assertEqual(self.teacher.faculty, "Engineering")
        self.assertEqual(self.teacher.experience, 5)
        self.assertEqual(self.teacher.start_work_at, Date(1, 9, 2016))
        self.assertEqual(self.teacher.subject, "Computer Science")
        self.assertEqual(self.teacher.salary, 75000)

    def test_repr(self):
        self.assertEqual(repr(self.teacher), f"Teacher(name='Jasmine', last name='Kaminska, "
                                             f"university=University(NYU, 18-04-1831, Person(Leo, Tm, MALE, "
                                             f"23, unknown), City(New York, God, 24000000, English)), "
                                             f"faculty='Engineering', experience='5', start_work_at='01-09-2016', "
                                             f"subject='Computer Science', salary='75000')")

    def test_set_experience(self):
        self.teacher.experience = 10
        self.assertEqual(self.teacher.experience, 10)

    def test_get_experience(self):
        self.assertEqual(self.teacher.experience, 5)

    def test_get_start_work_at(self):
        self.assertEqual(self.teacher.start_work_at, Date(1, 9, 2016))

    def test_get_subject(self):
        self.assertEqual(self.teacher.subject, "Computer Science")

    def test_get_faculty(self):
        self.assertEqual(self.teacher.faculty, "Engineering")

    def test_set_faculty(self):
        self.teacher.faculty = "Science"
        self.assertEqual(self.teacher.faculty, "Science")

    def test_get_salary(self):
        self.assertEqual(self.teacher.salary, 75000)

    def test_set_salary(self):
        self.teacher.salary = 80000
        self.assertEqual(self.teacher.salary, 80000)


if __name__ == '__main__':
    unittest.main()
