
class vehicleRouting:
  def __init__(self, grafo):
    self.grafo = grafo

  #returns the nearest client of a node
  def getNearestClient(self, startNode, visited, timePath):
    mini = float('inf')
    minSuccessor = None
    for successor in self.grafo.getSuccessors(startNode):
      peso = self.grafo.getWeight(startNode,successor)[1]
      if not visited[successor] and peso < mini and self.grafo.infoNodes[successor][3] == 'c' and timePath <= self.grafo.parameters['Tmax']:
        mini = peso
        minSuccessor = successor
    return minSuccessor

 
  #Solution of the problem
  def vehicleRouting(self):
    paths = []
    times = []
    visited = [False for i in range(len(self.grafo.matriz))]
    visited[0] = True

    #A cycle that is executed until a path is only len = 1, that means that all the nodes has been visited
    while(True):
      path = [0]
      a  = self.vehicleRoutingAux(0, path,0, visited)
      if len(path) == 1:
        break
      path.append(0)
      paths.append(path)
      times.append(a[1])
      print(f'{path} Time: {a[1]}')
    return paths,times


  #Solution of the problem
  def vehicleRoutingAux(self,startNode, path, timePath,visited):
    #if we have an actual path and the startNode is 0, return the path and its data
    if startNode == 0 and len(path)>1:
      return path,timePath

    #gets the nearest client
    nearestClient = self.getNearestClient(startNode, visited, timePath)

    #if we have an actual path and we have enough time and energy to come back, return the path and its data
    if nearestClient is None and timePath + self.grafo.getWeight(startNode, 0)[1] <= self.grafo.parameters['Tmax']:
     return path,timePath

    #actualize timepath with the distance of the nearest client
    timePath += self.grafo.getWeight(startNode, nearestClient)[1] + self.grafo.parameters['st_customer']


    #if we exceed the time, raise a time exceed exception
    if timePath > self.grafo.parameters['Tmax']:
      raise timeExceeded
   
    try:
      path.append(nearestClient)     
      visited[nearestClient] = True
      return self.vehicleRoutingAux(nearestClient, path,timePath, visited)
   
    except timeExceeded:
      return self.timeExceededCaseManagement(path, visited,timePath, nearestClient)

  
    

    
  #Due to management of self created errors, here we manage the errors caused by exceeding the limit time of the path
  def timeExceededCaseManagement(self, path, visited,timePath, nearestClient):
      path.pop() 

      #Supposing a possible travel back to the deposit
      timePath += self.grafo.getWeight(nearestClient,0)[1]

      #After supposing the travel, if we ran out of time, we raise an exception to get back to the last node

      #if going back to the deposit let us out of time, we des-visit clients until is possible to get back
      if timePath > self.grafo.parameters['Tmax']:
        visited[nearestClient] = False
        raise timeExceeded
      else:
      #Otherwise, we return the path
        path.append(nearestClient)
        return path,timePath


#Exception that indicates a lack of time
class timeExceeded(Exception):
  pass
