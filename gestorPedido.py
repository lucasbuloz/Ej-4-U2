from Classpedidos import classped
from gestormoto import gestormotos 
import csv

class gestorpedido:
    _listP:list
    
    def __init__(self):
        self._listP=[]
        
    def leerycargarpedi(self):
        archivo=open("datosPedidos.csv", "r")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            nuevopedido=classped(fila[0],fila[1],fila[2],int (fila[3]),int (fila[4]),float (fila[5]))
            self._listP.append(nuevopedido)
        archivo.close()
        
    def mostrar(self):
        for datosPedidos in self._listP:
            gestorpedido.mostrar()
    
    def ordenado(self):
        self._listP.sort()
        for classped in self._listP:
            classped.mostrarpe()
            
    def asignarmoto(self):
        patente= gestormotos.verificarpatente()
        nuevoid=input('Ingrese identificacion de pedido')
        nuevocom=input('Ingrese comida de pedido')
        nuevotiem=input('Ingrese tiempo de pedido')
        nuevotreal=input('Ingrese tiempo real de pedido')
        nuevopre=input('Ingrese precio de pedido')
        
        nuevopedido=(patente, nuevoid, nuevocom,nuevotiem, nuevotreal, nuevopre)
        self._listP.append(nuevopedido)
        
    """def inciso4(self):
        patente=input('Ingrese patente')
        nid=input('Ingrese nuevo id')
        tireal=input('Ingrese tiempo real')"""
        
    def modTiempoReal(self):
        patente = input("ingrese patente")
        id = input("ingrese id")
        for nuevoPedido in self._listP:
             if (nuevoPedido.id == id) and (nuevoPedido.patenteMoto == patente) :
                 nuevoPedido.tiempoDeEntregaReal = input("ingrese nuevo tiempo real")
                 
    def leerPatente(self):        
        patente = gestormotos.verificarpatente()
    
    def totalprecios(self):
        for i in gestormotos._listM:
            for j in gestorpedido._listP:
                totalprecios = totalprecios + i.precio
        return totalprecios

    def comi(self):
         for i in gestormotos._listM:
            for j in gestorpedido._listP:
              comision= gestorpedido.totalprecios()  
              print(f'patente:{i.patente}, nya: {i.nya}, id: {j.idpe, {j.tiem}, {j.treal},{j.pre}, {comision}}')
              
            