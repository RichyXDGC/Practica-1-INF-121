package java5;

class Laboratorio implements Ambiente {
    private String nombre;
    private int capacidad;
    private int nroMesas;
    private int nroSillas;

    public Laboratorio(String nombre, int capacidad, int nroMesas, int nroSillas) {
        this.nombre = nombre;
        this.capacidad = capacidad;
        this.nroMesas = nroMesas;
        this.nroSillas = nroSillas;
    }

    @Override
    public void mostrar() {
        System.out.printf("[Laboratorio] Nombre: %s, Capacidad: %d, Mesas: %d, Sillas: %d%n", 
                         nombre, capacidad, nroMesas, nroSillas);
    }

    @Override
    public int cantidadMuebles() {
        return nroMesas + nroSillas;
    }
}

