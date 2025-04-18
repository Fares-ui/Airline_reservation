from abc import ABC, abstractmethod
from multipledispatch import dispatch
from typing import List

# Abstract Base Class for User
class User(ABC):
    @abstractmethod
    def view_details(self):
        pass


# Passenger Class inheriting from User
class Passenger(User):
    def __init__(self, name: str, age: int, phone: str, address: str, passport_no: str):
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__address = address
        self.__passport_no = passport_no

    def view_details(self):
        print(f"\nPassenger Details:\nName: {self.__name}\nAge: {self.__age}\nPhone: {self.__phone}\nAddress: {self.__address}\nPassport No: {self.__passport_no}")

    def get_name(self):
        return self.__name

    def get_passport_no(self):
        return self.__passport_no


# Abstract Base Class for Airline Entities
class AirlineEntity(ABC):
    @abstractmethod
    def display_details(self):
        pass


# Baggage Class inheriting from AirlineEntity
class Baggage(AirlineEntity):
    def __init__(self, baggage_id: int, weight: float):
        self.__baggage_id = baggage_id
        self.__weight = weight
        self.__status = "in transit"

    def update_status(self, status: str):
        self.__status = status

    def check_weight(self, allowed_weight: float):
        if self.__weight > allowed_weight:
            excess_weight = self.__weight - allowed_weight
            extra_fee = excess_weight * 10
            print(f"Baggage ID {self.__baggage_id}: Your baggage exceeds the limit.\nExcess Weight: {excess_weight} kg | Extra Fee: ${extra_fee}")
        else:
            print(f"Baggage ID {self.__baggage_id}: Your baggage is within the allowed limit.")

    def display_details(self):
        print(f"Baggage ID {self.__baggage_id} status updated to: {self.__status}")


