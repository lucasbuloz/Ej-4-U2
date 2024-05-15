from gestormoto import gestormotos as m
from gestorPedido import gestorpedido as p

def testea():
    while True:
        print('----------Menu de opciones----------')
        print('1, cargar motos y pedidos')
        print('2, asignar pedido')
        print('3, modificar tiempo real')
        print('4, datos del conductor y promedio')
        print('5, listado de motos')
        
        opcion= input('Ingrese ocpion')
        
        if opcion == "1":
            m.leerycargar()
            p.leerycargarpedi()
        elif opcion =='2':
            p.asignarmoto()
        elif opcion == '3':
            p.modTiempoReal()
            p.leerPatente()
        elif opcion == '4':
            m.penultimo
            
        elif opcion == '5':
            p.comi()