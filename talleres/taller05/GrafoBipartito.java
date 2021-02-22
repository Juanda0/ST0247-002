import java.util.*;
/**
 * La clase GrafoBipartito trata grafos para ver si coloreables.
 * @author Sebastian Guerra, Juan David Echeverri
 * @version 3
 */
public class GrafoBipartito
{
    /**
     * El método coloring verifica si es posible colorear un grafo con m colores
     * @param g el grafo que cumple las condiciones mencionadas.
     * @param m numero de colores
     * @return Si el grafo puede ser coloreado con m colores
     */
    public static String coloring(Graph g, int m){
        int [] coloreado = new int[g.size()+1];
        int [] colores = new int[m];

        for (int i=0; i<m; i++){
            colores[i] = i+1;
        }

        coloreado[1] = 1;        

        return verificarBipartitoDFS(g, 1, coloreado, colores) ? "YES" : "NO";  
    }

    private static boolean verificarBipartitoDFS(Graph g, int source, int[] coloreado, int[] colores){
        ArrayList<Integer> next = g.getSuccessors(source);
        int colorActual = 0;

        //Caso base: llegar a un nodo sin adyacentes
        if(next.size() == 0){
            return true;
        }

        boolean answer = false;
        //Caso recursivo       
        for(int neighbor: next){       
            for (Integer color : colores){
                if(coloreado[neighbor] == 0){
                    coloreado[neighbor] = color;
                    answer =  answer || verificarBipartitoDFS(g, neighbor, coloreado, colores);
                    if (answer){
                        break;
                    }else
                        coloreado[neighbor] = 0;
                }
                
                if(coloreado[source] == coloreado[neighbor]){
                    coloreado[neighbor] = 0;
                }
            }
            
            if(coloreado[neighbor] == 0){
                return false;
            }
        }

        //Cambio de color para los adyacentes a los sucesores               

        return answer;
    }//O(n^2) siendo n el numero de vertices

    public static void main(){        
        ArrayList<Graph> lg = Lector.leerDataset();
        for(Graph g : lg){
            System.out.println(coloring(g, 2));
        }
    }
}
