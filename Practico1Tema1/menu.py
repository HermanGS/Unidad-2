from re import M
from ManejadorNovedades import ManejadorNovedades
from ManejadorPersonal import ManejadorPersonal


class menu:


    def __init__(self) -> None:
        pass




    def MostrarInfo(self):
        print("1. Dado el número de legajo de una persona, obtener el sueldo a liquidar (sueldo básico más los adicionales, menos los descuentos). \n2. Obtener un listado con el siguiente formato ordenado alfabéticamente por nombre y apellido, para efectivizar el ordenamiento, debe sobrecargar el operador  gt en la clase que corresponda \n3.Persona con menor sueldo \n4.Salir")
                   
    def opcion1(self,MP,MN):
        print("Ingreso Opcion 1")

        legajo = int(input("Ingrese el legajo para calcular el 'sueldo a Liquidar' :  "))
        sueldo = MP.ObtenerSueldoPorLegajo(legajo)
        if sueldo == None:
            print("No se encontro el legajo buscado")
        else:
            Sumatoria = MN.SumatoriaLiquidar(legajo,sueldo)
            print("La Sumatoria A Liquidar del Personal con Legajo :",legajo," es :",Sumatoria," .")

    def opcion2(self,MP,MN):
        print("Ingreso Opcion 2")

        print("Listado Ordenado Por Nombre")
        print("\n")
        MN.Listado(MP)

        # MP.MostrarArregloPersonal()





    def opcion3(self,MP,MN):
        minimo = MP.Minimo()
        print("El personal con Menor sueldo es ",minimo)
        

    def opcion4(self):
        print("<<< Fin Programa >>>")

    def choseOP(self,op,MP,MN):
        
        if op == 1:
            self.opcion1(MP,MN)
        if op == 2:
            self.opcion2(MP,MN)
        if op == 3:
            self.opcion3(MP,MN)    