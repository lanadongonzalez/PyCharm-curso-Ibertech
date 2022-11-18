import random


# Definimos una clase genérica de persona
class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        pass


# Definimos la clase doctor
class Doctor(Persona):
    def __init__(self, especialidad, dni, nombre, apellido, en_servicio=True):
        Persona.__init__(self, dni, nombre, apellido)
        self.especialidad = especialidad
        self.en_servicio = en_servicio

    # Un método para fichar. Cambia el estado del atributo booleano en_servicio
    def fichar(self):
        self.en_servicio = not self.en_servicio
        # En función del mensaje sabremos si ficha para entra o salir
        if self.en_servicio:
            print('Hola, {}. Buen día de trabajo'.format(self.nombre))
        else:
            print('Adiós, {}. Disfruta tu tiempo libre'.format(self.nombre))

    # El método devuelve una dupla: (True, enfermedad) o (False, cuentitis)
    @staticmethod  # Lo defino como método estático porque no se cambian las instancias y para probar diferentes formas
    def diagnosticar(paciente):
        esta_enfermo = True
        lista_enfermedades = ['covid', 'gripe', 'esguince', 'apendicitis']
        if random.randint(1, 10) < 7:
            esta_enfermo = False
            enfermedad = 'cuentitis aguda'
        else:
            enfermedad = random.choice(lista_enfermedades)
        print('El paciente {} ha sido diagnosticado de {}'.format(paciente.nombre, enfermedad))
        return esta_enfermo, enfermedad

    def __str__(self):
        return """DNI\t {}
        NOMBRE\t {}
        APELLIDO\t {}
        EN SERVICIO\t {}
        ESPECIALIDAD\t {}""".format(self.dni, self.nombre, self.apellido, self.en_servicio, self.especialidad)


# Definimos la clase enfermero
class Enfermero(Persona):
    def __init__(self, sector, dni, nombre, apellido, en_servicio=True):
        Persona.__init__(self, dni, nombre, apellido)
        self.sector = sector
        self.en_servicio = en_servicio

    # Un método para entra y salir del trabajo
    def fichar(self):
        self.en_servicio = not self.en_servicio
        if self.en_servicio:
            print('Hola, {}. Buen día de trabajo'.format(self.nombre))
        else:
            print('Adiós, {}. Disfruta tu tiempo libre'.format(self.nombre))

    @staticmethod  # Un método para sacar al paciente de la sala de espera y meterlo en la consulta
    def atender_paciente(sala_espera, consulta):
        if len(sala_espera) > 0:
            consulta.add_paciente(sala_espera[0])
            sala_espera.remove(sala_espera[0])

    def __str__(self):
        return """DNI\t {}
        NOMBRE\t {}
        APELLIDO\t {}
        EN SERVICIO\t {}
        SECTOR\t {}""".format(self.dni, self.nombre, self.apellido, self.en_servicio, self.sector)


# Definimos la clase paciente
class Paciente(Persona):
    def __init__(self, dni, nombre, apellido, sintomas):
        Persona.__init__(self, dni, nombre, apellido)
        self.sintomas = sintomas

    def __str__(self):
        return """DNI\t {}
        NOMBRE\t {}
        APELLIDO\t {}
        SINTOMAS\t {}""".format(self.dni, self.nombre, self.apellido, self.sintomas)


# Definimos la clase enfermo. Es idéntica a la del paciente con el atributo enfermedad
class Enfermo(Paciente):
    def __init__(self, enfermedad, dni, nombre, apellido, sintomas):
        Paciente.__init__(self, dni, nombre, apellido, sintomas)
        self.enfermedad = enfermedad

    def __str__(self):
        return """DNI\t {}
        NOMBRE\t {}
        APELLIDO\t {}
        SINTOMAS\t {}
        ENFERMEDAD\t {}""".format(self.dni, self.nombre, self.apellido, self.sintomas, self.enfermedad)


# Definimos la clase consulta
class Consulta:
    # En un principio, creamos la consulta sin doctor ni paciente. Si metemos un doctor, comprobamos que haya fichado
    def __init__(self, id_number, doctor=None, paciente=None):
        self.id_number = id_number
        self.doctor = doctor
        if (doctor is not None) and (not doctor.en_servicio):  # Comprobamos que esté de servicio y sino que fiche
            self.doctor.fichar()
        self.paciente = paciente

    # Un método para que el doctor entre en la consulta. Primero miramos si hay alguien y si el doctor está en su turno
    def add_doctor(self, doctor):
        if self.doctor:
            print('Disculpa, dr {}, está consulta esta ocupada. Váyase a otra'.format(doctor.nombre))
        elif not doctor.en_servicio:
            print('No voy a entrar en la consulta. Mi turno ha acabado')
        else:
            self.doctor = doctor

    # Método para que el doctor salga de la consulta y fiche
    def salir_doctor(self):
        if self.doctor is not None:
            self.doctor.fichar()
        self.doctor = None

    # Método para meter a un paciente en la consulta
    def add_paciente(self, paciente):
        if self.paciente:
            print('Disculpa, {}. Estoy ocupado con {}'.format(paciente.nombre, self.paciente.nombre))
        else:
            self.paciente = paciente

    # Método para sacar a un paciente de la consulta
    def despachar_paciente(self):
        self.paciente = None

    def __str__(self):
        return """Nº CONSULTA\t {}
        DOCTOR\t {}
        PACIENTE\t {}
                """.format(self.id_number, self.doctor, self.paciente)


