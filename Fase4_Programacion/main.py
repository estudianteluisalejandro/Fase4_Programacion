from cliente import Cliente
from reserva_sala import ReservaSala
from reserva import Reserva

print("OPERACION 1")
cliente1 = Cliente("Luis Alejandro", "208026", "luis@gmail.com")
print(cliente1.mostrar_info())

print("OPERACION 2")
servicio1 = ReservaSala("Sala VIP", 100000)

print("OPERACION 3")
reserva1 = Reserva(cliente1, servicio1, 2)

print("OPERACION 4")
reserva1.confirmar()

print("OPERACION 5")
print(reserva1.mostrar_reserva())

print("OPERACION 6")
reserva1.cancelar()

print("OPERACION 7")
print("Reserva cancelada correctamente")

print("OPERACION 8")
cliente2 = Cliente("Carlos", "12345", "carlos@gmail.com")

print("OPERACION 9")
servicio2 = ReservaSala("Sala Ejecutiva", 200000)

print("OPERACION 10")
reserva2 = Reserva(cliente2, servicio2, 3)
print(reserva2.mostrar_reserva())