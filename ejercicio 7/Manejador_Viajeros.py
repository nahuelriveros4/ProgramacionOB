from Viajero_Frecuente import ViajeroFrecuente
import csv

class lista:
    __lista=[]
    def __init__(self):
        self.__lista = []

    def test(self):
        archivo=open("viajeros.csv")
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            num_viajero = int(fila[0])
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millas_acum = int(fila[4])
            viajero = ViajeroFrecuente(num_viajero, dni, nombre, apellido, millas_acum)
            self.__lista.append(viajero)
        archivo.close()

    def numViajero(self):
        numero=int(input("Ingresar un numero de viajero frecuente: "))
        viaj=False
        for objeto in self.__lista:
            if  objeto.getNumero() == numero:
                viaj= objeto
        return viaj
    
    def sumaMillas(self):
        print(f"\nAcumular millas")
        for viajero in self.__lista:
            viajero=100+viajero
            print(f"Nombre: {viajero.getNombre()}\nMillas: {viajero.getMillas()}")
    
    def restaMillas(self):
        print(f"\nCanjear millas ")
        for viajero in self.__lista:
            viajero=100-viajero
            print(f"Nombre: {viajero.getNombre()}\nMillas: {viajero.getMillas()}")
    
    def compararMillas(self):
        print(f"\nComparar millas ")
        for viajero in self.__lista:
            if 100==viajero or viajero==100:
                print(f"Nombre: {viajero.getNombre()}\nMillas: {viajero.getMillas()}")