# Creamos a las personas que estarán en el hospital
persona1 = Persona('111A', 'Alejandra', 'Sánchez')
doctor1 = Doctor('pediatra', persona1.dni, persona1.nombre, persona1.apellido, en_servicio=False)
doctor2 = Doctor('familia', '222A', 'Irene', 'Sanz', en_servicio=False)
# print(doctor1)
# print(doctor2)
enfermero1 = Enfermero('maxilofacial', '333A', 'Carlos', 'Pérez', False)
enfermero2 = Enfermero('urgencias', '444A', 'Álvaro', 'Gómez', False)
# print(enfermero1)
# print(enfermero2)
paciente1 = Paciente('555A', 'Paco', 'Saura', ['falta olfato', 'dolor cabeza'])
paciente2 = Paciente('666A', 'Marta', 'San Miguel', ['dolor de tobillo', 'inflamación en la zona'])
paciente3 = Paciente('777A', 'Lucía', 'Del Romero', ['fiebre', 'diarrea'])
paciente4 = Paciente('888A', 'Inma', 'Luque', ['dolor garganta', 'dolor cabeza'])

consulta1 = Consulta('1')
consulta2 = Consulta('2')
# print(consulta1)
# print(consulta2)
# Los trabajadores creados entran a trabajar (fichan)
doctor1.fichar()
doctor2.fichar()
enfermero1.fichar()
enfermero2.fichar()
# print(doctor1)
# print(doctor2)
# print(enfermero1)
# print(enfermero2)
consulta1.add_doctor(doctor1)
consulta2.add_doctor(doctor2)
# print(consulta1)
# print(consulta2)

sala_espera = [paciente1, paciente2, paciente3, paciente4]
enfermos_en_habitacion = []
enfermos_en_pasillo = []
lista_enfermeros = [enfermero1, enfermero2]
lista_consultas = [consulta1, consulta2]

# Aquí empieza el proceso de tratar pacientes
turno_enfermero = 0
while len(sala_espera) > 0:
    print('========Empieza la colsulta===========')
    esta_enfermo = True
    # El enfermero correspondiente atiende al paciente (le manda a la consulta correspondiente)
    lista_enfermeros[turno_enfermero % 2].atender_paciente(sala_espera, lista_consultas[turno_enfermero % 2])
    # Comprobamos que haya un doctor en la consulta y este le diagnostica
    if lista_consultas[turno_enfermero % 2].doctor is not None:
        esta_enfermo, enfermedad = lista_consultas[turno_enfermero % 2].doctor.diagnosticar(
            lista_consultas[turno_enfermero % 2].paciente)
        # Creamos un enfermo (puede ser un cuentista)
        enfermo = Enfermo(enfermedad, lista_consultas[turno_enfermero % 2].paciente.dni,
                          lista_consultas[turno_enfermero % 2].paciente.nombre,
                          lista_consultas[turno_enfermero % 2].paciente.apellido,
                          lista_consultas[turno_enfermero % 2].paciente.sintomas)
        # Aquí decidimos si le mandamos a la habitación, al pasillo o a su casa
        if esta_enfermo and len(enfermos_en_habitacion) < 3:
            print('Dirijase a la habitación, {}. Usted tiene {}.'.format(
                lista_consultas[turno_enfermero % 2].paciente.nombre, enfermedad))
            enfermos_en_habitacion.append(enfermo)
        elif not esta_enfermo:
            print('No me haga perder mi valioso tiempo, {}. Usted tiene {}.'.format(
                lista_consultas[turno_enfermero % 2].paciente.nombre, enfermedad))
        else:
            print(
                '{}, usted tiene {}. Lo siento pero le van a dejar temporalmente el pasillo. Este es el estado de la '
                'sanidad pública en Madrid.'.format(
                    lista_consultas[turno_enfermero % 2].paciente.nombre, enfermedad))
            enfermos_en_pasillo.append(enfermo)
        # Aquí el paciente sale de la consulta
        print(consulta1)
        print(consulta2)
        lista_consultas[turno_enfermero % 2].despachar_paciente()
    else:
        print('La consulta {} está vacía. Llamen a un doctor ahora mismo, el paciente {} le está esperando'.format(
            lista_consultas[turno_enfermero % 2].id_number, lista_consultas[turno_enfermero % 2].paciente.nombre))
    turno_enfermero += 1
    print('========Termina la colsulta===========')
    # print(consulta1)
    # print(consulta2)
    # print(esta_enfermo)
    # print(consulta1)
    # print(consulta2)
    # print(len(sala_espera))
    # print(sala_espera)

consulta1.salir_doctor()
consulta2.salir_doctor()
enfermero1.fichar()
enfermero2.fichar()

print('\nLa sala de espera tiene {} paciente'.format(len(sala_espera)))
print('\nEn la habitación están los siguientes pacientes:')
for enfermo in enfermos_en_habitacion:
    print(enfermo)

if len(enfermos_en_pasillo) > 0:
    print('\nEn el pasillo están los siguientes pacientes:')
    for enfermo in enfermos_en_pasillo:
        print(enfermo)
else:
    print('\nEn el pasillo no hay pacientes')
