package comp3;

//b y c) Crear y mostrar
public class Main {
 public static void main(String[] args) {
     Avion avion = new Avion("Boeing 747", "Boeing");

     Parte motor = new Parte("Motor", 2000);
     Parte alas = new Parte("Alas", 5000);
     Parte tren = new Parte("Tren de Aterrizaje", 1500);

     avion.agregarParte(motor);
     avion.agregarParte(alas);
     avion.agregarParte(tren);

     System.out.println(">>> Información del avión:");
     avion.mostrarAvion();
 }
}