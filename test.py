import libreria_complejos as cpmx

#Mostrar Complejos
def printcomplex(c):
    if type(c) == float:
        print(round(c,2))
    else:
        if c[1] < 0:
            return (str(c[0]) + " - " + str(abs(c[1])) + "i")
        else:
            return (str(c[0]) + " + " + str(c[1]) + "i")


def casos_prueba(rest1,ver1,rest2,ver2):
    Passed = 0
    Failed = 0
    if rest1 == ver1:
        Passed+=1
    else:
        Failed+=1
    if rest2 == ver2:
        Passed+=1
    else:
        Failed+=1

    return "De dos casos pruebas:",Passed, "Pasaron con exito y",Failed,"No pasaron" 
  

c1 = (2,5)
c2 = (7,8)
c3 = (-21,15)
c4 = (-2,-2)

#Suma
print("Caso pruebas de Suma")
val1 = cpmx.sumcomplex(c1,c2)
val2 = cpmx.sumcomplex(c3,c4)
print(*casos_prueba(val1,(9,13),val2,(-23,13)))
print()

#Resta
print("Caso pruebas de Resta")
val1 = cpmx.restcomplex(c1,c2)
val2 = cpmx.restcomplex(c3,c4)
print(*casos_prueba(val1,(-5,-3),val2,(-19,17)))
print()

#Multiplicacion
print("Caso pruebas de Multiplicación")
val1 = cpmx.multcomplex(c1,c2)
val2 = cpmx.multcomplex(c3,c4)
print(*casos_prueba(val1,(-26,51),val2,(72,12)))
print()

#División
print("Caso pruebas de la División")
val1 = cpmx.divcomplex(c1,c2)
val2 = cpmx.divcomplex(c3,c4)
print(*casos_prueba(val1,(0.48,0.17),val2,(1.5,-9.0)))
print()

#Modulo
print("Caso pruebas del Modulo")
val1 = cpmx.moducomplex(c1)
val2 = cpmx.moducomplex(c3)
print(*casos_prueba(val1,(5.39),val2,(25.81)))
print()

#Conjugado
print("Caso pruebas del conjugado")
val1 = cpmx.conjucomplex(c1)
val2 = cpmx.conjucomplex(c3)
print(*casos_prueba(val1,(2,-5),val2,(-21,-15)))
print()

#Conversión entre cartesiano y polar
print("Caso pruebas de pasar de Cartesiano a Polar")
val1 = cpmx.cartesian_to_polar_complex(c1)
val2 = cpmx.cartesian_to_polar_complex(c3)
print(*casos_prueba(val1,(5.39,1),val2,(25.81,3)))
print()

#Fase
print("Caso pruebas de Fase")
val1 = cpmx.fasecomplex(c1)
val2 = cpmx.fasecomplex(c3)
print(*casos_prueba(val1,1.19,val2,2.52))
print()