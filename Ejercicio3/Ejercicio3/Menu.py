from ManejadorLista import ManejadorLista


class Menu:

    pass





    def opcion1(self,lista):
        a = ""
        # if type(lista) == ManejadorLista.ManejadorLista:
        print("Ingreso a la opcion 1")
        print(" Datos : Mayor Temperatura : {} ".format(lista.MayorTemperatura))
        b = lista.MayorTemperatura
        print(" print de b : ")
        print(b)

    def opcion2(self):
        b = ""
        print("Ingreso a la opcion 2")
        return b
    def opcion3(self):
        c = ""
        print("Ingreso a la opcion 3")
        return c

    def opcion4(self):
        print("<<<----------------< Fin Programa >---------------->>>")

    def elegirop(self, op, lista):
        if (op==1):
            self.opcion1(lista)
        if (op==2):
            self.opcion2()
        if (op==3):
            self.opcion3()
        if (op==4):
            self.opcion4()
