import flight


flight_1 = flight.FlightClass('Isengard', 'Minas Morghul', 415, 3)
flight_2 = flight.FlightClass('Gondor', 'Westfold', 313, 2)

flight_1.add_passenger('Bilbo Baggins')
flight_1.add_passenger('Gandalf The Grey')
flight_1.add_passenger('Thorin Oakenshield')

flight_2.add_passenger('Fredegar Bolger')
flight_2.add_passenger('Melilot Brandybuck')

flight_1.display_info()
flight_2.display_info()

flight_1.list_passengers()
flight_2.list_passengers()









