package hern1;

public class Vehiculo {
    protected String marca;
    protected String modelo;
    protected int año;
    protected double precioBase;

    public Vehiculo(String marca, String modelo, int año, double precioBase) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.precioBase = precioBase;
    }

    public void mostrarInfo() {
        System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Año: " + año + ", Precio base: " + precioBase);
    }
}