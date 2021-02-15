class Main {
  public static void main(String[] args) {
    Graph elGrafoMasMelo = new GraphAL(5);
    elGrafoMasMelo.addArc(0,1,0);
    elGrafoMasMelo.addArc(1,2,0);
    elGrafoMasMelo.addArc(2,3,0);
    elGrafoMasMelo.addArc(3,4,0);
    elGrafoMasMelo.addArc(2,5,0);
    string hayCamino = Taller4.pathDFS(elGrafoMasMelo, 0, 5) ? "Hay Camino" : "No hay camino";
    System.out.print(hayCamino);

  }
}