import matplotlib as mpl
import os
import matplotlib.pyplot as plt
import random

class GraphAM:
  def __init__(self, size, infoNodes = None, parameters = None):
    self.size = size
    self.matriz = [[(0,0) for i in range(size)] for i in range(size)]
    self.nombresVertices = {}
    self.infoNodes = infoNodes
    self.parameters = parameters
  
  #Generates a random color for visualization
  def rand_web_color_hex():
    rgb = ""
    for _ in "RGB":
        i = random.randrange(0, 2**8)
        rgb += i.to_bytes(1, "big").hex()
    if rgb == 'FFFFFF' or rgb == '000000':
      return GraphAM.rand_web_color_hex()
    return '#' + rgb

  def getWeight(self, sourceID, destinationID):
    if isinstance(sourceID, str):
      sourceID = self.nombresVertices[sourceID]
      destinationID = self.nombresVertices[destinationID]
    
    return self.matriz[sourceID][destinationID]
  
  def nombrarVertice(self, node):
    self.nombresVertices[node[0]] = node[1]

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

  #Flattens a matrix
  def flatten(matriz):
    aux = []
    for i in matriz:
      for j in i:
        aux.append(j)
    return set(aux)

  #Depending on the mode (Either 'Map' or 'Paths'), shows a visualization of the problem
  def showGraph(self,paths, colors, mode = 'Map'):
    stations = ['m', 'orange', 'yellow']
    if mode == 'Map':
      cliente = '#55db88'
    elif mode == 'Paths':
      cliente = 'r'

    plt.xlim(-5,125)
    plt.ylim(-5,125)
    flatten_paths = GraphAM.flatten(paths)
    print(len(flatten_paths))
    print(len(paths))
    for i in range(len(self.infoNodes)):
      if i in flatten_paths and i != 0 and mode == 'Paths' and self.infoNodes[i][3] != 's':
        continue
      infoNode = self.infoNodes[i]
      if infoNode[3] == 'd':
        plt.plot(float(infoNode[1]),float(infoNode[2]), marker="*", color="k")
      elif infoNode[3] == 'c':
        plt.plot(float(infoNode[1]),float(infoNode[2]), marker="h", color=cliente)
      elif infoNode[3] == 's':
        if infoNode[4] == '0':
          plt.plot(float(infoNode[1]),float(infoNode[2]), marker="D", color=stations[0])
        elif infoNode[4] == '1':
          plt.plot(float(infoNode[1]),float(infoNode[2]), marker="D", color=stations[1])
        elif infoNode[4] == '2':
          plt.plot(float(infoNode[1]),float(infoNode[2]), marker="D", color=stations[2])

    if mode == 'Paths':  
      auxCol = 0
      auxFig = 1
      for auxPath in paths:
        x_coordinates = []
        y_coordinates = []
        for i in auxPath:
          if auxCol == len(colors):
            auxCol = 0
          if i != 0:
            x_coordinates.append(float(self.infoNodes[i][1]))
            y_coordinates.append(float(self.infoNodes[i][2]))
        plt.xlim(-5,125)
        plt.ylim(-5,125)
        plt.scatter(x_coordinates, y_coordinates, color=colors[auxCol])
        plt.plot(x_coordinates, y_coordinates, color=colors[auxCol])
        
        #plt.savefig('Gif2/fig'+str(auxFig)+'.svg')
        auxCol += 1
        auxFig += 1
      
    plt.show()  