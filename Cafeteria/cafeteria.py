
import random
#"""import logging, ABC (clases abstractas y todo el tema)"""

#log.crear archivo con las excepciones

class CupOfCoffee:

    def __init__(self, type_of_coffee, temperature = 30):
        self.temperature = temperature
        self.type_of_coffee = type_of_coffee

class Client:

    def __init__(self, name):
        self.name = name

    def drink_coffee(self, coffee):
        #log.info se está bebiendo la taza
        if coffee.temperature < 20:
            pass#log.info el cliente dice que está fría
            #raise TooCold...('Café muy frío')
        elif coffee.temperature > 80:
            pass#log.info el cliente dice que está caliente
            #raise TooHot...('Café muy frío')

    def cool_coffee(self, coffee):
        pass #la idea es enfriar el café un poco

class Camarero():

    def __init__(self, nombre):
        self.nombre = nombre

    def prepare_coffee(self):
        pass
        #log.info el camarero está poniendo el café
        #type_of_coffee = input('¿Qué tipo de café quiere, señor?')
        #temperature = random.uniform(0, 100)
        #taza_cafe = CupOfCoffee(input('¿Qué tipo de café quiere, señor?'), random.uniform(0, 100))
        #log.debug información sobre la taza de café
        #return taza_cafe

class Bar:

    def __init__(self, waiter):
        self.waiter = waiter

    #def add_client(self, client):
     #   self.client.append(client)

    def atender_cliente(self, cliente):
        pass#taza_cafe = self.camarero.prepare_coffee()
        #try:
         #   cliente.tomar_taza(taza_cafe)
        #except TooHot as TH:
            #log.error TH.messahe
            #log.error sopla
        # except TooCold as TC:
            # log.error TC.message
            # log.error el camarero le calienta el café
        #except Exception as e:
            #pass
            #log.error algo pasa
        #else:
            #log.info el cliente se lo toma agusto a x grados


if __name__ == "__main__":
    pass
    #cliente =  Cliente('Maria_cliente')
    #camarero = Camarero('Diego_camarero')
    #bar = Bar(cliente, cmarero)
    #bar.atender_cliente(cliente)