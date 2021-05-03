input("Escribe el nombre del docente: ")


canalizacion = """
Consideraciones para canalizar alumnos a USAER.

1-No termina las actividades a tiempo.
2-No presta atención en clases.
3-Es indisciplinado.
4-No obedece las instruciones que se le dan.
5-No sigue instrucciones.
6-Requiere apoyo para leer y escribir.
7-Utiliza groserías en el aula.
8-Cuando se le cuestiona, sus respuestas son incongruentes.
9-Utiliza un lenguaje infantilizado.
10-Se aisla, prefiere no participar en clase. 

Elige uno o más números, no olvides separarlos por ,: """

opcion = input(canalizacion)

if opcion == "1":
    print("""Se puede fraccionar la actividad de tal manera que las termine en 2 sesiones,
    eso permitirá respetar su ritmo de aprendizaje. Tomar solamente este aspecto no basta
    para canalizar a un alumno al servicio de educación especial. Prueba con más opciones.
    """)
elif opcion == "2":
    print("""Revisa dónde está ubicado el alumno en el salón, si está cerca de las ventanas
    o puerta, puede que eso le genere distracciones. Si esta no es la causa, considera este
    punto y otros más tener un panorama más amplio.
    """)
elif opcion == "3":
    print("""La indisciplina en sí no es determinante para canalizar a alumnos a los servicios
    de educación especial. Prueba con otras opciones. 
    """)
elif opcion == "4":
    print("No es un aspecto para canalizar a USAER. Prueba con otras opciones, ándale")

elif opcion == "5":
    print("Prueba con otra opcion")

elif opcion == "1,2,5,6":
    print("El alumno será evaluado por USAER")

else:
    print("Elige una opción correcta")
    opcion = input(canalizacion)




