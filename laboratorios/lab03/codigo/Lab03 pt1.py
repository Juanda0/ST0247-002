import csv

class main:
  def main():
    a = lector.crearGrafoTxt("puentesColgantes.txt")
    source = '4'
    destination = '2'
    path = [source]
    bestPath = a.bestPathBT(source, destination, path = path)
    print(f"El mejor camino entre {source} y {destination} es {a.showPath(bestPath[1])} y tiene una distancia de {bestPath[0]}")
    

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

  def getSuccessors(self, verticeName):
    vertice = self.nombresVertices.index(verticeName)
    succs = []
    for d in self.lista[vertice]:
      succs.append(self.nombresVertices[d[0]])
    return succs

  def getEdgesDirected(self):
    print("digraph Matriz {")
    i = 0
    for i in range(len(self.lista)):
      for j in self.lista[i]:
        try:
          a = '\"' + str(self.nombresVertices[i]) + '\"'
          b = '\"' + str(self.nombresVertices[j[0]]) + '\"'
          print("  " + a + ' -> ' + b )         
        except:
          break

  def getEdgesUndirected(self):
    print("graph Matriz {")
    i = 0
    printed = []
    for i in range(len(self.lista)):
      for j in self.lista[i]:
        try:
          a = '\"' + str(self.nombresVertices[i]) + '\"'
          b = '\"' + str(self.nombresVertices[j[0]]) + '\"'
          if "  " + a + ' -- ' + b in printed:
            continue
          else:
            printed.append("  " + a + ' -- ' + b)
            printed.append("  " + b + ' -- ' + a)
            print("  " + a + ' -- ' + b )         
        except:
          break
    print("}")

  def wlist(self):
    for i in self.lista:
      print(i)

  def distancePath(self, path):
    distance = 0
    if len(path) == 0:
      return 0
    for i in range(0, len(path)-1):
      distance += self.getWeight(path[i], path[i+1])
    return distance

  def showPath(self, path):
    a = ''
    for i in range(len(path)):
      if i == len(path)-1:
        a += path[i]
        break
      a += path[i] + ' -- '
    return a

  def bestPathBT(self, sourceNode, destinationNode, path = []):

    if sourceNode == destinationNode:
      return (self.distancePath(path), path.copy())

    successors = self.getSuccessors(sourceNode)

    bestDistance = float('inf')
    bestPath = []
    for node in successors:
      if node in path:
        continue
      
      path.append(node)  
      aux = self.bestPathBT(node, destinationNode, path = path) 
      path.remove(node)

      if aux[0] < bestDistance:
        bestDistance = aux[0]
        bestPath = aux[1]
    
    return (bestDistance, bestPath)
    
      
      
      


 
  
if __name__ == "__main__":
	main.main()