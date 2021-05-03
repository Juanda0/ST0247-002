import GraphAM as gAM
import lector as lt
import vehicleRouting as vr


#Datasets/tc2c320s24cf0.txt
#Datasets/tc2c320s24cf1.txt
#Datasets/tc2c320s24cf4.txt
#Datasets/tc2c320s24ct0.txt
#Datasets/tc2c320s24ct1.txt
#Datasets/tc2c320s24ct4.txt
#Datasets/tc2c320s38cf0.txt
#Datasets/tc2c320s38cf1.txt
#Datasets/tc2c320s38cf4.txt
#Datasets/tc2c320s38ct0.txt
#Datasets/tc2c320s38ct1.txt
#Datasets/tc2c320s38ct4.txt
#Datasets/dummy.txt
class main: 
  def main():

    grafo = lt.lector.crearGrafoTxt("Datasets/tc2c320s38ct4.txt")
    aux = vr.vehicleRouting(grafo)
    a = aux.vehicleRouting()
    paths = a[0]
    times = a[1]
    batterys = a[2]
    colors = []
    print(f"AAAAAAAAAAAAAA {grafo.parameters['chargingTimes'][0][0]} ")
    for i in range(40):
      colors.append(gAM.GraphAM.rand_web_color_hex())
    print(aux.seed)
    #print(times)
    #print(batterys)
    grafo.showGraph(paths,colors, mode = 'Paths')  


if __name__ == "__main__":
  main.main()
