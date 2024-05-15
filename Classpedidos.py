class classped:
    _patpe:str
    _idpe:str
    _comid:str
    _tiem:int
    _treal:int
    _pre:float
    
    def __init__(self, patpe,idpe,comid,tiem,treal,pre):
        self._patpe=patpe
        self._idpe=idpe
        self._comid=comid
        self._tiem=tiem
        self._treal=treal
        self._pre=pre
    
    def getpatente(self):
        return self._patpe
    
    def mostrarpe(self):
        print('patente{}, Id{}, Comidas Pedidas {}, Tiempo de Entrega {}, Tiempo Real {}, Precio del Pedido {}'.format(self._patpe, self._idpe, self._comid, self._tiem, self._treal, self._pre))
        
    def getid(self):
        return self._idpe

    def __lt__(self,other):
        return (self._patpe < other.getpatente())
        
    