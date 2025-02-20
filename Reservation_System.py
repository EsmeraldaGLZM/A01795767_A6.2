import json
import os
import time


class Hotel:
    """Clase que representa un hotel."""
    def __init__(self, hotel_id, name, location):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location

    def to_dict(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location
        }


class Customer:
    """Clase que representa un cliente."""
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }


class Reservation:
    """Clase que representa una reservación."""
    def __init__(self, reservation_id, customer, hotel):
        self.reservation_id = reservation_id
        self.customer = customer
        self.hotel = hotel

    def to_dict(self):
        return {
            "reservation_id": self.reservation_id,
            "customer": self.customer.to_dict(),
            "hotel": self.hotel.to_dict()
        }


class ReservationSystem:
    """Clase que maneja las operaciones de hoteles, clientes y reservaciones."""
    def __init__(self, hotel_file, customer_file, reservation_file):
        self.hotel_file = hotel_file
        self.customer_file = customer_file
        self.reservation_file = reservation_file
        self.hotels = self.load_data(self.hotel_file)
        self.customers = self.load_data(self.customer_file)
        self.reservations = self.load_data(self.reservation_file)

    def load_data(self, filename):
        """Carga los datos desde un archivo JSON."""
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f"Error al leer los datos de {filename}, archivo corrupto.")
                return []
        return []

    def save_data(self, filename, data):
        """Guarda los datos en un archivo JSON."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def create_hotel(self, hotel):
        self.hotels.append(hotel.to_dict())
        self.save_data(self.hotel_file, self.hotels)

    def delete_hotel(self, hotel_id):
        self.hotels = [hotel for hotel in self.hotels if hotel["hotel_id"] != hotel_id]
        self.save_data(self.hotel_file, self.hotels)

    def modify_hotel(self, hotel_id, name=None, location=None):
        for hotel in self.hotels:
            if hotel["hotel_id"] == hotel_id:
                if name:
                    hotel["name"] = name
                if location:
                    hotel["location"] = location
        self.save_data(self.hotel_file, self.hotels)

    def create_customer(self, customer):
        self.customers.append(customer.to_dict())
        self.save_data(self.customer_file, self.customers)

    def delete_customer(self, customer_id):
        self.customers = [
            customer for customer in self.customers
            if customer["customer_id"] != customer_id
        ]
        self.save_data(self.customer_file, self.customers)

    def modify_customer(self, customer_id, name=None, email=None):
        for customer in self.customers:
            if customer["customer_id"] == customer_id:
                if name:
                    customer["name"] = name
                if email:
                    customer["email"] = email
        self.save_data(self.customer_file, self.customers)

    def create_reservation(self, reservation):
        self.reservations.append(reservation.to_dict())
        self.save_data(self.reservation_file, self.reservations)

    def cancel_reservation(self, reservation_id):
        self.reservations = [
            res for res in self.reservations
            if res["reservation_id"] != reservation_id
        ]
        self.save_data(self.reservation_file, self.reservations)

    def display_hotels(self):
        return self.hotels

    def display_customers(self):
        return self.customers

    def display_reservations(self):
        return self.reservations

    def run_flake8(self):
        """Ejecuta Flake8 y guarda el reporte en un archivo único."""
        timestamp = int(time.time())
        flake8_report = f"flake8_report_{timestamp}.txt"
        command = (
            "py -3.9 -m flake8 Reservation_System.py "
            "--max-line-length=100 > " + flake8_report
        )
        os.system(command)
        print(f"Reporte de Flake8 generado en {flake8_report}")


if __name__ == "__main__":
    reservation_system = ReservationSystem(
        "hotels.json", "customers.json", "reservations.json"
    )
    reservation_system.run_flake8()
