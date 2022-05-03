from ViajeroFrecuente import Viajerofrecuente
from ManejadorViajero import manejadorviajero
from Menu import Menu

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

if __name__ == "__main__":
    mv = manejadorviajero()
    mv.testViajeros()
    print("lista de Viajeros Cargados : \n")
    print(mv)
    print(mv.retornaViajeroDeLista(0))

    # a =  viajerofrecuente(18,44808998,"Herman","Soria",11500)
    NumViajero = int(input("Ingrese el numero del viajero para realizar las operaciones: "))
    print("\n")
    indice = mv.BuscarViajero(NumViajero)
    if (indice != None):
        menuviajero = Menu()

        op = -1
        while(op != 4):
            print("Elija una de estas opciones [elija ""4(cuatro)"" para terminar] ")
            op = int(input("1 -Consultar Cantidad de Millas.\n2 -Acumular Millas.\n3 -Canjear Millas.\n--------------------------------- \n opcion elegida :  "))
             # print( " la opcion elegida es {}".format(op))
            while(op!= 1 and op!= 2 and op!= 3 and op!= 4 ):
                print("Error - Vuelva a elegir opcion" "\n")
                op = int(input("1 -Consultar Cantidad de Millas.\n2 -Acumular Millas.\n3 -Canjear Millas.\n--------------------------------- \n opcion elegida :  "))
            print("resumen Actual: {} \n ".format(mv.retornaViajeroDeLista(indice)))
            menuviajero.opcion(op,mv.retornaViajeroDeLista(indice))

    else:
        print("No se encontro el viajero con numero {}".format(NumViajero))




