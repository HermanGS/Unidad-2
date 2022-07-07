

from ManejadorInfractores import ManejadorInfractores
from ManejadorInfracciones import ManejadorInfracciones

if __name__ == '__main__':


    MInfractores = ManejadorInfractores()

    MInfracciones = ManejadorInfracciones()


    MInfractores.IngresoArchivo()
    
    MInfracciones.IngresoArchivo(MInfractores)

    print("--------------------------------------------------------------")
    MInfractores.MostrarLista()


    print("--------------------------------------------------------------")
    MInfracciones.MostrarArreglo()

    print("--------------------------------------------------------------")
    print("<<< Descuento Puntos >>>")
    MInfractores.DescuentoPuntos(MInfracciones)
    MInfractores.MostrarLista()
    print("--------------------------------------------------------------")

    MInfractores.Formato2(21111222,MInfracciones)
    print("--------------------------------------------------------------")
    