# Seat Class
class Seat:
    def __init__(self, seat_number: int, class_type: str, price: float):
        self.__seat_number = seat_number
        self.__class_type = class_type
        self.__price = price
        self.__available = True

    def book_seat(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def get_seat_number(self):
        return self.__seat_number

    def is_available(self):
        return self.__available

    def __str__(self):
        status = "Available" if self.__available else "Booked"
        return f"Seat {self.__seat_number} ({self.__class_type}, ${self.__price}) - {status}"


# Flight Class
class Flight(AirlineEntity):
    def __init__(self, flight_number: int, origin: str, destination: str, departure_time: str):
        self.__flight_number = flight_number
        self.__origin = origin
        self.__destination = destination
        self.__departure_time = departure_time
        self.__seats: List[Seat] = []

    def add_seat(self, seat: Seat):
        self.__seats.append(seat)

    def display_details(self):
        print(f"\nFlight {self.__flight_number} — {self.__origin} ➡ {self.__destination}")
        print(f"Departure Time: {self.__departure_time}")
        print("Available Seats:")
        for seat in self.__seats:
            print(seat)

    def book_seat(self, seat_number: int):
        for seat in self.__seats:
            if seat.get_seat_number() == seat_number:
                if seat.book_seat():
                    return seat
                else:
                    print(f"❌ Seat {seat_number} is already booked.")
                    return None
        print(f"Seat {seat_number} not found.")
        return None


# Ticket Class
class Ticket(AirlineEntity):
    def __init__(self, ticket_number: int, passenger: Passenger, flight: Flight, seat: Seat, payment_status: bool = False):
        self.__ticket_number = ticket_number
        self.__passenger = passenger
        self.__flight = flight
        self.__seat = seat
        self.__payment_status = payment_status

    def view_ticket(self):
        print(f"\n✅ Your Ticket Details:\nTicket No: {self.__ticket_number}\nPassenger: {self.__passenger.get_name()}\nSeat No: {self.__seat.get_seat_number()}\nFlight No: {self.__flight._Flight__flight_number}\nDestination: {self.__flight._Flight__destination}\nPayment Status: {'Completed' if self.__payment_status else 'Pending'}")

    def display_details(self):
        self.view_ticket()


# Airline Class
class Airline(AirlineEntity):
    def __init__(self, name: str, country: str, fleet_size: int, iata_code: str):
        self.__name = name
        self.__country = country
        self.__fleet_size = fleet_size
        self.__iata_code = iata_code

    def display_details(self):
        print(f"\nAirline Details:\nName: {self.__name}\nCountry: {self.__country}\nFleet Size: {self.__fleet_size}\nIATA Code: {self.__iata_code}")


# Airline Management System
class AirlineManagementSystem:
    def __init__(self):
        self.__passengers = []
        self.__flights = []
        self.__tickets = []
        self.__baggage = []
        self.__current_passenger = None

    def main_menu(self):
        while True:
            print("\nAirline Management System")
            print("1. Register or Login")
            print("2. Exit")
            choice = self.get_valid_input("Enter your choice: ", int)

            if choice == 1:
                self.auth_menu()
            elif choice == 2:
                print("Thank you for using the Airline Management System!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def auth_menu(self):
        while True:
            print("\n1. Register Passenger")
            print("2. Login Passenger")
            choice = self.get_valid_input("Enter your choice: ", int)
            if choice == 1:
                self.register_passenger()
                self.logged_in_menu()
                break
            elif choice == 2:
                self.login_passenger()
                if self.__current_passenger:
                    self.logged_in_menu()
                break
            else:
                print("Invalid choice. Please try again.")

    def logged_in_menu(self):
        while True:
            print("\n1. View Your Details")
            print("2. View Flights and Book a Seat")
            print("3. View Your Tickets")
            print("4. Manage Baggage")
            print("5. View Airline Info")
            print("6. Logout")
            choice = self.get_valid_input("Enter your choice: ", int)

            if choice == 1:
                self.view_passenger_details()
            elif choice == 2:
                self.view_flights()
                self.book_seat()
            elif choice == 3:
                self.view_tickets()
            elif choice == 4:
                self.manage_baggage()
            elif choice == 5:
                self.view_airline_details()
            elif choice == 6:
                self.__current_passenger = None
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_valid_input(self, prompt, expected_type):
        while True:
            try:
                value = input(prompt)
                converted = expected_type(value)
                if expected_type == int and prompt.lower().startswith("enter age") and converted < 18:
                    print("You must be 18 or older to register.")
                    continue
                return converted
            except ValueError:
                print(f"Invalid input! Please enter a valid {expected_type.__name__}.")

    def register_passenger(self):
        print("\nRegister Passenger")
        name = input("Enter Name: ")
        age = self.get_valid_input("Enter Age: ", int)

        while True:
            phone = input("Enter Phone Number: ")
            if phone.isdigit():
                break
            else:
                print("Invalid phone number! Please enter digits only.")

        address = input("Enter Address: ")
        while True:
            passport_no = input("Enter passport Number: ")
            if passport_no.isdigit():
                break
            else:
                print("Invalid passport number! Please enter digits only.")
        passenger = Passenger(name, age, phone, address, passport_no)
        self.__passengers.append(passenger)
        print(f"Passenger {name} registered successfully!")
        self.__current_passenger = passenger

    def login_passenger(self):
        print("\nLogin Passenger")
        passport_no = input("Enter Your Passport No to Login: ")
        for passenger in self.__passengers:
            if passenger.get_passport_no() == passport_no:
                self.__current_passenger = passenger
                print(f"Welcome, {passenger.get_name()}!")
                return
        print("Passenger not found! Please register.")

    def view_passenger_details(self):
        if self.__current_passenger:
            self.__current_passenger.view_details()
        else:
            print("Please login to view your details.")

    def view_flights(self):
        if not self.__flights:
            print("No flights available.")
            return
        for flight in self.__flights:
            flight.display_details()

    def book_seat(self):
        if not self.__current_passenger:
            print("Please login to book a seat.")
            return

        flight_number = self.get_valid_input("Enter Flight Number to Book Seat: ", int)
        found_flight = None
        for flight in self.__flights:
            if flight._Flight__flight_number == flight_number:
                found_flight = flight
                break
        if not found_flight:
            print("Flight not found.")
            return

        while True:
            seat_number = self.get_valid_input("Enter Seat Number: ", int)
            seat = found_flight.book_seat(seat_number)
            if seat:
                ticket = Ticket(len(self.__tickets) + 1, self.__current_passenger, found_flight, seat)
                self.__tickets.append(ticket)
                print("Seat booked successfully!")
                ticket.view_ticket()
                break
            else:
                print("Please try booking a different seat.")

    def view_tickets(self):
        if not self.__current_passenger:
            print("Please login to view your tickets.")
            return
        tickets_found = False
        for ticket in self.__tickets:
            if ticket._Ticket__passenger == self.__current_passenger:
                ticket.view_ticket()
                tickets_found = True
        if not tickets_found:
            print("You have no tickets booked.")

    def manage_baggage(self):
        print("\nManage Baggage")
        baggage_id = self.get_valid_input("Enter Baggage ID: ", int)
        weight = self.get_valid_input("Enter Baggage Weight (in kg): ", float)
        baggage = Baggage(baggage_id, weight)
        baggage.check_weight(allowed_weight=23)
        baggage.display_details()
        self.__baggage.append(baggage)

    def view_airline_details(self):
        airline = Airline("EgyptAir", "Egypt", 67, "MS")
        airline.display_details()


@dispatch(Passenger)
def handle_entity(entity: Passenger):
    print("Handling Passenger:")
    entity.view_details()


@dispatch(Flight)
def handle_entity(entity: Flight):
    print("Handling Flight:")
    entity.display_details()


@dispatch(Ticket)
def handle_entity(entity: Ticket):
    print("Handling Ticket:")
    entity.display_details()


@dispatch(Baggage)
def handle_entity(entity: Baggage):
    print("Handling Baggage:")
    entity.display_details()


if __name__ == "__main__":
    system = AirlineManagementSystem()

    flight1 = Flight(8452, "Cairo", "New York", "2am")
    flight1.add_seat(Seat(14, "Economy", 10000))
    flight1.add_seat(Seat(15, "Economy", 12000))
    system._AirlineManagementSystem__flights.append(flight1)

    system.main_menu()