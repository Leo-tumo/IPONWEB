from Patient import Patient
from datetime import timedelta, datetime


class DoctorError(Exception):
    pass


class Doctor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.schedule = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise DoctorError(f'Must be str no {type(value)}')
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if type(value) != str:
            raise DoctorError(f'Must be str no {type(value)}')
        self.__surname = value

    def __repr__(self):
        ret = f'Doctor {self.name} {self.surname} schedule'
        for item in self.schedule:
            ret += f'\n{item} : {self.schedule[item]}'
        return ret

    def register_patient(self, patient: Patient, time: datetime):
        if self.is_registered(patient):
            print("Patient is already registered")
        if self.is_free(time):
            self.schedule[time] = patient

    def is_free(self, time: datetime):
        if time.weekday() == 5 or time.weekday() == 6:  # weekend
            print('Not working on weekends')
            return False
        if time.hour < 9 or time.hour > 17:
            print('Workday starts from 9:00 - 17:59')
            return False
        if 13 < time.hour > 14:  # pereriv
            return False
        time = self._round_minute(time)
        if time in self.schedule.keys():
            return False
        return True

    def is_registered(self, patient: Patient):
        if patient in self.schedule.values():
            return True
        return False

    @staticmethod
    def _round_minute(dt):
        if dt.minute != 0 or dt.minute != 30:
            print("Please book a round time! ex. 12:00, 12:30 etc.")
            if 0 < dt.minute < 15:
                dt -= timedelta(minutes=dt.minute)
            elif 45 < dt.minute < 59:
                dt += timedelta(60 - dt.minute)
            else:
                dt += timedelta(minutes=(30-dt.minute))
        return dt


