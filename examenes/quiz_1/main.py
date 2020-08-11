import fibonacci
import time


inicio = time.time()
fibonacci.caso1 (27)
tiempo_caso_1= time.time()-inicio

inicio = time.time()
fibonacci.caso2(27)
tiempo_caso_2= time.time()-inicio

if tiempo_caso_1>tiempo_caso_2:
    print("Es mas rapido el caso 2")
else:
    print("Es mas rapido el caso1")