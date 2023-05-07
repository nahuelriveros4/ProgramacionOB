from clasePlanAhorro import PlanAhorro
import csv 

class lista:
    __lista = []
    def __init__(self):
        self.__lista = []

    def testlista(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            f = fila
            plan = PlanAhorro(f[0], f[1], f[2], f[3])
            self.__lista.append(plan)
        archivo.close()

    
    def Mostrar_menu(self):
        print('a. Actualizar el valor del vehículo de cada plan.')
        print('b. Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor ingresado.')
        print('c. Mostrar el monto que se debe haber pagado para licitar el vehículo.')
        print('d. Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.')
        print('e. Salir')

    def menu(self):
     opc = input('Ingrese una opcion: ')
     while opc != 'e':

        if opc == 'a':
            self.actualizar()
            self.mostrar()
        elif opc == 'b':
            valor = float(input('Ingrese el valor: '))
            self.mostrar_plan_cuota_inf(valor)
        elif opc == 'c':
            cuota = float(input('Ingrese el importe de la cuota: '))
            monto = PlanAhorro.monto_licitacion(cuota)
            print(f'Monto para licitar: {monto}')
        elif opc == 'd':
            cod_plan = input('Ingrese el código del plan: ')
            nuevas_cuotas = int(input('Ingrese la nueva cantidad de cuotas para licitar: '))
            self.modificar_cuotas_licitar(cod_plan, nuevas_cuotas)

        opc = input('Ingrese una opcion: ')
    
    def actualizar(self):
        for plan in self.__lista:
            print(plan)
            nuevo_valor = float(input('Ingrese nuevo valor para modificarlo en el plan: '))
            plan.actualizaValor(nuevo_valor)

    def mostrar_plan_cuota_inf(self, valor):
        for plan in self.__lista:
            if plan.valorCuota() < valor:
                print(plan)

    def modificar_cuotas_licitar(self, cod_plan, nuevas_cuotas):

        i = 0
        while i < len(self.__lista):
            if self.__lista[i].get_cod() == cod_plan:
                self.__lista[i].modificarCant_CuotasPagas(nuevas_cuotas)

            i += 1

    def mostrar(self):
        for plan in self.__lista:
            print(plan)
