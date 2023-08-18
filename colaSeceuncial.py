import numpy as np

class Cola:
    __items=[]
    __pr=0
    __ult=0
    __cant=0
    __max=0
    def __init__(self, max):
        self.__max=max
        self.__pr=0
        self.__ult=0
        self.__cant=0
        self.__items=np.empty(max)

    def vacia(self):
        return self.__cant==0
    
    def lleno(self):
        return self.__cant==self.__max

    def insertar(self, objeto):
        if not self.lleno():
            self.__items[self.__ult]=objeto
            self.__ult= (self.__ult+1) % self.__max
            self.__cant+=1
            return objeto
        else:
            print("La Cola esta llena")
        
    def suprimir(self):
        if self.vacia():
            print("La Cola esta vacia")
        else:
            x=self.__items[self.__pr]
            self.__pr=(self.__pr+1)%self.__max
            self.__cant-=1
            return x
        
    def recorrer(self):
        if not self.vacia():
            i=self.__pr
            for j in range(self.__cant):
                print(self.__items[i])
                i= (i+1) % self.__max
        
if __name__ == "__main__":
    cola=Cola(5)
    cola.insertar(2)
    cola.insertar(5)
    cola.insertar(8)
    cola.insertar(4)
    cola.insertar(5)
    cola.insertar(6)
    cola.recorrer()
    cola.suprimir()
    cola.suprimir()
    
    print("Lista despues de suprimir")
    cola.recorrer()
