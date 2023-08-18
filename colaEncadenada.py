class Nodo:
    __item=int
    __sig=None
    def __init__(self, item):
        self.__item=item
        self.__sig=None

    def getValor(self):
        return self.__item
    
    def setSiguiente(self, objeto):
        self.__sig=objeto

    def getSiguiente(self):
        return self.__sig

class cola:
    __pr=None
    __ult=None
    __cant=int
    def __init__(self, cant=0):
        self.__cant=cant

    def vacia(self):
        return self.__cant==0
    
    def insertar(self, item):
        p=Nodo(item)
        if self.__ult == None:
            self.__pr=p
        else:
            self.__ult.setSiguiente(p)
        self.__ult=p
        self.__cant+=1
        return self.__ult.getValor()
        
    def suprimir(self):
        if self.vacia():
            print("Cola Vacia")
        else:
            x=self.__pr.getValor()
            self.__pr=self.__pr.getSiguiente()
            self.__cant-=1
            return x
        
    def recuperarPr(self):
        return self.__pr
    
    def recorrer(self, aux):
        if aux != None:
            print(aux.getValor())
            self.recorrer(aux.getSiguiente())

if __name__=="__main__":
    c=cola(5)
    c.insertar(2)
    c.insertar(5)
    c.insertar(8)
    c.insertar(4)
    c.insertar(5)
    c.recorrer(c.recuperarPr())
    c.suprimir()
    c.suprimir()

    
    print("Lista despues de suprimir")
    c.recorrer(c.recuperarPr())


        
    
               

        
