from servicio import Servicio


class AlquilerEquipo(Servicio):

    def calcular_costo(self):
        return self.precio * 1.1

    def descripcion(self):
        return f"Servicio de alquiler de equipos - Precio: {self.precio}"