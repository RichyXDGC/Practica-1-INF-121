package java5;

class Aula implements Ambiente {
    private String nombre;
    private int capacidad;
    private int nroPupitres;

    public Aula(String nombre, int capacidad, int nroPupitres) {
        this.nombre = nombre;
        this.capacidad = capacidad;
        this.nroPupitres = nroPupitres;
    }

    @Override
    public void mostrar() {
        System.out.printf("[Aula] Nombre: %s, Capacidad: %d, Pupitres: %d%n", 
                         nombre, capacidad, nroPupitres);
    }

    @Override
    public int cantidadMuebles() {
        return nroPupitres;
    }
}
