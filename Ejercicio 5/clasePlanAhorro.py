class PlanAhorro:
    __codigoP = ''
    __modelo = ''
    __version = ''
    __valorVehiculo = ''
    __cantidadCuotas_plan: int = 60
    __cantidadCuotas_pagas: int = 10

    def __init__(self , codigo, modelo, version, valorvehiculo):
        self.__codigoP = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valorVehiculo = valorvehiculo

    def __str__(self) -> str:
        return f"{self.__codigoP, self.__modelo, self.__version, self.__valorVehiculo}"

    def valorCuota (self):
        return (float(self.__valorVehiculo) / 60) + float(self.__valorVehiculo)*0.10

    def actualizaValor(self, nuevoValor):
        self.__valorVehiculo= nuevoValor
    
    @staticmethod
    def monto_licitacion(importe_cuota):
        return PlanAhorro.__cantidadCuotas_pagas * importe_cuota

    def get_cod(self):
        return self.__codigoP

    def modificarCant_CuotasPagas(self, nuevas_cuotas):
        self.__cantidadCuotas_pagas = nuevas_cuotas



        

