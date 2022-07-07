from ManejadorInfracciones import ManejadorInfracciones
from ManejadorInfractores import ManejadorInfractores



class menu:


    def opcion1(self,MInfractores,MInfracciones):
        
    def opcion2(self,MInfractores,MInfracciones):
        pass
    def opcion3(self,MInfractores,MInfracciones):
        pass
    def opcion4(self,MInfractores,MInfracciones):
        pass
    def opcion5(self,MInfractores,MInfracciones):
        pass

    def MostrarOpciones(self):
        print("a.Formato \nb.InfraccionesImpagas por dni y patente")


    def ChoseOP(self,op,MInfractores,MInfracciones):
        if op == 1:
            self.__opcion1(MInfractores,MInfracciones)
        if op == 2:
            self.__opcion2(MInfractores,MInfracciones)
        if op == 3:
            self.__opcion3(MInfractores,MInfracciones)
        if op == 4:
            self.__opcion4(MInfractores,MInfracciones)
        if op == 5:
            self.__opcion5(MInfractores,MInfracciones)