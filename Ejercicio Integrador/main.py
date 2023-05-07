from manejadorAlumnos import Manejador_Alumno
from manejadorMaterias import Manejador_Materias
from claseMenu import Menu

if __name__=="__main__":
    arreglo=Manejador_Alumno.inicializar()
    manejadorAlumno=Manejador_Alumno(arreglo)
    #print("\n")
    lista=Manejador_Materias.inicializar()
    manejadorMateria=Manejador_Materias(lista)
    
    Menu(manejadorMateria,manejadorAlumno)
    
 