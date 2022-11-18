import test as t

# Creamos a las personas que estarán en el hospital
persona1 = t.Persona('111A', 'Alejandra', 'Sánchez')
doctor1 = t.Doctor('pediatra', persona1.dni, persona1.nombre, persona1.apellido, en_servicio=False)
doctor2 = t.Doctor('familia', '222A', 'Irene', 'Sanz', en_servicio=False)
# print(doctor1)
# print(doctor2)
enfermero1 = t.Enfermero('maxilofacial', '333A', 'Carlos', 'Pérez', False)
enfermero2 = t.Enfermero('urgencias', '444A', 'Álvaro', 'Gómez', False)
# print(enfermero1)
# print(enfermero2)
paciente1 = t.Paciente('555A', 'Paco', 'Saura', ['falta olfato', 'dolor cabeza'])
paciente2 = t.Paciente('666A', 'Marta', 'San Miguel', ['dolor de tobillo', 'inflamación en la zona'])
paciente3 = t.Paciente('777A', 'Lucía', 'Del Romero', ['fiebre', 'diarrea'])
paciente4 = t.Paciente('888A', 'Inma', 'Luque', ['dolor garganta', 'dolor cabeza'])

consulta1 = t.Consulta('1')
consulta2 = t.Consulta('2')
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
        enfermo = t.Enfermo(enfermedad, lista_consultas[turno_enfermero % 2].paciente.dni,
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
