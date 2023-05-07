from claseviajeroFrecuente import ViajeroFrecuente
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
    
    def almacenMemoria(self):
        print("Representacion del almacenamiento en memoria para la lista cargada con 4 viajeros.")
        for i in range(4):
            viajero= self.__lista[i]
            print(f"Numero: {viajero.getNumero()}\nNombre y Apellido: {viajero.getApellido()} {viajero.getNombre()}\nDNI: {viajero.getDNI()}\nMillas: {viajero.getMillas()}\n")
    
    def mayorCantMillas(self):
        mayor_millas = max(self.__lista)
        mayores_millas=[]
        for viajero in self.__lista:
            if viajero.getMillas()==mayor_millas.getMillas():
                mayores_millas.append(viajero)
        print(f"El/los viajero/s con mayor cantidad de millas acumuladas")
        for viajero in mayores_millas:
            print(f"Nombre: {viajero.getNombre()}")
    
    def sumaMillas(self):
        print(f"\nAcumular millas")
        for viajero in self.__lista:
            viajero=viajero+100
            print(f"Nombre: {viajero.getNombre()}\nMillas: {viajero.getMillas()}")
    
    def restaMillas(self):
        print(f"\nCanjear millas ")
        for viajero in self.__lista:
            viajero=viajero-100
            print(f"Nombre: {viajero.getNombre()}\nMillas: {viajero.getMillas()}")