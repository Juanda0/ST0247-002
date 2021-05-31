import GraphAM as gAM
import lector as lt
import vehicleRouting as vr
import random
from memory_profiler import memory_usage
import time
import pandas as pd

#Datasets/tc2c320s24cf0.txt
#Datasets/tc2c320s24cf1.txt
#Datasets/tc2c320s24cf4.txt
#Datasets/tc2c320s24ct0.txt
#Datasets/tc2c320s24ct1.txt
#Datasets/tc2c320s24ct4.txt
#Datasets/tc2c320s38cf0.txt
#Datasets/tc2c320s38cf1.txt
#Datasets/tc2c320s38cf4.txt
#Datasets/tc2c320s38ct0.txt
#Datasets/tc2c320s38ct1.txt
#Datasets/tc2c320s38ct4.txt
#Datasets/dummy.txt
class main: 
  def main():
    grafo = lt.lector.crearGrafoTxt('Datasets/tc2c320s38ct4.txt')
    #bestPath = aux.vehicleRouting()
    bestRoute = None
    bestPath = None
    bestPathTime = float("inf")
    bestPathSeed = None
    bestVC = 0
    fails = 0
    for i in range(1):
        if i % 10 == 0:
          print(i)

        aux = vr.vehicleRouting(grafo, k = 1, b = 50)
        try:
          
          path = aux.vehicleRouting()
          pathTime = path[1]
        except Exception as e:
          print(e)
          fails += 1
          pathTime = None
        

        if pathTime is not None and sum(pathTime) < bestPathTime:
            bestRoute = aux
            bestPath = path
            bestPathTime = sum(pathTime)

    times = bestPath[1]
    paths = bestPath[0]
    batterys = bestPath[2]

    times = bestPath[1]
    paths = bestPath[0]
    batterys = bestPath[2]

    colors = []
    for i in range(40):
      colors.append(gAM.GraphAM.rand_web_color_hex())

    print(f'cantidad rutas: {len(paths)}\nTiempo de rutas: {sum(times)}\n')
    print(f'Parametros: {bestRoute.getParameters()}')
    grafo.showGraph(paths,colors, mode = 'Paths')  
    
if __name__ == "__main__":
  main.main()
