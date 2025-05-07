from abc import ABC, abstractmethod
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
        try:
            self.__baggage_id = int(baggage_id)
            self.__weight = float(weight)
            self.__status = "in transit"
        except ValueError:
            print("Error: Invalid data type for baggage ID or weight.")
        except TypeError:
            print("Error: Please ensure baggage ID and weight are the correct types.")
        except Exception as e:
            print("An unexpected error occurred during initialization:", e)

    def update_status(self, status: str):
        try:
            self.__status = str(status)
        except ValueError:
            print("Error: Cannot convert status to string.")
        except Exception as e:
            print("An unexpected error occurred while updating status:", e)

    def get_baggage_id(self):
        return self.__baggage_id

    def get_weight(self):
        return self.__weight

    def check_weight(self, allowed_weight: float):
        try:
            allowed_weight = float(allowed_weight)
            if self.__weight > allowed_weight:
                excess_weight = self.__weight - allowed_weight
                extra_fee = excess_weight * 10
                print(f"Baggage ID {self.__baggage_id}: Your baggage exceeds the limit.\n"
                      f"Excess Weight: {excess_weight} kg | Extra Fee: ${extra_fee}")
            else:
                print(f"Baggage ID {self.__baggage_id}: Your baggage is within the allowed limit.")
        except ValueError:
            print("Error: Allowed weight must be a number.")
        except OverflowError:
            print("Error: The values are too large to compute.")
        except Exception as e:
            print("An unexpected error occurred while checking weight:", e)

    def display_details(self):
        try:
            print(f"Baggage ID {self.__baggage_id} status updated to: {self.__status}")
        except Exception as e:
            print("An unexpected error occurred while displaying details:", e)


# Seat Class
class Seat:
    def __init__(self, seat_number: int, class_type: str, price: float):
        try:
            self.__seat_number = int(seat_number)
            self.__class_type = str(class_type)
            self.__price = float(price)
            self.__available = True
        except ValueError:
            print("Error: Invalid value for seat number, class type, or price.")
        except TypeError:
            print("Error: Incorrect data type provided.")
        except Exception as e:
            print("An unexpected error occurred during seat initialization:", e)

    def book_seat(self):
        try:
            if self.__available:
                self.__available = False
                return True
            return False
        except Exception as e:
            print("An unexpected error occurred while booking the seat:", e)

    def get_seat_number(self):
        try:
            return self.__seat_number
        except Exception as e:
            print("An unexpected error occurred while getting the seat number:", e)

    def is_available(self):
        try:
            return self.__available
        except Exception as e:
            print("An unexpected error occurred while checking availability:", e)

    def make_available(self):
        try:
            self.__available = True
        except Exception as e:
            print("An unexpected error occurred while making the seat available:", e)

    def __str__(self):
        try:
            status = "Available" if self.__available else "Booked"
            return f"Seat {self.__seat_number} ({self.__class_type}, ${self.__price}) - {status}"
        except Exception as e:
            return f"An unexpected error occurred while generating seat string: {e}"


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
        print(f"\n ✈️ Flight {self.__flight_number} — {self.__origin} ➡ {self.__destination}")
        print(f"Departure Time: {self.__departure_time}")
        print("Available Seats:")
        for seat in self.__seats:
            print(seat)
    
    def get_flights(self):
        return self.__flight_number
    
    def get_destination(self):
        return self.__destination
    

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
    
    def get_seats(self):    
        return self.__seats
 

