class Nodo:
    __item=None
    __siguiente=None
    def __init__(self):
        self.__item=None
        self.__siguiente=None
    def obtenerItem(self):
        return self.__item
    def obtenerSiguiente(self):
        return self.__siguiente
    def cargarItem(self,x):
        self.__item=x
    def cargarSiguiente(self,siguiente):
        self.__siguiente=siguiente

class PilaEncadenada:
    __tope=None
    __cantidad=0
    def __init__(self):
        self.__tope=None
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def getValorTope(self):
      return self.__tope.obtenerItem()
    def getCantidad(self):
      return self.__cantidad
    def insertar(self,x):
        nodo=Nodo()
        nodo.cargarItem(x)
        nodo.cargarSiguiente(self.__tope)
        self.__tope=nodo
        self.__cantidad+=1
        return nodo
    def suprimir(self):
        x=None
        if self.vacia():
            print('Pila vacia.')
        else:
            x=self.__tope.obtenerItem()
            self.__tope=self.__tope.obtenerSiguiente()
            self.__cantidad-=1
        return x
    def mostrar(self):
        if self.vacia():
            print('Pila Vacia')
        else:
            aux=self.__tope
            while aux!=None:
                print(aux.obtenerItem())
                aux=aux.obtenerSiguiente()
    def dibujar(self,x=-100,y=-72):
      if not self.vacia():
        aux=self.__tope
        y+=(self.__cantidad-1)*16
        while aux!=None:
          screen.drawSprite(str(aux.obtenerItem()+1),x,y)
          y-=16
          aux=aux.obtenerSiguiente()
    def vaciar(self):
      while self.__cantidad>0:
        self.suprimir()
        