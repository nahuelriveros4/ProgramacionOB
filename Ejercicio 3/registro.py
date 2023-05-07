class Registro:
    __temp = float
    __hum = float
    __pres = float

    def __init__(self, temp: float, hum: float, pres:float):
        self.__temp = temp
        self.__hum = hum
        self.__pres = pres

    def __repr__(self)->str:
        return f"{self.__temp, self.__hum, self.__pres}"

    def getTemperatura(self)->float:
        return self.__temp
    
    def getHumedad(self)->float:
        return self.__hum
    
    def getPresion(self)->float:
        return self.__pres