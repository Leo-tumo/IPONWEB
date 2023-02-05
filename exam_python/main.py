from Passenger import Passenger
from Hotel import Hotel
import unittest


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.tourist = Passenger("Silia", "Adelaide")
        self.hotel = Hotel("Adelaide", stars=7)

    def test_book_hotel(self):
        self.hotel.reserve_rooms("single", 12)
        self.assertEqual(self.hotel.free_rooms_list("single"), 50 - 12)

    def test_book_tourist(self):
        self.tourist.rooms = ('double', 23)
        self.assertEqual(self.tourist.booked_rooms("double"), 23)


def book():
    tourist = Passenger("Silia", "Adelaide")
    hotel = Hotel("Adelaide", stars=7)

    hotel.reserve_rooms("Presidential", 1)
    hotel.reserve_rooms("single", 12)
    tourist.rooms = ("Single", 12)
    tourist.rooms = ("Presidential", 1)
    print(tourist, hotel)


if __name__ == '__main__':
    book()
    unittest.main()
