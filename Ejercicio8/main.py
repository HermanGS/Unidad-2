import Conjunto

if __name__=="__main__":
    conjunto1=Conjunto.Conjunto()
    conjunto1.test1()
    conjunto2=Conjunto.Conjunto()
    conjunto2.test2()
    print("Conjunto 1:")
    print(conjunto1)
    print("Conjunto 2")
    print(conjunto2)
    print("Union de conjunto 1 y conjunto 2")
    print(conjunto1+conjunto2)
    print("Diferencia entre conjunto 1 y conjunto 2")
    print(conjunto1-conjunto2)
    print("Comparacion entre conjuntos")
    if(conjunto1==conjunto2):
        print("Son iguales")
    else:
        print("Son distintos")
