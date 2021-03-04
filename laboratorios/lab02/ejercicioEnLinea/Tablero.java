import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;
/**
 * La clase Tablero contiene el desarrollo del segundo punto del lab 2
 * @author Juan David Echeverri, Sebastian Guerra
 * @version 2
 */
public class Tablero {
  
	
	/**
	* Metodo que verifica si es posible poner las reinas hasta la columna c, que soporta posiciones rotas
	* 
	* @param c hasta esta columna revisa
  * @param f la posible fila
	* @param tablero el tablero
  * @param casillasRotas Arreglo con las posiciones donde no podemos poner reinas
	* @return true si es posible, false de lo contrario
	*/	
	private static boolean puedoPonerReinaRoto(int c,int f, int[] tablero,ArrayList<Integer>[] casillasRotas) {
    if (casillasRotas[f-1] != null && casillasRotas[f-1].contains(c))
      return false;
      
    tablero[c] = f;
    for(int i = 0; i<c ; i++){
      if(tablero[i]==tablero[c] && tablero[i] != 0){
        tablero[c] = 0;
        return false;
      }
      else if(Math.abs(c-i) == Math.abs(tablero[c]-tablero[i]) && tablero[c] + tablero[i] != 0){
        tablero[c] = 0;
        return false;
      }
    }
    tablero[c] = 0;
    return true;
  }//O(n)
		
  /**
	* Metodo auxiliar para llamar el metodo posterior, solicita tamaño de tablero n, y posteriormente el tablero, con '.' para indicar casillas y '*' para indicar casillas rotas
	* @return numero de soluciones
	*/	
  public static void nReinasRoto() {
    Scanner scan = new Scanner(System.in);
    ArrayList<Integer> respuestas = new ArrayList();
    
    while(true){
      int n = scan.nextInt();
      if (n == 0)
        break;
        
      ArrayList<Integer>[] casillasRotas = new ArrayList[n];
      for(int i = 0; i < n; i++){      
        String row = scan.next();

        if (row.length() != n){
          System.out.printf("Recuerde que su tablero es de %d x %d \n", n, n);
          return;
        }

        for (int j=0; j<n; j++){
          if(row.charAt(j) == '*'){
            if(casillasRotas[i] == null){
              casillasRotas[i] = new ArrayList();
            }
            casillasRotas[i].add(j);
          }
        }             
      }
      respuestas.add(nReinasRoto(0, n, new int[n], casillasRotas));
    }
    int i = 1;
    for(Integer respuesta: respuestas){
      System.out.printf("Case %d: %d \n", i, (int)respuesta);
      i++;
    }
	}

  /**
	* Metodo devuelve el numero de soluciones que tiene el problema
	* 
	* @param  c columna
	* @param  n numero de reinas
  * @param  casillasRotas Arreglo con las posiciones donde no podemos poner reinas
	* @return numero de soluciones
	*/	
  private static int nReinasRoto(int c, int n, int[] tablero,ArrayList<Integer>[] casillasRotas){
    int soluciones = 0;
    if (c == n){
      return 1;
    }   
    for (int i = 1; i <= n; i++){
      if (puedoPonerReinaRoto(c,i, tablero, casillasRotas)){        
        tablero[c] = i;
        soluciones += nReinasRoto(c+1, n, tablero, casillasRotas);
      }
    }
    //System.out.println("Exit 2");
    return soluciones;  
  }
	

  /**
	* Metodo Imprime una visualizacion de las posiciones de las reinas 
	*/	
	public static void imprimirTablero(int[] tablero) {
		int n = tablero.length;
		System.out.print("    ");
		for (int i = 0; i < n; ++i)
			System.out.print(i + " ");
		System.out.println("\n");
		for (int i = 0; i < n; ++i) {
			System.out.print(i + "   ");
			for (int j = 1; j <= n; ++j)
				System.out.print((tablero[i] == j ? "Q" : "#") + " ");
			System.out.println();
		}
		System.out.println();
    
    
	}
}