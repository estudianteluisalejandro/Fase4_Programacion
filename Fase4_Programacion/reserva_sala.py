from servicio import Servicio


class ReservaSala(Servicio):

    def calcular_costo(self):
        return self.precio

    def descripcion(self):
        return f"Servicio de reserva de sala - Precio: {self.precio}"