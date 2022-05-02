from ViajeroFrecuente import viajerofrecuente
from ManejadorViajero import manejadorviajero


# Listas
#
# En una aerolínea ofrece una promoción a sus viajeros frecuentes que consiste en acumular puntos por los viajes que realizan, pudiendo luego recibir beneficios a través del canje de puntos.
#
# Usted trabaja en el área de sistemas de la aerolínea y le han solicitado la implementación de un sistema capaz de gestionar la promoción. Respetando el siguiente diseño de clase:
#
# Clase viajero frecuente
#
# Atributos: número de viajero, DNI, nombre, apellido y millas acumuladas.
# Métodos:
# a- El constructor.
# b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
# c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
# d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas.
#
# Implemente un programa que:
#
# 1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y almacenarlas en una lista.
#
# 2- Lea por teclado un número de viajero frecuente y presente un menú con las siguientes opciones:
#
# a- Consultar Cantidad de Millas.
#
# b- Acumular Millas.
#
# c- Canjear Millas.
#
# 3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.



#

if __name__ == "__main__":
    mv = manejadorviajero()
    mv.testViajeros()
    print("lista de Viajeros Cargados : \n")
    print(mv)

    a =  viajerofrecuente(18,44808998,"Herman","Soria",11500)
    print("Elija una de estas opciones [elija ""0(cero)"" para terminar]\n ")
    op = str(input("a- Consultar Cantidad de Millas.\nb- Acumular Millas.\nc- Canjear Millas.\n--------------------------------- \n opcion elegida :  "))

    if (type(op)==str):
        a=-1
    while(a==-1):
        while (op !="a" and op!="b" and op!="c"):
            print("----------------------------------")
            print("ERROR - caracter no valido")
            print("Elija una de estas opciones [elija ""0(cero)"" para terminar] ")
            print("a- Consultar Cantidad de Millas.\nb- Acumular Millas.\nc- Canjear Millas.\n---------------------------------\n")
            op = input(" Vuelva a elegir: ")

            if (op =="a"):
                print("Cantidad Total de millas : {}".format(a.cantidadTotaldeMillas()))
            if (op =="b"):
                print("Cantidad de millas Actuales despues de la Suma : {}".format(a.acumularMillas(int(input("Ingrese la cantidad de millas que ha recorrido para acumular : ")))))
            if (op =="c"):
                print("Cantidad de millas actuales despues del Canje : {} ".format(a.canjearMillas(int(input(" Ingrese la cantidad de millas que quiere Canjear : ")))))











'''
    opciones = {
        "a": a.cantidadTotaldeMillas()
        "b": a.acumularMillas(int(input("Ingrese la cantidad de millas nuevas: ")))
        "c": a.canjearMilas()
    }
'''


print("Hola mundo")

