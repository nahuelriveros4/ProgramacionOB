from correo import Email 
from mensaje import imprimir_mensaje

if _name_ == '_main_':

#Ingresar datos por teclado
nombre = input("Ingrese su nombre: ")
idCuenta = input("Ingrese el id de cuenta: ")
dominio = input("Ingrese el dominio: ")
tipoDominio = input("Ingrese el tipo de dominio: ")
contraseña = input("Ingrese la contraseña: ")

# Creación de instancia de la clase Email
email = Email(idCuenta, dominio, tipoDominio, contraseña)

#Imprimir Mensaje
imprimir_mensaje(nombre, email.retornaEmail())

#Modificar contraseña
print("Cambio de contraseña")
contraseña_Actual = input("Ingrese contraseña actual: ")
if   contraseña_Actual == email.contraseña:
     nueva_contraseña = input("Ingrese nueva contraseña: ")
     email.contraseña == nueva_contraseña
     print("Contraseña modificada exitosamente")
else :
     print("Contraseña incorrecta")

#Crear un objeto de clase Email, a partir de una dirección de correo
direccionCorreo = input("Ingrese direccion de correo: ")
email.crearCuenta(direccionCorreo)

# Ingresar dominio e indicar cuantos emeail tienen el mismo domino
dominioBuscar = input("Ingrese dominio a buscar: ")
contador = 0
