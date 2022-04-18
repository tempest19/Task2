import random
import string


class FlightClass:
    passengers = []

    def __init__(self, source, destination, duration, seats):
        self.source = source
        self.destination = destination
        self.duration = duration
        self.seats = seats

    @property
    def generate_id(self):
        self.id = string.ascii_uppercase
        return ( ''.join(random.choice(self.id) for i in range (5)))


    def open_seats(self):

        if len(FlightClass.passengers) >= self.seats:
            return "Not available"
        else:
            return "Available"

    def add_passenger(self, name):

        if name not in FlightClass.passengers:
            FlightClass.passengers.append(name)
            print ("Added ", name, "to flight ", self.generate_id)

    def list_passengers(self):

        for number, letter in enumerate(FlightClass.passengers, start = 1):
            print (number, letter)

    def display_info(self):
        print('Flight ID: ', self.generate_id)
        print('Source: ', self.source)
        print('Destination: ', self.destination)
        print('Duration: ', self.duration)
        print('Seats: ', self.seats)