# Ticket Class
class Ticket(AirlineEntity):
    def __init__(self, ticket_number: int, passenger: Passenger, flight: Flight, seat: Seat, baggage: Baggage = None, payment_status: bool = False):
        try:
            self.__ticket_number = int(ticket_number)
            self.__passenger = passenger
            self.__flight = flight
            self.__seat = seat
            self.__baggage = baggage
            self.__payment_status = bool(payment_status)
            self.__payment = None # Payment object for handling payment       
        except ValueError:
            print("Error: Invalid value for ticket number or payment status.")
        except TypeError:
            print("Error: Invalid type for one or more inputs in Ticket.")
        except Exception as e:
            print("An unexpected error occurred during ticket initialization:", e)

    def get_ticket_number(self): 
        try:
            return self.__ticket_number
        except Exception as e:
            print("An unexpected error occurred while getting ticket number:", e)

    def get_passenger(self):
        try:
            return self.__passenger
        except Exception as e:
            print("An unexpected error occurred while getting passenger:", e)

    def set_baggage(self, baggage: Baggage):
        self.__baggage = baggage

    def get_seat(self):
        try:
            return self.__seat
        except Exception as e:
            print("An unexpected error occurred while getting seat:", e)
            
    def update_payment_status(self, status: bool):
        self.__payment_status = status
        
    def view_ticket(self):
        try:
            print(f"\n🎫 Your Ticket Details:\n"
                  f"Ticket No: {self.__ticket_number}\n"
                  f"Passenger: {self.__passenger.get_name()}\n"
                  f"Seat No: {self.__seat.get_seat_number()}\n"
                  f"Flight No: {self.__flight.get_flights()}\n"
                  f"Destination: {self.__flight.get_destination()}\n"
                  f"Payment Status: {'Completed ✅' if self.__payment_status else 'Pending⏳'}")
            if self.__baggage:
                print(f"Baggage ID: {self.__baggage.get_baggage_id()}")
    
        except AttributeError:
            print("Error: One of the ticket components is missing or improperly set.")
        except Exception as e:
            print("An unexpected error occurred while viewing ticket:", e)
    
    def create_payment(self, amount: float, card_number: str):
        if self.__payment is None:           
           self.__payment = Payment(self, amount, card_number)
        return self.__payment

    def display_details(self):
        try:
            self.view_ticket()
        except Exception as e:
            print("An unexpected error occurred while displaying ticket details:", e)


