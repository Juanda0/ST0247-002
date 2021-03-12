
#Ejemplo (poner en consola):
#5 6
#1 2 2
#2 5 5
#2 3 4
#1 4 1
#4 3 3
#3 5 1

class main:
  def main():
    a = lector.crearGrafoConsola()
    source = '4'
    destination = '2'
    path = [source]
    bestPath = a.bestPathBT(source, destination, path = path)
    if bestPath[0] == float("inf"):
      print(-1)
    else:
      print(a.showPath(bestPath[1]))


class lector:
  def crearGrafoConsola():	
    graphData = input("").split(' ')
    grafo = GraphAl(int(graphData[0]))
    for i in range(int(graphData[1])):
      insertEdge = input("").split(' ')
      sourceNode = insertEdge[0]
      destinationNode = insertEdge[1]
      weight = float(insertEdge[2])
      grafo.addArc(sourceNode, destinationNode, weight)
    return grafo

class GraphAl:
  def __init__(self, size):
    self.size = size
    self.lista = [[] for i in range(size)]
    self.nombresVertices = []
    for i in range(1, len(self.lista)+1):
      self.nombresVertices.append(str(i))

  def getWeight(self, sourceNode, destinationNode):
    source = self.nombresVertices.index(sourceNode)
    destination = self.nombresVertices.index(destinationNode)
    a = -1
    aux = float('inf')
    for d in self.lista[source]:
      if d[0] == destination:
        if d[1] < aux:      
          a = d[1]
          aux = a
    return a
  
  def nombrarVertices(self, nombresVertices):
    if len(nombresVertices) == len(self.lista):
      self.nombresVertices = nombresVertices
    else:
      print("Los nombres exceden el tamaño de la lista")

  def addArc(self, sourceNode, destinationNode, weight = 1):
    source = self.nombresVertices.index(sourceNode)
    destination = self.nombresVertices.index(destinationNode)
    self.lista[source].append((destination, weight))
    self.lista[destination].append((source, weight))

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
      a += path[i] + ' '
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
