import GraphAM as gAM
import lector as lt
import vehicleRouting as vr
import random

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
    
    grafo = lt.lector.crearGrafoTxt("Datasets/tc2c320s38ct0.txt")

    
    #bestPath = aux.vehicleRouting()
    bestRoute = None
    bestPath = None
    bestPathTime = float("inf")
    bestPathSeed = None
    bestVC = 0

    for i in range(1):
        aux = vr.vehicleRouting(grafo, k = 1, b = 60)
        print(i)
        path = aux.vehicleRouting()
        pathTime = path[1]
        visitedClients = len(gAM.GraphAM.flatten(path[0]))
        if visitedClients > bestVC:
            bestRoute = aux
            bestPath = path
            bestPathTime = sum(pathTime)
            bestPathSeed = aux.seed
            bestVC = visitedClients
        elif visitedClients == bestVC and sum(pathTime) < bestPathTime:
            bestRoute = aux
            bestPath = path
            bestPathTime = sum(pathTime)
            bestPathSeed = aux.seed
    """
    grafo = lt.lector.crearGrafoTxt("Datasets/tc2c320s38ct4.txt")
    aux = vr.vehicleRouting(grafo)
    bestPath = aux.vehicleRouting(seed = 7360069244080628934)
    """
    times = bestPath[1]
    paths = bestPath[0]
    batterys = bestPath[2]

    times = bestPath[1]
    paths = bestPath[0]
    batterys = bestPath[2]

    colors = []
    for i in range(40):
      colors.append(gAM.GraphAM.rand_web_color_hex())

    print(f"Seed: {aux.seed}")
    print('Tiempo de rutas',sum(times))
    print(batterys)
    print(bestRoute.getParameters())
    grafo.showGraph(paths,colors, mode = 'Paths')  


if __name__ == "__main__":
  main.main()
