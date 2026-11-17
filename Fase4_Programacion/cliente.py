from excepciones import ClienteError


class Cliente:

    def __init__(self, nombre, cedula, correo):

        if not nombre:
            raise ClienteError("El nombre no puede estar vacío")

        if not cedula:
            raise ClienteError("La cédula no puede estar vacía")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__cedula} - {self.__correo}"
    