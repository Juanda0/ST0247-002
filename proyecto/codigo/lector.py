import re
import GraphAM as gAM
import math
class lector:
  #Given a txt, creates a graph
  def crearGrafoTxt(archivo):		
    with open(archivo, "r") as f:
      a_txt = f.readlines()
    textAsString = "".join(a_txt)
    parameters = dict(re.findall("(\w+) = (\d+[.\d+]*)", textAsString))#Regular expression for parameters
    for p in parameters.keys():
      parameters[p] = float(parameters[p])
    parameters['breakPoints'] =  re.findall("(\d*) (\d*) (\d*) (\d*)", textAsString) #Regular expression for breakPoints
    parameters['chargingTimes'] = re.findall("0 (\d\.\d+) (\d\.\d+) (\d\.\d+)", textAsString) #Regular expression for times from crearGrafoTxt  

    carSpeed = parameters['speed']
    infoNodes = re.findall("\d+ (\w+) (\d+.\d+) (\d+.\d+) (\w) (\d)", textAsString)#Regular expression for info of nodes
    print(infoNodes)

    grafo = gAM.GraphAM(int(parameters['n']), infoNodes, parameters)
    for idNode in range(len(infoNodes)):
      infoNode = infoNodes[idNode]
      grafo.nombrarVertice((infoNodes[idNode][0],idNode))
      for nodeAux in range(len(infoNodes)):
        if idNode != nodeAux:
          infoNodeAux = infoNodes[nodeAux]
          distanceN = math.sqrt(((float(infoNodeAux[1])-float(infoNode[1]))**2) + ((float(infoNodeAux[2])-float(infoNode[2]))**2))
          timeN = distanceN/carSpeed
          weight = (distanceN, timeN)
          grafo.addArc(idNode, nodeAux, weight)
    return grafo