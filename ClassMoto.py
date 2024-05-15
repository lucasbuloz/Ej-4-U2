import numpy as np
class moto:
    _patente:str
    _marca:str
    _nya:str
    _km:float
    
    def __init__(self, patente,marca,nya,km):
        self._patente=patente
        self._marca=marca
        self._nya=nya
        self._km=km
    
    
    def getpatente(self):
        return self._patente
    
    def mostrarmoto(self):
       print('Patente {} Marca {} Nombre y Apellido del Conductor {} Kilometraje {}'.format(self._patente,self._marca,self._nya,self._km))
    
    def getNya(self):
        return self._nya
    
    