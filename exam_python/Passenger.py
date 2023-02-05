class PassengerError(Exception):
    pass


class Passenger:
    room_types = ["Single", "Double", "Penthouse", "Presidential"]

    def __init__(self, name: str, city: str):
        rooms = {k: 0 for k in self.room_types}
        self.name = name
        self.city = city
        self.__rooms = rooms

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise PassengerError(f"Must be str not {type(value)}")
        self.__name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if type(value) != str:
            raise PassengerError(f"Must be str not {type(value)}")
        self.__city = value

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value: tuple):
        if value[0].capitalize() not in self.room_types:
            raise PassengerError("No such room in our hotel")
        if not isinstance(value[1], int) or value[1] < 0:
            raise PassengerError("wrong number of rooms")
        self.__rooms[value[0].capitalize()] += value[1]

    def booked_rooms(self, rtype: str):
        try:
            return self.rooms[rtype.capitalize()]
        except Exception as e:
            raise e

    def __repr__(self):
        ret = f'{self.name} - {self.city} :'
        for item in self.rooms:
            ret += f'\n{item} : {self.rooms[item]}'
        return ret
