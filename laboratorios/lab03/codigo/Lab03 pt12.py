import time

def puedoPonerReina(c, f, tablero):
  tablero[c] = f
  for i in range(c):
    if(tablero[i]==tablero[c] and tablero[i] != 0):
      tablero[c] = 0
      return False
    
    elif(abs(c-i) == abs(tablero[c]-tablero[i]) and tablero[c] + tablero[i] != 0):
      tablero[c] = 0
      return False

  tablero[c] = 0
  return True

def nReinas(n, way):
  tablero = []
  for i in range(n):
    tablero.append(0)
  if way == "BF":
    return nReinasBF(0, n, tablero)
  elif way == "BT":
    return nReinasBT(0, n, tablero)

def nReinasBF(c, n, tablero):
  soluciones = 0
  if (c == n):
    return 1
     
  for i in range(1, n+1):
    if puedoPonerReina(c,i,tablero):    
      tablero[c] = i;
      soluciones += nReinasBF(c+1, n, tablero)

  return soluciones

def nReinasBT(c, n, tablero):
  answer = False
  if (c == n):
    return True
     
  for i in range(1, n+1):
    if puedoPonerReina(c,i,tablero):    
      tablero[c] = i;
      answer = answer or nReinasBT(c+1, n, tablero);
    if answer:
      break
  if answer:
    return tablero
  else:
    return False

if __name__ == '__main__':
  BFTimes = open("BFTimes.txt", "w")
  BTTimes = open("BTTimes.txt", "w")

  BFTimes.write("Time of Execution for nReinas using brute force:\n\n")
  BTTimes.write("Time of Execution for nReinas using backtracking:\n\n")
  for i in range(16):
    print(i)
    start_time1 = time.time()  
    nReinas(i,'BF')
    end_time1 = time.time() 
    BFTimes.write(f"nReinas = {i} \nExecution time: {round(end_time1-start_time1,5)}\n\n")
  for i in range(31):  
    print(i)
    start_time2 = time.time()  
    print(nReinas(i,'BT'))
    end_time2 = time.time() 
    BTTimes.write(f"nReinas = {i} \nExecution time: {round(end_time2-start_time2,5)}\n\n")

  BFTimes.close()
  BTTimes.close()
