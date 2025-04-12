package java1;

public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    public Videojuego() {
        this("Desconocido", "Genérica", 1);
    }

    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    public void mostrar() {
        System.out.println("Videojuego: " + this.nombre);
        System.out.println("Plataforma: " + this.plataforma);
        System.out.println("Jugadores: " + this.cantidadJugadores);
    }

    public void agregarJugadores() {
        this.cantidadJugadores += 1;
        System.out.println("Se agregó 1 jugador. Total ahora: " + this.cantidadJugadores);
    }

    public void agregarJugadores(int cantidad) {
        this.cantidadJugadores += cantidad;
        System.out.println("Se agregaron " + cantidad + " jugadores. Total ahora: " + this.cantidadJugadores);
    }

    public static void main(String[] args) {
        Videojuego v1 = new Videojuego("Hollow Knight", "PC", 1);
        Videojuego v2 = new Videojuego("It Takes Two", "PS5", 2);

        v1.mostrar();
        v1.agregarJugadores();
        v1.agregarJugadores(3);

        System.out.println(".............");

        v2.mostrar();
        v2.agregarJugadores(2);
    }
}