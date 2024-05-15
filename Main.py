"""La empresa “RapiPedido”, lo contrata para desarrollar un sistema que debe procesar los
pedidos que llevan las motos que dispone para el delibery de comida.
Cada moto registra: patente, marca, nombre y apellido del conductor, kilometraje.
De cada pedido se registran: patente de la moto que lo tuvo asignado, identificador de
pedido, comidas pedidas, tiempo estimado de entrega (en minutos), tiempo real de entrega
(se inicializa en cero), precio del pedido.
El sistema debe proveer un menú de opciones que permita:
1. Leer los datos de las motos, desde un archivo denominado “datosMotos.csv” y cargarlos
en un Gestor de Motos.
2. Leer los datos de los pedidos, desde un archivo denominado “datosPedidos.csv”, y
cargarlos en el Gestor de Pedidos.
3. Cargar nuevos pedidos, leer los datos por teclado, y asignar a una moto el pedido, al
solicitar la patente de la moto para asignarla, validar que la moto existe.
4. Leer por teclado número de patente, identificador de pedido, y tiempo real de entrega,
modificar en el Gestor de Pedidos, el tiempo real de entrega para ese pedido.
4. Leer por una patente de una moto, mostrar los datos del conductor y el tiempo promedio
real de entrega de los pedidos que hizo.
5. Generar un listado para cada moto, para el pago de comisiones a los conductores de las
motos: """

from Teste import testea
if __name__=="__main__":
     testea()