class Payment:
    def __init__(self, ticket: Ticket, amount: float, card_number: int):
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if not self.is_valid_card_number(str(card_number)):
            raise ValueError("Invalid card number. It must be 16 digits.")    
        self.__ticket = ticket
        self.__amount = float(amount)
        self.__payment_status = False
        self.__card_number = str(card_number)
    
    def is_valid_card_number(self, card_number: str) -> bool:
        return card_number.isdigit() and len(card_number) == 16
    
    def make_payment(self):
        if self.__payment_status:
            print(f"⚠️ Payment already made for ticket {self.__ticket.get_ticket_number()}.")
            return

        try:
            masked_card = "**** **** **** " + self.__card_number[-4:]
            print(f"Processing Card payment of ${self.__amount} using card ending with {masked_card}...")
            self.__payment_status = True
            self.__ticket.update_payment_status(True)
            print(f"✅ Card payment successful for Ticket {self.__ticket.get_ticket_number()}.")
        except Exception as e:
            print(f"❌ Payment failed due to: {e}")

    def get_payment_status(self):
        return self.__payment_status

    def get_amount(self):
        return self.__amount

    def get_ticket(self):
        return self.__ticket


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
        self.__admin_username = "admin"
        self.__admin_password = "admin"

    def get_flights(self):
        return self.__flights

    def admin_menu(self):
        while True:
            print("\nAdmin Panel")
            print("1. Add New Flight")
            print("2. Add Seats to Flight")
            print("3. View All Flights")
            print("4. View All Bookings")
            print("5. View Registered Passengers")
            print("6. Cancel a Ticket")
            print("7. Logout")

            choice = self.get_valid_input("Enter your choice: ", int)

            if choice == 1:
                self.add_new_flight()
            elif choice == 2:
                self.add_seats_to_flight()
            elif choice == 3:
                self.view_flights()
            elif choice == 4:
                self.view_all_bookings()
            elif choice == 5:
                self.view_all_passengers()
            elif choice == 6:
                ticket_number = self.get_valid_input("Enter Ticket Number to Cancel: ", int)
                self.cancel_ticket(ticket_number)
            elif choice == 7:
                print("Logged out from Admin Panel.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_flight(self):
        print("\nAdd New Flight")
        flight_number = self.get_valid_input("Enter Flight Number: ", int)

        for flight in self.get_flights():
            if flight.get_flights() == flight_number:
                print("❌ Flight with this number already exists.")
                return

        while True:
            origin = self.get_valid_input("Enter Origin: ", str)
            if origin.isalpha():
                break
            else:
                print("Invalid Input")
                
        while True:
            destination = self.get_valid_input("Enter Destination: ", str)
            if destination.isalpha():
                break
            else:
                print("Invalid Input")
                
        departure_time = self.get_valid_input("Enter Departure Time: ", str)
        flight = Flight(flight_number, origin, destination, departure_time)
        self.__flights.append(flight)
        print("✅ New flight added successfully.")

    def add_seats_to_flight(self):
        flight_number = self.get_valid_input("Enter Flight Number to Add Seats: ", int)

        for flight in self.__flights:
            if flight.get_flights() == flight_number:
                while True:
                    # Loop until user provides a unique seat number
                    while True:
                        seat_number = self.get_valid_input("Enter Seat Number: ", int)

                        # Check if seat number already exists in flight
                        existing_seat = None
                        for seat in flight.get_seats():
                            if seat.get_seat_number() == seat_number:
                                existing_seat = seat
                                break

                        if existing_seat:
                            print(f"❌ Seat number {seat_number} already exists. Please enter a different seat number.")
                        else:
                            break  # Valid seat number

                    # Validate class type input
                    while True:   
                        class_type = input("Enter Class Type (Economy or Business): ").strip().capitalize()
                        if class_type in ["Economy", "Business"]:
                            break
                        print("❌ Invalid class type. Please enter 'Economy' or 'Business'.")

                    price = self.get_valid_input("Enter Price: ", float)

                    # Create and add the seat
                    new_seat = Seat(seat_number, class_type, price)
                    flight.add_seat(new_seat)
                    print("✅ Seat added.")

                    more = input("Add another seat? (y/n): ").lower()
                    if more != 'y':
                        break
                return

        print("❌ Flight not found.")

    def cancel_ticket(self, ticket_number: int):
        for ticket in self.__tickets:
            if ticket.get_ticket_number() == ticket_number:
                # Make the seat available again
                ticket.get_seat().make_available()
                self.__tickets.remove(ticket)
                print(f"✅ Ticket {ticket_number} has been successfully canceled.")
                return
        print(f"❌ Ticket {ticket_number} not found.")

    def view_all_bookings(self):
        if not self.__tickets:
            print("No bookings available.")
        else:
            for ticket in self.__tickets:
                ticket.view_ticket()

    def view_all_passengers(self):
        if not self.__passengers:
            print("No registered passengers.")
        else:
            for passenger in self.__passengers:
                passenger.view_details()

    def main_menu(self):
        while True:
            print("\nAirline Management System")
            print("1. Register or Login")
            print("2. Admin Panel")
            print("3. Exit")

            choice = self.get_valid_input("Enter your choice: ", int)

            if choice == 1:
                self.auth_menu()
            elif choice == 2:
                self.admin_login()
            elif choice == 3:
                print("Thank you for using the Airline Management System!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def admin_login(self):
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if username == self.__admin_username and password == self.__admin_password:
            print("✅ Admin login successful.")
            self.admin_menu()
        else:
            print("❌ Invalid credentials. Access denied.")

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
            print("6. Cancel a Ticket")
            print("7. Make Payment for Ticket")
            print("8. Logout")

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
                ticket_number = self.get_valid_input("Enter your Ticket Number to cancel: ", int)
                found = False
                for ticket in self.__tickets:
                    if ticket.get_ticket_number() == ticket_number and ticket.get_passenger() == self.__current_passenger:
                        self.cancel_ticket(ticket_number)
                        found = True
                        break
                if not found:
                    print("❌ Ticket not found or does not belong to you.")
            elif choice == 7:
                self.make_payment_for_ticket()
            elif choice == 8:
                self.__current_passenger = None
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_seat(self):
        if not self.__current_passenger:
            print("Please login to book a seat.")
            return

        flight_number = self.get_valid_input("Enter Flight Number to Book Seat: ", int)
        found_flight = None
        
        # Find the flight
        for flight in self.__flights:
            if flight.get_flights() == flight_number:
                found_flight = flight
                break
        
        if not found_flight:
            print("Flight not found.")
            return

        # Display available seats
        print("\nAvailable Seats:")
        available_seats = [seat for seat in found_flight.get_seats() if seat.is_available()]
        if not available_seats:
            print("No available seats on this flight.")
            return
        
        for seat in available_seats:
            print(seat)

        # Get seat number to book
        while True:
            seat_number = self.get_valid_input("\nEnter Seat Number to book (or 0 to cancel): ", int)
            if seat_number == 0:
                return
            
            # Find the seat
            selected_seat = None
            for seat in found_flight.get_seats():
                if seat.get_seat_number() == seat_number:
                    selected_seat = seat
                    break
            
            if not selected_seat:
                print("Seat not found. Please try again.")
                continue
                
            if not selected_seat.is_available():
                print("Seat is already booked. Please choose another seat.")
                continue
                
            # Book the seat
            if selected_seat.book_seat():
                # Create ticket
                ticket = Ticket(len(self.__tickets) + 1, self.__current_passenger, found_flight, selected_seat,None)  # No baggage initially
                self.__tickets.append(ticket)
                print("\nSeat booked successfully!")
                ticket.view_ticket()
                
                # Ask about baggage
                add_baggage = input("\nWould you like to add baggage? (y/n): ").lower()
                if add_baggage == 'y':
                    self.manage_baggage_for_ticket(ticket)
                break
            else:
                print("Failed to book seat. Please try again.")

    def manage_baggage_for_ticket(self, ticket):
        print("\nAdding Baggage to Ticket")
        baggage_id = self.get_valid_input("Enter Baggage ID: ", int)
        weight = self.get_valid_input("Enter Baggage Weight (in kg): ", float)
        baggage = Baggage(baggage_id, weight)
        baggage.check_weight(allowed_weight=23)
        baggage.display_details()
        ticket.set_baggage(baggage)
        self.__baggage.append(baggage)
        print("Baggage added to ticket successfully!")

    def make_payment_for_ticket(self):
        if not self.__current_passenger:
            print("Please login to make a payment.")
            return
            
        ticket_number = self.get_valid_input("Enter your Ticket Number to make payment: ", int)
        ticket = None
        
        for t in self.__tickets:
            if t.get_ticket_number() == ticket_number and t.get_passenger() == self.__current_passenger:
                ticket = t
                break
                
        if ticket:
            if ticket._Ticket__payment_status: 
                print(f"✅ Payment for Ticket {ticket_number} is already completed.")
                return
            else:
                amount = ticket.get_seat()._Seat__price
                while True:
                    card_number = input("Enter your 16-digit card number: ").strip()
                    if card_number.isdigit() and len(card_number) == 16:
                        break
                    else:
                        print("❌ Invalid card number. Please enter exactly 16 digits.")

                payment = ticket.create_payment(amount, card_number)
                payment.make_payment()
        else:
            print(f"❌ Ticket {ticket_number} not found or does not belong to you.")

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


if __name__ == "__main__":
    system = AirlineManagementSystem()

    # Initialize some sample flights and seats
    flight1 = Flight(452, "Cairo", "New York", "2am")
    flight1.add_seat(Seat(14, "Economy", 1000))
    flight1.add_seat(Seat(15, "Economy", 1200))
    
    flight2 = Flight(981, "Cairo", "London", "9:30am")
    flight2.add_seat(Seat(12, "Economy", 500))
    flight2.add_seat(Seat(14, "Business", 1200))
    
    flight3 = Flight(985, "Cairo", "Paris", "11:00am")
    flight3.add_seat(Seat(21, "Economy", 950))
    flight3.add_seat(Seat(2, "Business", 2200))

    flight4 = Flight(791, "Cairo", "Dubai", "6:00pm")
    flight4.add_seat(Seat(18, "Economy", 400))
    flight4.add_seat(Seat(3, "Business", 950))

    flight5 = Flight(839, "Cairo", "Jeddah", "1:15pm")
    flight5.add_seat(Seat(25, "Economy", 350))
    flight5.add_seat(Seat(5, "Business", 800))
    
    system._AirlineManagementSystem__flights.append(flight1)
    system._AirlineManagementSystem__flights.append(flight2)
    system._AirlineManagementSystem__flights.append(flight3)
    system._AirlineManagementSystem__flights.append(flight4)
    system._AirlineManagementSystem__flights.append(flight5)

    system.main_menu()
