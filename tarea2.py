
class NodoCircular:
    def __init__(self,dato):
        self.dato=dato
        self.sig=None
        self.prev=None

class ListaDobleCircular:
    def __init__(self):
        self.cabeza=None
        self.ultimo=None
    def insertar(self,dato):
        nuevo_c= NodoCircular(dato)
        if self.cabeza==None:
            self.cabeza=self.ultimo=nuevo_c
        else:
            nuevo_c.prev=self.ultimo
            nuevo_c.sig=self.cabeza
            self.ultimo.sig=nuevo_c
            self.ultimo=nuevo_c
            self.cabeza.prev=self.ultimo

    def recorrer(self):
        temp=self.cabeza
        while temp is not None:
            print(temp.dato)
            if temp.sig==self.cabeza:
                return
            temp=temp.sig
    def buscar(self,dato):
        temp=self.cabeza
        while temp is not None:
            if temp.dato==dato:
                print(f'anterior:{temp.prev.dato} actual:{temp.dato} siguiente:{temp.sig.dato}')
                #print(temp.dato)
            if temp.sig==self.cabeza:
                return
            temp=temp.sig
listacircular=ListaDobleCircular()
if __name__ == "__main__":
    listacircular.insertar(22)
    listacircular.insertar(44)
    listacircular.insertar(15)
    listacircular.insertar(18)
    listacircular.insertar(111)
    listacircular.recorrer()
    datob=input('Seleccione numero:')
    listacircular.buscar(int(datob))
