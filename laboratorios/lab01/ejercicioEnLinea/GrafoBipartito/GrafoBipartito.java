import java.util.*;
/**
 * La clase GrafoBipartito trata grafos para ver si son bipartitos.
 * @author Sebastian Guerra, Juan David Echeverri
 * @version 3
 */
public class GrafoBipartito
{
    /**
     * El método descomponerGarras verifica si es posible descomponer un grafo simple con todos sus vertices de grado 3 en garras.
     * @param g el grafo que cumple las condiciones mencionadas.
     * @return la veracidad sobre la descomposición en garras del grafo ingresado.
     */
    public static String descomponerGarras(Graph g){
        int [] coloreado = new int[g.size()+1];
        coloreado[1] = 1;
        
        return verificarBipartitoBFS(g, 1, coloreado, 2) ? "YES" : "NO";  
    }
    
    private static boolean verificarBipartitoBFS(Graph g, int source, int[] coloreado, int colorActual){
        ArrayList<Integer> next = g.getSuccessors(source);
        
        //Caso base: llegar a un nodo sin adyacentes
        if(next.size() == 0){
            return true;
        }
        
        Queue<Integer> cola = new LinkedList<Integer>();
        boolean answer = true;
        
        //Caso recursivo       
        for(int neighbor: next){
            if(coloreado[neighbor] == 0){
                cola.add(neighbor);
                coloreado[neighbor] = colorActual;
            }
            else if(coloreado[neighbor] != colorActual){
                return false;
            }
        }

        //Cambio de color para los adyacentes a los sucesores
        colorActual = colorActual == 1 ? 2:1;
        while (cola.size() != 0){         
            int sig = (int)cola.poll();            
            answer =  answer && verificarBipartitoBFS(g, sig, coloreado, colorActual); //O(n^2)
            if(!answer){
                break;
            }
        }
        
        return answer;
    }//O(n^2) siendo n el numero de vertices

    public static void main(){        
        ArrayList<Graph> lg = Lector.leerDataset();
        for(Graph g : lg){
            System.out.println(descomponerGarras(g));
        }
    }
}
