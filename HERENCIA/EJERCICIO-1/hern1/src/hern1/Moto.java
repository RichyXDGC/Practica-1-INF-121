package hern1;

public class Moto extends Vehiculo {
    private int cilindrada;
    private String tipoMotor;

    public Moto(String marca, String modelo, int año, double precioBase, int cilindrada, String tipoMotor) {
        super(marca, modelo, año, precioBase);
        this.cilindrada = cilindrada;
        this.tipoMotor = tipoMotor;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Cilindrada: " + cilindrada + ", Tipo de motor: " + tipoMotor);
    }
}