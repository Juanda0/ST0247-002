import java.util.*;

public class Taller4
{   
    //Punto 1
    public static boolean pathDFS(Graph g, int source, int destination){
        boolean [] checked = new boolean[g.size()+1];
        return auxDFSPath(g, source, destination, checked);
    }
    
    private static boolean auxDFSPath(Graph g, int source, int destination, boolean[] checked){
        ArrayList<Integer> next = g.getSuccessors(source);
        checked[source] = true;
        boolean answer = false;

        if(destination == source){
            answer = true;
        }

        for(int neighbor: next){
            if(checked[neighbor] == false){
                answer = answer || auxDFSPath(g, neighbor, destination, checked);               
            }
            if (answer == true){
              break;
            }
        }
        return answer;
    }

    //Punto 2
    public static ArrayList lowCostPathDFS(Graph g, int source, int destination){
        boolean [] checked = new boolean[g.size()+1];
        ArrayList<ArrayList<Integer>, Integer> ruta = new ArrayList();
        return lowCostPathAux(g, source, destination, checked, ruta);
    }

    private static ArrayList lowCostPathAux(Graph g, int source, int destination, boolean[] checked, ArrayList ruta){

        ArrayList<Integer> next = g.getSuccessors(source);
        next.remove((Integer)source);
        
        checked[source] = true;
        boolean answer = false;

        
        if(destination == source){
            answer = true;
        }
        

        for(int neighbor: next){
            if(checked[neighbor] == false){
                Pair<ArrayList<Integer>, Integer> ruta = new ArrayList();
                ruta.set(1, ruta.get(1) + g.getWeight(source, neighbor));            
                ruta[0].append(source);
                answer = answer || lowCostPathAux(g, neighbor, destination, checked, ruta);               
            }
            if (answer == true){
              break;
            }
        }
        return answer;
  }

    
}