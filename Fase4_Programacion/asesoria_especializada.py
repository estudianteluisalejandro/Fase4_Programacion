from servicio import Servicio


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self):
        return self.precio * 1.2

    def descripcion(self):
        return f"Servicio de asesoría especializada - Precio: {self.precio}"