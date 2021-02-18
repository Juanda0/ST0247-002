import csv
import collections
class main:
  def main():		
    my_file = "Arcos.txt"
    csv.register_dialect('skip_space', skipinitialspace=True)
    with open(my_file, 'r') as f:
      next(f)
      reader=csv.reader(f , delimiter=' ', dialect='skip_space')
      arcs = [[], [], []]
      for item in reader:
        arcs[0].append(item[0]) 
        arcs[1].append(item[1])
        arcs[2].append(item[2]) 
    
    vertices = arcs[0] + list(set(arcs[1]) - set(arcs[0]))
    a = GraphAl(len(vertices))
    a.nombrarVertices(vertices)
    for i in range(len(arcs[0])):
      sourceNode = arcs[0][i]
      destinationNode = arcs[1][i]
      weight = float(arcs[2][i])
      a.addArc(sourceNode, destinationNode, weight)
    a.getEdges()

class GraphAl:
  def __init__(self, size):
    self.size = size
    self.lista = [[] for i in range(size)]
    self.nombresVertices = []
    for i in range(len(self.lista)):
      self.nombresVertices.append(i)

  def getWeight(self, source, destination):
    for d in self.lista[source]:
      if d[0] == destination:
        return d[1]

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

if __name__ == "__main__":
	main.main()
