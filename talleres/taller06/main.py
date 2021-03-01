
import csv
import sys
class main:
  def main():
    a = lector.crearGrafoTxt("puentesColgantes.txt")
    bestPath = a.getBestWayOnceGreedy("10000")
    print(f"El mejor camino es {bestPath[0]} y tiene una distancia de {bestPath[1]}")

  def devolverCambio(cantidad, monedas):
    monedas.sort(reverse = True)
    cambio = {}
    for i in monedas:
      cambio[i] = 0
    for i in monedas:
      while cantidad > 0:
        if cantidad - i >= 0:
          cantidad -= i
          cambio[i] += 1
        else:
          break

    for coin in cambio.keys():
      if cambio[coin] > 0:
        print(f"Se requiere {cambio[coin]} monedas de {coin}")

    

class lector:
  def crearGrafoTxt(archivo):		
    my_file = archivo
    csv.register_dialect('skip_space', skipinitialspace=True)
    with open(my_file, 'r') as f:
      next(f)
      reader=csv.reader(f , delimiter=' ', dialect='skip_space')
      arcs = [[], [], []]
      for item in reader:
        arcs[0].append(item[0]) 
        arcs[1].append(item[1])
        arcs[2].append(item[2]) 
    
    vertices = list(set(arcs[0])) + list(set(arcs[1]) - set(arcs[0]))
    a = GraphAl(len(vertices))
    a.nombrarVertices(vertices)
  
    for i in range(len(arcs[0])):
      sourceNode = arcs[0][i]
      destinationNode = arcs[1][i]
      weight = float(arcs[2][i])
      a.addArc(sourceNode, destinationNode, weight)

    return a

class GraphAl:
  def __init__(self, size):
    self.size = size
    self.lista = [[] for i in range(size)]
    self.nombresVertices = []
    for i in range(len(self.lista)):
      self.nombresVertices.append(i)

  def getWeight(self, sourceNode, destinationNode):
    source = self.nombresVertices.index(sourceNode)
    destination = self.nombresVertices.index(destinationNode)
    for d in self.lista[source]:
      if d[0] == destination:
        return d[1]
    return -1
  
  def nombrarVertices(self, nombresVertices):
    if len(nombresVertices) == len(self.lista):
      self.nombresVertices = nombresVertices
    else:
      print("Los nombres exceden el tamaño de la lista")

  def addArc(self, sourceNode, destinationNode, weight = 1):
    source = self.nombresVertices.index(sourceNode)
    destination = self.nombresVertices.index(destinationNode)
    self.lista[source].append((destination, weight))

  def getSuccessors(self, vertice):
    succs = []
    for d in self.lista[vertice]:
      succs.append(d[0])
    return succs

  def getEdges(self):
    print("digraph Matriz {")
    i = 0
    for j in self.lista:
      try:
        a = '\"' + str(self.nombresVertices[i]) + '\"'
        b = '\"' + str(self.nombresVertices[j[0][0]]) + '\"'
        print("  " + a + ' -> ' + b )         
        i += 1
      except:
        break
    print("}")

  def wlist(self):
    for i in self.lista:
      print(i)

  def distancePath(self, path):
    distance = 0
    for i in range(0, len(path)-1):
      distance += self.getWeight(path[i], path[i+1])
    return distance 
  
  def getBestWayOnceGreedy(self, sourceNode):
    None

if __name__ == "__main__":
  main.devolverCambio(1013, [5,10,20,1])