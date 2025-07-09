class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.mascotas = []

        def agregar_mascota(self, mascota):
            self.mascotas.append(mascota)

            class Mascota:
                def __init__(self, nombre, especie, raza, edad):
                    self.nombre = nombre
                    self.especie = especie
                    self.raza = raza
                    self.edad = edad
                    self.hisotial = []

                    def agregar_Citas(self, citas):
                        self.historial.append(citas)

                        class CitaMedica:
                            def __init__(self, fecha, motivo, diagnostico):
                                self.fecha = fecha
                                self.motivo = motivo
                                self.diagnostico = diagnostico

                                class Veterinaria:
                                    def __init__(self):
                                        self.cliente = []

                                        def registrar_Cliente(self, nombre, telefono, correo):
                                            cliente = Cliente(nombre, telefono, correo)
                                            self.cliente.append(cliente)
                                            print("Cliente registrado exitosamente")

                                            def BuscarCliente(self, nombre):
                                                for cliente in self.cliente:
                                                    if cliente.nombre.lower() == nombre.lower():
                                                        return cliente
                                                    return None

                                                def registrarMascota(self, nombre_Cliente, nombre_Mascota, Especie, Raza, edad):
                                                    cliente = self.BuscarCliente(nombre_Cliente)
                                                    if cliente:
                                                        mascota = Mascota(nombre_Mascota, Especie, Raza, edad)
                                                        Cliente.agregar_mascota(mascota)
                                                        print("Mascota registrada exitosamente")
                                                    else:
                                                        print("Cliente no encontrado")

                                                        def agendar_cita(self, nombre_Cliente, nombre_Mascota, fecha, motivo, diagnostico):
                                                            cliente = self.BuscarCliente(nombre_Cliente)
                                                            if cliente:
                                                                for mascota in cliente.mascotas:
                                                                    if mascota.nombre.lower() == nombre_Mascota.lower():
                                                                        citas = CitaMedica(fecha, motivo, diagnostico)
                                                                        mascota.agregar_Citas(citas)
                                                                        print("Cita medica registrada exitosamente")
                                                                        return
                                                                    print("Mascota no encontrada")
                                                                else:
                                                                    print("Cliente no encontrado")

                                                            def Mostrar_Historial(self, nombre_Cliente, nombre_Mascota):
                                                                cliente = self.BuscarCliente(nombre_Cliente)
                                                                if cliente:
                                                                    for mascota in cliente.mascotas:
                                                                        if mascota.nombre.lower() == nombre_Mascota.lower():
                                                                            if mascota.historial:
                                                                                print(f"Historial medico de mascota {mascota.nombre}")
                                                                                for citas in mascota.historial:
                                                                                    print(f"-{cita.fecha}: {cita.motivo} → {cita.diagnostico}")
                                                                                else:
                                                                                    print("No hay citas registradas.")

                                                                                    def ver_ClientesYMascota(self):
                                                                                        for cliente in self.cliente:
                                                                                            print(f"{cliente.nombre} ({cliente.telefono}) {cliente.correo})")
                                                                                            for mascota in cliente.mascotas:
                                                                                                print(
                                                                                                    f"{mascota.nombre} - {mascota.especie}, {mascota.raza}, {mascota.edad} años")

                                                                                                veterinaria = veterinaria()

                                                                                                while True:
                                                                                                    print("Bienvenido a la veterinaria")
                                                                                                    print("1. Registrar nuevo Cliente")
                                                                                                    print("2. Registrar nuevo Mascota")
                                                                                                    print("3. Agendar cita medica")
                                                                                                    print("4. Ver el historial de citas")
                                                                                                    print("5. Ver clientes y mascotas")
                                                                                                    print("6. Salir")

                                                                                                    opcion = input("Seleccione una opcion: ")

                                                                                                    if opcion == "1":
                                                                                                        nombre = input("Nombre del cliente: ")
                                                                                                        telefono = input("Telefono del cliente: ")
                                                                                                        correo = input("Correo del cliente: ")
                                                                                                        Veterinaria.registrar_cliente(nombre, telefono, correo)