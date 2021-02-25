import java.util.*;
import javafx.util.Pair;

/**
 * La clase Taller5 trata grafos para ver sus posibilidades de ser coloreado.
 * @author Sebastian Guerra, Juan David Echeverri
 * @version 4
 */
public class Taller5
{
    /**
     * El método mColoring indica cuantos colores m se necesitan para pintar un grafo
     * @param g el grafo a analizar
     */
    public static int mColoring(Graph g){
        int m = 1000;
        int [] coloreado = new int[g.size()+1];
        int [] colores = new int[m];

        for (int i=0; i<m; i++){
            colores[i] = i+1;
        }

        coloreado[0] = 1; 

        Pair a = mColoringAux(g, 0, coloreado, colores);

        System.out.println("Se necesitan "+a.getValue()+" colores para pintar el grafo");
        return (int)a.getValue();
    }

    /**
     * El método coloring verifica si es posible colorear un grafo con m colores
     * @param g el grafo a analizar
     * @param m numero de colores
     * @return si el grafo puede ser coloreado con m colores
     */
    public static String coloring(Graph g, int m){        
        int [] coloreado = new int[g.size()+1];
        int [] colores = new int[m];

        for (int i=0; i<m; i++){
            colores[i] = i+1;
        }

        coloreado[0] = 1;
        return coloringAux(g, 0, coloreado, colores) ? "YES" : "NO";
    }


    private static boolean coloringAux(Graph g, int source, int[] coloreado, int[] colores){
        ArrayList<Integer> next = g.getSuccessors(source);

        boolean answer = false;

        for(int neighbor: next){
            if (coloreado[source] == coloreado[neighbor])
                return false;            
            else if(coloreado[neighbor] != 0)
                continue;

            for (int color: colores){
                if(coloreado[source] == color)
                    continue;
                coloreado[neighbor] = color;
                answer =  answer || coloringAux(g, neighbor, coloreado, colores);
                if (answer)
                    return true;
                else
                    coloreado[neighbor] = 0;                
            }

            if(coloreado[neighbor] == 0)
                return false;
        }

        return true;
    }

    private static Pair<Boolean, Integer> mColoringAux(Graph g, int source, int[] coloreado, int[] colores){
        ArrayList<Integer> next = g.getSuccessors(source);
        int cantColoresMax = 0;
        boolean answer = false;

        for(int neighbor: next){
            if (coloreado[source] == coloreado[neighbor])
                return new Pair(false, 0);            
            else if(coloreado[neighbor] != 0)
                continue;

            int cantColores = 0;
            for (int color: colores){
                cantColores++;
                if(coloreado[source] == color)
                    continue;

                coloreado[neighbor] = color;
                Pair x = mColoringAux(g, neighbor, coloreado, colores);
                answer =  answer || (boolean)x.getKey();

                cantColoresMax = Math.max(cantColoresMax, cantColores);
                cantColoresMax = Math.max(cantColoresMax, (int)x.getValue());
                if (answer)
                    return new Pair(true, cantColoresMax);
                else
                    coloreado[neighbor] = 0;                
            }            

            if(coloreado[neighbor] == 0)            
                return new Pair(false, 0);
        }

        return new Pair(true, cantColoresMax);
    }

    public static void main(){        
        ArrayList<Graph> lg = Lector.leerDataset();
        for(Graph g : lg){
            System.out.println("¿Cuantos necesito?");
            int m = mColoring(g); //Ejercicio 2
            
            System.out.println("¿Con esos me basta?");            
            System.out.println(coloring(g, m)); // Problema 1
            
            System.out.println("¿Si quito un color aún se puede?");            
            System.out.println(coloring(g, m-1)); // Problema 1
        }
    }
}
