package ejercicio2;

public class Coche {
    private String marca;
    private String modelo;
    private int velocidad;

    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = 0;
    }

    public void acelerar() {
        this.velocidad += 10;
    }

    public void frenar() {
        this.velocidad -= 5;
        if (this.velocidad < 0) {
            this.velocidad = 0;
        }
    }

    public void mostrarVelocidad() {
        System.out.println(this.marca + " " + this.modelo + " va a " + this.velocidad + " km/h");
    }

    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Caldina");
        Coche coche2 = new Coche("Suzuki", "Fachera");

        coche1.acelerar();
        coche1.acelerar();
        coche1.frenar();

        coche2.acelerar();
        coche2.frenar();
        coche2.frenar();

        coche1.mostrarVelocidad();
        coche2.mostrarVelocidad();
    }
}