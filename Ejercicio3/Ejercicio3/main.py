# Ejercicio 3
#  Listas bidimensionales
#
# Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.
#
# Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.
#
# Implemente un programa que:
#
# 1.    Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.
#
# 2.    Almacene en la lista bidimensional los datos registrados en el archivo.
#
# 3.    Presente un menú de opciones permita realizar las siguientes tareas:
#
# 3.1.        Mostrar para cada variable el día y hora de menor y mayor valor.
#
# 3.2.        Indicar la temperatura promedio mensual por cada hora.
#
# 3.3.        Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.

from Registro import Registro
from ManejadorLista import ManejadorLista
from Menu import Menu

if __name__ == "__main__":
    MM = ManejadorLista()

    # TEST temporal
    # dia0 = int(input("Ingrese un ""día"" para modificar temp hum y pre : "))
    # # print(dia0)
    # hora0 = int(input("Ingrese un ""hora"" para modificar temp hum y pre : "))
    # # print(hora0)
    # print("--------------------------------------------")
    # print("Ingreso de datos del Registro Temporal")
    # temp = float(input("ingrese temperatura : "))
    # hum = int(input("ingrese humedad : "))
    # pre = float(input("ingrese presion : "))
    # Registrotemp = Registro(temp, hum, pre)
    # print("Registro cargado: ")
    # print(Registrotemp)
    # MM.AgregarAlaMatriz(dia0, hora0, Registrotemp)

    print("---------------------------------")
    MM.ingresoArchivo()
    print("Ingreso de datos del Archivo : COMPLETADO ")
    print("---------------------------------")
    # MM.PruebaCarga()

    # Menu:
    # #op1
    # print("Del mes : \n La Mayor Temperatura es {}, La Menor Temperatura es {},\n La Mayor Humedad es {}, La Menor Humedad es {},\n La Mayor Presion es {}, La Menor Presion es {}.\n ".format(MM.MayorTemperatura(),MM.MenorTemperatura(),MM.MayorHumedad(),MM.MenorHumedad(),MM.MayorPresion(),MM.MenorPresion() ))
    # #op2
    # MM.PromedioMensualPorHora()
    # #op3
    # dia = int(input("Ingrese el dia, para ver todos los Valores de las Variales Metereologicas por HORA : "))
    # print("Matriz por día : {}".format(dia))
    # print("--------------------------------")
    # MM.MostrarPorDia(dia)

    op = -1
    while op != 4:
        print("1  2  3 o 4 para salir ")
        op = int(input("Elija una Opcion : "))
        print("op : ")
        print(op)
        if (op==1)or(op==2)or(op==3)or(op==4):
            if (op==1):
                print("Del mes : \n La Mayor Temperatura es {}, La Menor Temperatura es {},\n La Mayor Humedad es {}, La Menor Humedad es {},\n La Mayor Presion es {}, La Menor Presion es {}.\n ".format(MM.MayorTemperatura(),MM.MenorTemperatura(),MM.MayorHumedad(),MM.MenorHumedad(),MM.MayorPresion(),MM.MenorPresion() ))
            if (op==2):
                MM.PromedioMensualPorHora()
            if (op==3):
                dia = int(input("Ingrese el dia, para ver todos los Valores de las Variales Metereologicas por HORA : "))
                print("Matriz por día : {}".format(dia))
                print("--------------------------------")
                MM.MostrarPorDia(dia)
            if (op==4):
                print("<<<----------------< Fin Programa >---------------->>>")
        else:
            print("Opcion Equivocada")

        # el Módulo Menu no puede importar bien el módulo ManejadorLista, por esto mismo hago el menu en el main
        # menuOP = Menu()
        # menuOP.elegirop(op, MM)
