from Reservation_System import ReservationSystem, Hotel, Customer, Reservation

def test_reservation_system():
    """Script de prueba para ejecutar todas las funciones del sistema usando los archivos principales."""
    rs = ReservationSystem("hotels.json", "customers.json", "reservations.json")
    
    # 1. Crear un hotel
    hotel = Hotel(1, "Hotel Paradise", "Beach City")
    rs.create_hotel(hotel)
    print("Hoteles después de crear uno:", rs.display_hotels())
    
    # 2. Modificar un hotel
    rs.modify_hotel(1, name="Luxury Resort", location="Island Beach")
    print("Hoteles después de modificar:", rs.display_hotels())
    
    # 3. Eliminar un hotel
    rs.delete_hotel(1)
    print("Hoteles después de eliminar:", rs.display_hotels())
    
    # 4. Crear un cliente
    customer = Customer(1, "Alice Doe", "alice@example.com")
    rs.create_customer(customer)
    print("Clientes después de crear uno:", rs.display_customers())
    
    # 5. Modificar un cliente
    rs.modify_customer(1, name="Alice Smith", email="alice.smith@example.com")
    print("Clientes después de modificar:", rs.display_customers())
    
    # 6. Eliminar un cliente
    rs.delete_customer(1)
    print("Clientes después de eliminar:", rs.display_customers())
    
    # 7. Crear una reservación
    rs.create_hotel(Hotel(2, "Grand Hotel", "Downtown"))
    rs.create_customer(Customer(2, "Bob Smith", "bob@example.com"))
    reservation = Reservation(1, Customer(2, "Bob Smith", "bob@example.com"), Hotel(2, "Grand Hotel", "Downtown"))
    rs.create_reservation(reservation)
    print("Reservaciones después de crear una:", rs.display_reservations())
    
    # 8. Cancelar una reservación
    rs.cancel_reservation(1)
    print("Reservaciones después de cancelar:", rs.display_reservations())

# Ejecutar el script de prueba
test_reservation_system()
