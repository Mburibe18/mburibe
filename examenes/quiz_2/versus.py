import burbuja
import insercion
import time
import mezcla
import random
def line_design():
  print ('#'*30)
size_list= int (input("Ingrese tamaño de la lista : "))
lista = [random.randint(300,1230) for i in range(size_list)]

lista_desordenada = lista
line_design()
print("se muestra la lista desordenada")
print(lista_desordenada)
line_design()
lista_desordenada_2 = lista
lista_desordenada_3 = lista
inicio = time.time()
burbuja.ordenamiento_burbuja(lista)
final_burbuja = time.time()-inicio

inicio = time.time()
insercion.ordenamiento_por_insercion(lista_desordenada)
final_insercion = time.time()-inicio


inicio = time.time()
mezcla.ord_por_mezcla(lista_desordenada_2)
final_mezcla = time.time()-inicio

line_design()
print("se muestra la lista ordenada")
print(lista_desordenada)
line_design()

print(f"el tiempo fina de borbuja es {final_burbuja} y el de insercion {final_insercion} y el tiempo final de mezcla {final_mezcla}")
line_design()

print("el metodo mas efectivo es el de insercion")