def main():
  cadena = "abc"
  respuestas = []
  permutacionesConRepeticion(respuestas, "", cadena, len(cadena))
  print(respuestas)

#Punto 1
def combinaciones(respuestas, loQueLlevo, loQueFalta):
  if len(loQueFalta) == 0:
    respuestas.append(loQueLlevo)
    return
  
  combinaciones(respuestas, loQueLlevo+loQueFalta[0], loQueFalta[1:])
  combinaciones(respuestas, loQueLlevo, loQueFalta[1:])

#Punto 2
def permutacionesSinOrden(respuestas, loQueLlevo, loQueFalta, tamaño):
  if len(loQueLlevo) == tamaño:
    respuestas.append(loQueLlevo)
    return
  
  for caracter in loQueFalta:
    permutacionesSinOrden(respuestas, loQueLlevo+caracter, loQueFalta.replace(caracter, ""), tamaño)

#Punto 4
def permutacionesConRepeticion(respuestas, loQueLlevo, loQueFalta, tamaño):
  if len(loQueLlevo) == tamaño:
    respuestas.append(loQueLlevo)
    return
  
  for caracter in loQueFalta:
     permutacionesConRepeticion(respuestas, loQueLlevo+caracter, loQueFalta, tamaño)

if __name__ == "__main__":
   main()