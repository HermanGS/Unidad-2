class Conjunto:
    def __init__(self):
        self.__Numeros=[]
    def Agregarelemento(self, numero):
        if (type(numero)==int): 
            self.__Numeros.append(numero)
    def __str__(self):
        return("{}".format(self.__Numeros))
    def test1(self):
        self.Agregarelemento(1)
        self.Agregarelemento(2)
        self.Agregarelemento(3)
        self.Agregarelemento(4)
        self.Agregarelemento(5)
    def test2(self):
        self.Agregarelemento(1)
        self.Agregarelemento(3)
        self.Agregarelemento(6)
        self.Agregarelemento(9)
        self.Agregarelemento(4)
    def QuitarRepetidos(self):
        for i in range(len(self.__Numeros)-1):
            j=i+1
            while (j<len(self.__Numeros)):
                if self.__Numeros[i]==self.__Numeros[j]:
                    self.__Numeros.pop(j)
                j=j+1
    def __add__(self, otro):
        resultado=None
        if type(otro)==type(self):
            Union=Conjunto()
            for i in self.__Numeros:
                Union.Agregarelemento(i)
            for j in otro.__Numeros:
                Union.Agregarelemento(j)
            Union.QuitarRepetidos()
            resultado=Union
        else:
            print("Tipo de dato no valido")
        return(resultado)
    def __sub__(self, otro):
        resultado=None
        if type(otro)==type(self):
            Interseccion=Conjunto()
            for i in range(len(self.__Numeros)):
                j=0
                while ((j<len(otro.__Numeros)) and (self.__Numeros[i]!=otro.__Numeros[j])):
                    j+=1
                if j>=len(otro.__Numeros):
                    Interseccion.Agregarelemento(self.__Numeros[i])
            resultado=Interseccion
        else:
            print("Tipo de dato no valido")
        return(resultado)
    def __eq__(self, otro):
        bandera=False
        if (len(self.__Numeros)==len(otro.__Numeros)):
            bandera=True
            i=0
            while (i<len(otro.__Numeros) and (bandera==True)):
                j=0
                while (j<len(otro.__Numeros) and (self.__Numeros[i]!=otro.__Numeros[j])):
                    j+=1
                if j>=len(otro.__Numeros):
                    bandera=False
                i+=1
        return(bandera)  
