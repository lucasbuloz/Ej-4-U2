from ClassMoto import moto
from gestorPedido import gestorpedido
import csv

class gestormotos:
    _listM:list
    
    def __init__(self):
        self._listM=[]
        
    def leerycargar(self):
        archivo=open ("datosMotos.csv")
        reader=csv.reader(archivo, delimiter=';')
        for fila in reader:
            nuevamoto=moto(fila[0],fila[1],fila[2],float(fila[3]))
            self._listM.append(nuevamoto)
        archivo.close()
    
    def mostrar(self):
        for moto in self._listM:
            moto.mostrarmoto()
            
    def verificarpatente(self):
        patente=input('Ingrese patente')
        for i in self._listP:
            if (i.patente==patente):
                return patente
    
    def penultimo(self):
        totaltiempo=0
        cantped=0
        pat=input('Ingrese patente')
        for i in gestorpedido._listP:
            if i._patente==pat:
                totaltiempo+=i.treal
                cantped+=1
            if cantped>0:
                prom=totaltiempo/cantped
                for j in self._listM:
                    if j.patente == pat:
                        conductor=j.nya
                    break
                print(f'conductor:{conductor}')
                print(f'Tiempo promedio de entrega: {prom}minutos')
            else:
                print('No se econtraron pedidos para esa moto')
                    
                    