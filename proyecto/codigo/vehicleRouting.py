import math
from collections import deque 
import random
import sys
class vehicleRouting:
  def __init__(self, grafo,seed = None, k = 1, b = None):
    self.grafo = grafo
    if seed is None:
      self.seed = random.randrange(sys.maxsize)
    else:
      self.seed = seed
    random.seed(self.seed)
    self.k = k #cantidad de clientes a randomizar (mejores k clientes)
    self.b = b #porcentaje de bateria 'critica' (ir a recargar si estacion esta cerca y bateria bajo este porcentaje)

  def getParameters(self):
    return {'Seed':self.seed, 'k':self.k,'b':self.b}

  #returns an estimate of the best station closest to the node were the route is standing on
  def getBestStation(self, startNode,timePath, battery, visited):
    bestStations = {'0':None, '1':None, '2':None}
    bestStationTimes = {'0':float('inf'), '1':float('inf'), '2':float('inf')}
    bestStationChargingTimes = {'0':0, '1':0, '2':0}
    breakPointUsed = 16000

    for station in self.grafo.getSuccessors(startNode,visited):
      if self.grafo.infoNodes[station][3] == 's':
        peso = self.grafo.getWeight(startNode, station)[1]
        if peso < bestStationTimes[self.grafo.infoNodes[station][4]] and (battery - (self.grafo.getWeight(startNode, station)[0]*self.grafo.parameters['r'])) > 0:
          bestStationTimes[self.grafo.infoNodes[station][4]] = peso
          bestStations[self.grafo.infoNodes[station][4]] = station

       
    
    for i in bestStationTimes.keys():
      if bestStations[i] is not None:
        batteryAux = battery - (self.grafo.getWeight(startNode, bestStations[i])[0] * self.grafo.parameters['r'])
        batteryAux = breakPointUsed- batteryAux
        bestStationChargingTimes[i] = batteryAux * float(self.grafo.parameters['chargingTimes'][int(i)][2])/breakPointUsed

    bestStation = None
    bestTime = float('inf')
     
    
    for i in bestStationTimes.keys():
      if bestStationTimes[i]+bestStationChargingTimes[i] < bestTime and bestStationChargingTimes[i] > 0:
        bestStation = bestStations[i]
        chargingTime = bestStationChargingTimes[i]
        bestTime = bestStationTimes[i]+bestStationChargingTimes[i]
    

    if bestStation is None:
      return None
      
    return {'bestStation':bestStation, 'chargingTime':chargingTime, 'breakPointUsed':breakPointUsed}

  #returns the nearest client of a node
  def getNearestClient(self, startNode, visited, timePath):
    mini = deque([float('inf') for i in range(self.k)])
    minSuccessors = deque([None for i in range(self.k)])
    for successor in self.grafo.getSuccessors(startNode,visited):
      if visited[successor] or self.grafo.infoNodes[successor][3] != 'c':
        continue
      for i in range(self.k):
        peso = self.grafo.getWeight(startNode,successor)[1]
        if peso < mini[i]:
          mini.insert(i,peso)
          minSuccessors.insert(i,successor) 
          mini.pop()
          minSuccessors.pop()
          break

    selectOne = random.randrange(0,self.k)
    while (selectOne > 0):
      if minSuccessors[selectOne] is None:
        selectOne -= 1
      else:
        break
    return minSuccessors[selectOne]


  def getMiddleStation(self,startNode,nearestClient,timePath,visited, battery):
    bestStation = None
    batteryReturned = None
    bestTime = float('inf')
    bestChargingTime = float('inf')
    breakPointUsed = 16000
    for station in self.grafo.getSuccessors(startNode,visited):
      if self.grafo.infoNodes[station][3] == 's':
        identifier = self.grafo.infoNodes[station][4]
        batteryRemaining = battery - (self.grafo.getWeight(startNode, station)[0]*self.grafo.parameters['r'])

        if startNode == 0:
          batteryToCharge = self.grafo.getWeight(station, nearestClient)[0]*self.grafo.parameters['r']
        else:
          batteryToCharge = breakPointUsed - batteryRemaining
        
        chargingTime = batteryToCharge *float(self.grafo.parameters['chargingTimes'][int(identifier)][2])/breakPointUsed
        time = self.grafo.getWeight(startNode, station)[1] +  chargingTime  + self.grafo.getWeight(nearestClient, station)[1]
        if time < bestTime and (battery - (self.grafo.getWeight(startNode, station)[0]*self.grafo.parameters['r'])) > 0 and time + timePath < self.grafo.parameters['Tmax'] and batteryRemaining + batteryToCharge <= 16000:
          bestTime = time
          bestStation = station
          bestChargingTime = chargingTime
          batteryReturned = batteryRemaining + batteryToCharge
    if bestStation is None:
      return None
    return {'bestStation':bestStation, 'chargingTime':bestChargingTime, 'breakPointUsed':batteryReturned}

  def goBackwards(self, path, startNode, timePath, battery, visited, typeN, previousBatterys, assumption = None, help=0):
    aux1 = path.pop() #The same as startNode, but we must delete it from the path
    aux2 = path[-1]

    #Delete the way between the startNode(aux1) and its previous node(aux2).
    timePath -= self.grafo.getWeight(aux1, aux2)[1] + self.grafo.parameters['st_customer']
    battery += (self.grafo.getWeight(aux1, aux2)[0] * self.grafo.parameters['r'])


    #If we create an assumption, we must delete it
    if assumption is not None:
      timePath -= self.grafo.getWeight(startNode, assumption)[1]        
      battery += self.grafo.getWeight(startNode, assumption)[0] * self.grafo.parameters['r']

    if self.grafo.infoNodes[aux1][3] == 's':
      battery -= previousBatterys.pop() #Substract what we charge

    visited[aux1] = False
    return self.vehicleRoutingAux(aux2, path, timePath,visited, battery, typeN, previousBatterys, help)

  def tryWithMiddle(self, startNode, timePath, battery, visited, path, previousBatterys, help):
    getStationData = self.getMiddleStation(startNode,0,timePath,visited, battery)  
    
    #Esta es la forma para soportar cuando Middle retorna None
    if getStationData is None:
      return self.goBackwards(path, startNode, timePath, battery, visited, 's', previousBatterys, help=help)

    timePath += getStationData['chargingTime'] + self.grafo.getWeight(startNode, getStationData['bestStation'])[1] + self.grafo.getWeight(0, getStationData['bestStation'])[1]

    if timePath > self.grafo.parameters['Tmax']:
      timePath -= getStationData['chargingTime'] + self.grafo.getWeight(startNode, getStationData['bestStation'])[1] + self.grafo.getWeight(0, getStationData['bestStation'])[1]
      return self.goBackwards(path, startNode, timePath, battery, visited, 's', previousBatterys, help=help)    #Alternar entre s y d
    else:
      previousBatterys.append(getStationData['breakPointUsed'] - battery)
      path.append(getStationData['bestStation'])
      battery = getStationData['breakPointUsed'] -  self.grafo.getWeight(getStationData['bestStation'], 0)[0] * self.grafo.parameters['r']
    
    if startNode == 0:
      return self.vehicleRoutingAux(getStationData['bestStation'], path, timePath,visited, getStationData['breakPointUsed'], 'c', previousBatterys, help)
    else:
      return self.vehicleRoutingAux(getStationData['bestStation'], path, timePath,visited, getStationData['breakPointUsed'], 'd', previousBatterys, help)

  def vehicleRouting(self):
    paths = []
    times = []
    batterys = []
    visited = [False for i in range(len(self.grafo.matriz))]
    visited[0] = True
    
    #A cycle that is executed until a path is only len = 1, that means that all the nodes has been visited
    route = 0
    while(True):         
        path = [0]
        a  = self.vehicleRoutingAux(0, path,0, visited, self.grafo.parameters['Q'], 'c', help=route)
        path.append(0)
        if len(path) == 2:
          break
        paths.append(path)
        times.append(a[1])
        batterys.append(a[2])
        route += 1
    return paths,times,batterys      

  #?? 
  def vehicleRoutingAux(self,startNode, path, timePath,visited, battery, nodeToGo, previousBatterys = [], help=0):
    
    battery_percentage = battery/int(self.grafo.parameters['breakPoints'][0][3])*100
    #gets the nearest client
    nearestClient = self.getNearestClient(startNode, visited, timePath)
    if battery_percentage < self.b and nodeToGo == 'c' and nearestClient is not None:
      getStationData = self.getBestStation(startNode, timePath, battery, visited)
      if getStationData is not None:
        #Data about the best station
        bestStation = getStationData['bestStation']
        chargingTime = getStationData['chargingTime']
        breakPointUsed = getStationData['breakPointUsed']
        if  self.grafo.getWeight(startNode,bestStation)[1] < self.grafo.getWeight(startNode, nearestClient)[1]: 
          timePath += self.grafo.getWeight(startNode, bestStation)[1] + chargingTime
          if timePath < self.grafo.parameters['Tmax']:
            previousBatterys.append(breakPointUsed - battery)
            path.append(bestStation)
            return self.vehicleRoutingAux(bestStation, path, timePath,visited, breakPointUsed, 'c', previousBatterys, help) 
          timePath -= self.grafo.getWeight(startNode, bestStation)[1] + chargingTime

    

    #if we have an actual path and we have enough time and energy to come back, return the path and its data
    if nearestClient is None:
      timePath += self.grafo.getWeight(startNode, 0)[1] 
      battery -= self.grafo.getWeight(startNode, 0)[0] * self.grafo.parameters['r']

      if timePath > self.grafo.parameters['Tmax']: 
        return self.goBackwards(path, startNode, timePath, battery, visited, 'd', previousBatterys,assumption = 0, help=help)

      if battery < 0:
        timePath -= self.grafo.getWeight(startNode, 0)[1] 
        battery += self.grafo.getWeight(startNode, 0)[0] * self.grafo.parameters['r']
        return self.tryWithMiddle(startNode, timePath, battery, visited, path, previousBatterys, help)
      
      #path.append(0)
      return path,timePath,battery

    if startNode == 0 and nodeToGo == 's':
       getStationData = self.getMiddleStation(0,nearestClient,timePath,visited, battery)
       previousBatterys.append(0)
       path.append(getStationData['bestStation'])
       timePath += getStationData['chargingTime'] + self.grafo.getWeight(startNode, getStationData['bestStation'])[1]
       return self.vehicleRoutingAux(getStationData['bestStation'], path, timePath, visited, getStationData['breakPointUsed'], 'c', previousBatterys, help)
    

    if nodeToGo == 'd':
      #Save the original battery
      originalBattery = battery

      #Suppose going to depot
      timePath += self.grafo.getWeight(startNode, 0)[1] 
      battery -= self.grafo.getWeight(startNode, 0)[0] * self.grafo.parameters['r']

      if timePath > self.grafo.parameters['Tmax']:
        return self.goBackwards(path, startNode, timePath, battery, visited, 'd', previousBatterys, assumption=0, help=help)
      
      elif battery <= 0:
        #Delete the assumptions
        timePath -= self.grafo.getWeight(startNode, 0)[1] 
        battery += self.grafo.getWeight(startNode, 0)[0] * self.grafo.parameters['r']

        #Try to found a station
        a = self.tryWithMiddle(startNode, timePath, battery, visited, path, previousBatterys, help)
        if a is not None:
          return a

      #path.append(0)
      return path,timePath,battery

    elif nodeToGo == 's':
      #Save the original battery
      originalBattery = battery

      #Try to get the best station to charge. If not possible, it will be null
      getStationData = self.getBestStation(startNode, timePath, battery, visited)
      
      if getStationData is not None:
        #Data about the best station
        bestStation = getStationData['bestStation']
        chargingTime = getStationData['chargingTime']
        breakPointUsed = getStationData['breakPointUsed']

        #Suppose going to that station
        timePath += self.grafo.getWeight(startNode, bestStation)[1] + chargingTime
        #battery -= self.grafo.getWeight(startNode, bestStation)[0] * self.grafo.parameters['r']
      else:
        return self.goBackwards(path, startNode, timePath, battery, visited, 's', previousBatterys, help=help)
        
      
      if timePath > self.grafo.parameters['Tmax']:
        return self.goBackwards(path, startNode, timePath, battery, visited, 's', previousBatterys, assumption=bestStation, help=help)        

      #There we must add the amount of charge in previousBatterys
      previousBatterys.append(breakPointUsed - originalBattery)
      path.append(bestStation)
      return self.vehicleRoutingAux(bestStation, path, timePath,visited, breakPointUsed, 'c', previousBatterys, help)

    #actualize timepath with the distance of the nearest client
    timePath += self.grafo.getWeight(startNode, nearestClient)[1] + self.grafo.parameters['st_customer']
      
    #actualize battery with the energy required to go to the nearest client
    battery -= self.grafo.getWeight(startNode, nearestClient)[0] * self.grafo.parameters['r']

    

    #if we exceed the time, delete the assumption and go to depot
    if timePath > self.grafo.parameters['Tmax']:
      timePath -= self.grafo.getWeight(startNode, nearestClient)[1] + self.grafo.parameters['st_customer']
      battery += self.grafo.getWeight(startNode, nearestClient)[0] * self.grafo.parameters['r']
      return self.vehicleRoutingAux(startNode, path, timePath,visited, battery, 'd', previousBatterys, help)
    
    if battery <= 0:
      timePath -= self.grafo.getWeight(startNode, nearestClient)[1] + self.grafo.parameters['st_customer']
      battery += self.grafo.getWeight(startNode, nearestClient)[0] * self.grafo.parameters['r']
      return self.vehicleRoutingAux(startNode, path, timePath,visited, battery, 's', previousBatterys, help)

 
    path.append(nearestClient)
    visited[nearestClient] = True
    return self.vehicleRoutingAux(nearestClient, path,timePath, visited, battery, 'c', previousBatterys, help)
