import datetime

# Base class representing a vehicle
class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.available = True  # Vehicle availability status

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"{self.brand} {self.model} (ID: {self.vehicle_id}, Price: INR {self.rental_price}/day) - {availability}"


# Class representing a car
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, doors):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.doors = doors


# Class representing a bike
class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, type_of_bike):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.type_of_bike = type_of_bike


# Class representing a truck
class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, capacity):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.capacity = capacity


# Class representing a customer
class Customer:
    def __init__(self, name, drivers_license):
        self.name = name
        self.drivers_license = drivers_license
        self.rented_vehicles = []  # List to store rented vehicles and rental info

    def rent_vehicle(self, vehicle, rental_period):
        if vehicle.available:
            vehicle.available = False
            rental_info = {
                'vehicle': vehicle,
                'rental_start': datetime.datetime.now(),
                'rental_period': rental_period
            }
            self.rented_vehicles.append(rental_info)
            print(f"{self.name} rented {vehicle.brand} {vehicle.model}.")
        else:
            print(f"{vehicle.brand} {vehicle.model} is not available.")

    def return_vehicle(self, vehicle):
        for rental in self.rented_vehicles:
            if rental['vehicle'].vehicle_id == vehicle.vehicle_id:
                rental_duration = (datetime.datetime.now() - rental['rental_start']).days
                rental_cost = rental_duration * rental['vehicle'].rental_price
                rental['vehicle'].available = True
                self.rented_vehicles.remove(rental)
                print(f"{self.name} returned {vehicle.brand} {vehicle.model}. Total cost: INR {rental_cost:.2f}")
                return
        print(f"{self.name} has not rented {vehicle.brand} {vehicle.model}.")


# Class representing the rental service
class RentalService:
    def __init__(self):
        self.fleet = []  # List to store all vehicles

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)
        print(f"Added {vehicle} to the fleet.")

    def view_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.fleet:
            if vehicle.available:
                print(vehicle)

    def view_rental_history(self, customer):
        print(f"Rental history for {customer.name}:")
        for rental in customer.rented_vehicles:
            vehicle = rental['vehicle']
            print(f"- {vehicle.brand} {vehicle.model} rented on {rental['rental_start']} for {rental['rental_period']} days.")


# Example usage of the system
rental_service = RentalService()

# Adding vehicles to the fleet
car1 = Car("C001", "Toyota", "Camry", 40, 4)
car2 = Car("C002", "Honda", "Civic", 35, 4)
bike1 = Bike("B001", "Yamaha", "YZF-R3", 25, "Sport")
truck1 = Truck("T001", "Ford", "F-150", 70, 1000)

rental_service.add_vehicle(car1)
rental_service.add_vehicle(car2)
rental_service.add_vehicle(bike1)
rental_service.add_vehicle(truck1)

# Creating a customer
customer1 = Customer("Aditya", "MH12AC1225")

# View available vehicles
rental_service.view_available_vehicles()

# Renting a vehicle
customer1.rent_vehicle(car1, 5)  # Rent for 5 days

# View available vehicles after renting
rental_service.view_available_vehicles()

# Returning a vehicle
customer1.return_vehicle(car1)

# View rental history
rental_service.view_rental_history(customer1)

# View available vehicles after returning
rental_service.view_available_vehicles()
