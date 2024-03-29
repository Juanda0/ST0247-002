import java.util.ArrayList;
import java.util.Collections;

/**
 * Clase en la cual se implementan los metodos del Taller 3
 * 
 * @author Mauricio Toro, Camilo Paez
 */
public class Taller3 {
	
	/**
	* Metodo que verifica si es posible poner las reinas hasta la columna c
	* 
	* @param  c hasta esta columna revisa
	* @param  tablero el tablero
	* @return true si es posible, false de lo contrario
	*/	
	private static boolean puedoPonerReina(int c, int f, int[] tablero) {
    if (Arrays.asList(tablero).contains(f)){
      return false;
    }
    return checarDiagonales(c, f, 0, tablero);
	}

  private static boolean checarDiagonales(int c, int f, int nivelRecur, int[] tablero) {
    if (c < 0 || c >= tablero.length){
      return true;
    }
    if(tablero[c] == f + nivelRecur || tablero[c] == f - nivelRecur){
      return false;
    }
    return checarDiagonales(c-1, f, nivelRecur+1, tablero) || checarDiagonales(c+1, f, nivelRecur+1, tablero);
  }
	
	
	/**
	* Metodo auxiliar para llamar el metodo posterior
	* 
	* @param  n numero de reinas
	* @return numero de soluciones
	*/	
	public static int nReinas(int n) {
		return nReinas(0, n, new int[n]);
	}

	/**
	* Metodo devuelve el numero de soluciones que tiene el problema
	* 
	* @param  c columna
	* @param  n numero de reinas
	* @return numero de soluciones
	*/	
	private static int nReinas(int c, int n, int[] tablero) {
    
	}
	
	public static void imprimirTablero(int[] tablero) {
		int n = tablero.length;
		System.out.print("    ");
		for (int i = 0; i < n; ++i)
			System.out.print(i + " ");
		System.out.println("\n");
		for (int i = 0; i < n; ++i) {
			System.out.print(i + "   ");
			for (int j = 0; j < n; ++j)
				System.out.print((tablero[i] == j ? "Q" : "#") + " ");
			System.out.println();
		}
		System.out.println();
	}
	
	/**
	* Metodo que recorre un grafo por dfs
	* 
	* @param  g grafo ya implementado
	* @param  inicio nodo inicial
	* @param  fin nodo final
	* @return una lista con el camino encontrado
	*/	
	public static ArrayList<Integer> camino(Digraph g, int inicio, int fin) {
	
	}

	/**
	* Metodo que implemeta un recorrido de un grafo por profundidad (dfs)
	* 
	* @param  g grafo ya implementado
	* @param  nodo nodo desde el cual se empezara hacer la busqueda
	* @param  objetivo hasta donde se quiere llegar
	* @param  visitados representa los nodos que ya se verificaron
	* @param  list la lista con el camino encontrados
	* @return  una lista con el camino
	*/	
	private static ArrayList dfs(Digraph g, int nodo, int objetivo, boolean[] visitados, ArrayList<Integer> list) {
		
	}

}
