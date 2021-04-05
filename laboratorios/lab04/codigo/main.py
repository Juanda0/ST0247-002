import csv
class main:
  def main():
    a = lector.crearGrafoTxt('puentesColgantes.txt')
    print('El mejor camino TSP es')
    a.tsp()

    
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
    a = GraphAM(len(vertices))
    aux = 0
    for i in vertices:
      a.nombrarVertice(i, aux)
      aux += 1
  
    for i in range(len(arcs[0])):
      sourceNode = arcs[0][i]
      destinationNode = arcs[1][i]
      weight = float(arcs[2][i])
      a.addArc(sourceNode, destinationNode, weight)

    return a

#Graph implementation
class GraphAM:
  def __init__(self, size, infoNodes = None, parameters = None):
    self.size = size
    self.matriz = [[0 for i in range(size)] for i in range(size)]
    self.nombresVertices = {}
    self.infoNodes = infoNodes
    self.parameters = parameters

  def getWeight(self, sourceID, destinationID):
    if isinstance(sourceID, str):
      sourceID = self.nombresVertices[sourceID]
      destinationID = self.nombresVertices[destinationID]
    
    return self.matriz[sourceID][destinationID]
  
  def nombrarVertice(self, nombre, id):
    self.nombresVertices[nombre] = id

  def addArc(self, sourceID, destinationID, weight = 1):
    if isinstance(sourceID, str):
      sourceID = self.nombresVertices[sourceID]
      destinationID = self.nombresVertices[destinationID]
    self.matriz[sourceID][destinationID] = weight
    self.matriz[destinationID][sourceID] = weight
    
  def getSuccessors(self, vertice):
    succs = []
    aux = 0
    for i in self.matriz[vertice]:
      if i[0] != 0:
        succs.append(aux)
      aux += 1
    return succs

  #Receives an array and calculates the distance between each point in it
  def distancePath(self, path):
    distance = 0
    for i in range(0, len(path)-1):
      distance += (self.getWeight(path[i], path[i+1])[1] + self.parameters['st_customer'])
    return distance - (2*self.parameters['st_customer'])

  def getNameById(self,id):
    for key in self.nombresVertices.keys():
      if self.nombresVertices[key] == id:
        name = key
        break
    return name

  def tsp(self):
    stack = []
    nNodes = len(self.matriz)
    visited = [False for i in range(nNodes)]
    visited[0] = True
    stack.append(0)
    element,dst = 0,0
    print(f'{self.getNameById(0)}\t')
    while (len(stack) > 0):
      element = stack[-1]
      i = 0
      mini = float('inf')
      while (i < nNodes):
        if self.matriz[element][i] > 0 and not visited[i]:
          if mini > self.matriz[element][i]:
            mini = self.matriz[element][i]
            dst = i
            minFlag = True
        i += 1
      if minFlag:
        visited[dst] = True
        stack.append(dst)
        print(f'{self.getNameById(dst)}\t')
        minFlag = False
        continue
      stack.pop()
    print(f'{self.getNameById(0)}\t')
  
if __name__ == "__main__":
	main.main()
