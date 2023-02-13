#!/usr/bin/python3
# ************************************************************************ #
#                                                                          #
#              homework2.py                                                #
#              Created: 2023/01/19 14:36:27 by leo                         #
#              Made by: leo <leonidas.xaralambos@gmail.com>                #
#                                                                          #
# ************************************************************************ #

# ! Task 1
# Write a Python program to create a new dictionary by extracting the mentioned keys
# from the below dictionary.

def extract_keys(d: dict, keys: list) -> dict:
    ans = {k: d[k] for k in keys}
    return ans


# ! dTask 2
# Get the key of a minimum value from the following dictionary.
# Example:

def min_value(d: dict):
    if not d:
        return
    ans = next(iter(d.items()))
    for item in d.items():
        if item[1] < ans[1]:
            ans = item
    return ans[0]


# ! Task 3
# Write a Python program to copy the contents of a file to another file

def cp_r(src: str, dst: str):
    with open(src, 'r') as source, open(dst, 'w') as dest:
        cp = source.read()
        dest.write(cp)


# ! Task 4
# Write a Python program to count the frequency of words in a file
def word_frequency(src: str, rev_sort=False) -> dict:
    with open(src, 'r') as source:
        ret = {}
        text = source.read()
        p_marks = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        text = text.translate(text.maketrans('', '', p_marks))
        words = text.split()
        for word in words:
            if word in ret.keys():
                ret[word] += 1
            else:
                ret[word] = 1
        sorted_ret = dict(sorted(ret.items(), key=lambda item: item[1], reverse=True))
        return sorted_ret if rev_sort else ret


# ! Task 5
# Write a Python program to read last n lines of a file

def tail(src: str, n: int):
    try:
        assert n > 0
        with open(src, 'r') as file:
            lines = file.readlines()
            return lines[-n:]
    except (FileNotFoundError, PermissionError, OSError):
        raise FileNotFoundError('Check the filename and/or file\'s rights')
    except (AssertionError, TypeError):
        raise ValueError('n must be an unsigned integer')


# ! Task 6
# Finish class work, which you started in class.
# Class
# Write class Company
# Data members: company_name, founded_at, employees_count
# Data methods: __init__, __repr__

# Write class Job.
# Data members: company(Company type), salary, experience_year, position.
# Data methods: __init__, __repr__, change_salary, change_experience_year,
# change_postition.
# Write class Person.
# Data members: name, surname, gender(Male or Female), age, address, friends(list
# of Person type), job(list of Job type)
# Data methods: __init__, __repr__, add_friend, remove_friend, add_job,
# remove_job, display_job
# Some logics
# When Person add job Company employees count should increase by 1.
# When Person quit the job Company employees count should decrease by 1.
# You can come up with other logics.

# ======================================================== #
# ===================== class Company ==================== #
# ======================================================== #

class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.company_name = company_name
        self.founded_at = founded_at
        self.employees_count = employees_count

    def __repr__(self):
        return f'{self.company_name} company is founded at {self.founded_at} and has {self.employees_count} employees'


# ======================================================== #
# ======================= class Job ====================== #
# ======================================================== #

class Job:
    def __init__(self, company: Company, salary, experience_year, position):
        self.company = company
        self.salary = salary
        self.experience_year = experience_year
        self.position = position

    def __repr__(self):
        return f'Working at {self.company} company as {self.position} with {self.salary} salary and have' \
               f' {self.experience_year} years of experience'

    def change_salary(self, new_salary):
        self.salary = new_salary

    def change_experience_year(self, new_experience_year):
        self.experience_year = new_experience_year

    def change_position(self, new_position):
        self.position = new_position


# ======================================================== #
# ===================== class Person ===================== #
# ======================================================== #

class Person:
    def __init__(self, name, surname, gender, age, address):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.address = address
        self.friends: list[Person] = []
        self.jobs: list[Job] = []

    def __repr__(self):
        return f'first name - {self.name}\nlast name - {self.surname}\nsex - {self.gender}\nage - ' \
               f'{self.age}\naddress - {self.address}'

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


# Task 7
# Write this classes.
# Class - Date
# Data members
# Year - integer
# Month - integer
# Day - integer
# Data methods
# Constructor - 3 params for init year, month, day
# __repr__ for print Date objet like - day.mount.year
# Ex. 15.10.1950
# add_day - add day to given Date object
# Add_mount - add mount to given Date object
# Add_year - add year to given Date object
# __is_leap_year - check year is leap or not

# Class - Time
# Data members
# Hour - int
# Minute - int
# Second - int
# Data methods

# __init__ constructor
# __repr__
# 3. add_second(s)
# 2. add_minute(m)
# 1.add_hour(h)
# sum 2 Time objects (take into account that, when add seconds, minutes can be
# changed, when add minutes hour can be changed, when add hours, can get value &gt;
# 24, that case should take hour%24 as hour)
# Time() and Date() classes are very similar, but Time() is easy, because, in
# Date() we have month with different days, but Time() all are standard, 1min =
# 60sec, 1hour = 60minute=3600second


# ======================================================== #
# ====================== class Date ====================== #
# ======================================================== #

class Date:
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day: int, month: int, year: int):
        if month > 12 or month < 1:
            raise ValueError(f"wrong month {month}, month can be between 1 and 12")
        if day > self.month_days[month] or day < 1:
            if not (self.is_leap_year() and month == 2 and day == 29):
                raise ValueError(f"Month no '{month}' doesn't have that many days")
        if year < 1:
            raise ValueError(f"Year must be a positive integer only")
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __days_in_month(self):
        if self.is_leap_year() and self.month == 2:
            return 29
        else:
            return self.month_days[self.month]

    def add_day(self, days: int):
        self.day += days
        while self.day > self.__days_in_month():
            self.day -= self.__days_in_month()
            self.add_month(1)

    def add_month(self, months: int):
        self.month += months
        while self.month > 12:
            self.month -= 12
            self.add_year(1)
        if self.day > self.__days_in_month():
            self.day -= self.__days_in_month()
            self.month += 1

    def add_year(self, years: int):
        self.year += years

    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False



# ======================================================== #
# ====================== Class Time ====================== #
# ======================================================== #

class Time:
    def __init__(self, hour: int, minute: int, second: int):
        if second > 59 or second < 0 or minute > 59 or minute < 0 or hour > 23 or hour < 0:
            raise ValueError("time range is 0:0:0 -> 23:59:59")

        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        mn = ''
        sc = ''
        if self.minute < 10:
            mn = 0
        if self.second < 10:
            sc = 0
        return f"{self.hour}:{mn}{self.minute}:{sc}{self.second}"

    def add_second(self, seconds: int):
        self.second += seconds
        while self.second >= 60:
            self.second -= 60
            self.add_minute(1)

    def add_minute(self, minutes: int):
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.add_hour(1)

    def add_hour(self, hours: int):
        self.hour += hours
        self.hour = self.hour % 24

    def __add__(self, other):
        hour = self.hour + other.__hour
        minute = self.minute + other.__minute
        second = self.second + other.__second
        return Time(hour, minute, second)
