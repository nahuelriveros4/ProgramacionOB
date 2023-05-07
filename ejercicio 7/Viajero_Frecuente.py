class ViajeroFrecuente:
    __num_viajero= int
    __dni= ""
    __nombre=""
    __apellido=""
    __millas_acum=int
    
    def __init__(self, num, xdni,xnombre, xapellido, xmillas):
        self.__num_viajero= num
        self.__dni=xdni
        self.__nombre=xnombre
        self.__apellido=xapellido
        self.__millas_acum = xmillas

    def getMillas(self):
        return self.__millas_acum

    def acumularMillas(self, millas_reco):
        self.__millas_acum+=millas_reco
        return self.__millas_acum

    def canjearMillas(self, millas_canjear):
        if millas_canjear <= self.__millas_acum:
            self.__millas_acum-=millas_canjear
            return self.__millas_acum
    
    def __gt__(self, otro):
        return self.getMillas()>otro.getMillas()
    
    def __radd__(self, millas):
        self.acumularMillas(millas)
        return self
    
    def __rsub__(self, millas):
        self.canjearMillas(millas)
        return self
    
    def __eq__(self, millas):
        return self.getMillas() == millas
    
    def getNumero(self):
        return self.__num_viajero
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
