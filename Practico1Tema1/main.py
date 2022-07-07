from ManejadorPersonal import ManejadorPersonal
from ManejadorNovedades import ManejadorNovedades
from menu import menu


if __name__ == '__main__':
    print("Hola gente de youtube")

    MP = ManejadorPersonal()
    
    MN = ManejadorNovedades()

    MP.Ingresar_Personal_Archivo()

    MN.Ingresar_Novedades_Archivo(MP)

    print("--------------------------------")
    MP.MostrarArregloPersonal()
    print("--------------------------------")
    MN.MostrarListaNovedades()
    
    MP.Ordenamiento3()
    print("--------------------------------")
    MP.MostrarArregloPersonal()


    menuc = menu()

    marcelo= "xd"    

    op = -1
    while op != 4 :
        menuc.MostrarInfo()
        print("\n")
        op = int(input("Ingrese la opcion elegida : ")) 
        while op>3 or op<1:
            menuc.MostrarInfo()
            print("\n")
            print("ERROR - Vuelva a ingresar la opcion")
            op = int(input("Ingrese la opcion elegida : "))
        menuc.choseOP(op,MP,MN)