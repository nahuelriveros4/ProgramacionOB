class Email:
    def __init__(self, idCuenta, dominio, tipoDominio, contraseña):
        self.idCuenta = idCuenta
        self.dominio = dominio
        self.tipoDominio = tipoDominio
        self.contraseña = contraseña

    def retornaEmail(self):
        return f"{self.idCuenta}@{self.dominio}.{self.tipoDominio}"
    
    def getDominio(self):
        return self.dominio
    
    @classmethod
    
    def crearCuenta(self, direccionCorreo):
        partes = direccionCorreo.split("@")
        if len(partes) == 2:
            idCuenta = partes[0]
            dominio_tipoDominio = partes[1]
            dominio, tipoDominio = dominio_tipoDominio.split(".")
            contraseña = input("Ingrese contraseña: ")
            self.idCuenta = idCuenta
            self.dominio = dominio
            self.tipoDominio = tipoDominio
            self.contraseña = contraseña
            print("Cuenta creada correctamente")
        else: 
            print("Direccion de correo incorrecta")
        
    

