package comp1;

//b) Crear casa y agregar habitaciones
public class Main {
 public static void main(String[] args) {
     Casa casa = new Casa("Av. Libertador 123");

     Habitacion h1 = new Habitacion("Dormitorio", 16);
     Habitacion h2 = new Habitacion("Sala", 25);
     Habitacion h3 = new Habitacion("Cocina", 12);

     casa.agregarHabitacion(h1);
     casa.agregarHabitacion(h2);
     casa.agregarHabitacion(h3);

     // c) Mostrar información completa
     System.out.println(">>> Información de la casa:");
     casa.mostrarCasa();
 }
}