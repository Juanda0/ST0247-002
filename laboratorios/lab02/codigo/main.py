import csv
import sys
class main:
  def main():
    a = lector.crearGrafoTxt("puentesColgantes.txt")
    bestPath = a.getBestWayOnce("10000")
    print(f"El mejor camino es {bestPath[0]} y tiene una distancia de {bestPath[1]}")

    

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
  
  def getBestWayOnce(self, sourceNode):
    others = self.nombresVertices.copy()
    paths = []
    self.permutaciones(sourceNode,paths, others)
    bestPathDistance = sys.maxsize
    bestPath = []
    distance = 0
    for i in paths:
      if self.getWeight(i[len(i)-1], sourceNode) == -1:
        continue
      i.append(sourceNode)
      distance = self.distancePath(i)
      if distance < bestPathDistance:
        bestPath = i
        bestPathDistance = distance
    return (bestPath,bestPathDistance)


  def permutaciones(self, sourceNode,paths, others, path = []):
    path.append(sourceNode)
    try:
      others.remove(sourceNode)
    except:
      None

    if(len(others) == 0):
      paths.append(path)
      return 

    for i in others:
      if self.getWeight(sourceNode, i) == -1:
        continue
      self.permutaciones(i, paths, others.copy(), path = path.copy())
  
  def distancePath(self, path):
    distance = 0
    for i in range(0, len(path)-1):
      distance += self.getWeight(path[i], path[i+1])
    return distance


if __name__ == "__main__":
	main.main()