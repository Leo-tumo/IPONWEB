class HotelError(Exception):
    pass


class Hotel:
    room_types = ["Single", "Double", "Penthouse", "Presidential"]

    def __init__(self, city: str, stars=5):
        self.stars = stars
        rooms = {"Single": 50, "Double": 30, "Penthouse": 2, "Presidential": 1}
        self.city = city
        self.__rooms = rooms

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if type(value) != str:
            raise HotelError(f"Must be str not {type(value)}")
        if hasattr(self, 'city'):			# City can be set once!
            return
        self.__city = value

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value: tuple):
        if value[0] not in self.room_types:
            raise HotelError("No such room in our hotel")
        if value[1] != int or value[1] < 0:
            raise HotelError("wrong number of rooms")
        self.__rooms[value[0]] += value[1]

    def __repr__(self):
        ret = f'{self.stars * "*"} {self.city}:'
        for item in self.rooms:
            ret += f'\n{item} : {self.rooms[item]}'
        return ret

    def free_rooms_list(self, room_type: str):
        if not room_type.capitalize() in self.room_types:
            raise HotelError("Sorry got no such rooms")
        if self.rooms[room_type.capitalize()] == 0:
            print("Out of rooms, pls look for another option")
        return self.rooms[room_type.capitalize()]

    def reserve_rooms(self, rtype, count):
        if not rtype.capitalize() in self.room_types:
            raise HotelError("Sorry got no such rooms")
        if self.rooms[rtype.capitalize()] < count:
            print("No so many free rooms you're looking, pls have a look for another option")
        self.rooms[rtype.capitalize()] -= count


