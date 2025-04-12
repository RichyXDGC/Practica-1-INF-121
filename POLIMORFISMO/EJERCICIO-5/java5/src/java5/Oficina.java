package java5;

class Oficina implements Ambiente {
    private int nroSillas;
    private int nroEscritorios;
    private int nroEstanterias;

    public Oficina(int nroSillas, int nroEscritorios, int nroEstanterias) {
        this.nroSillas = nroSillas;
        this.nroEscritorios = nroEscritorios;
        this.nroEstanterias = nroEstanterias;
    }

    @Override
    public void mostrar() {
        System.out.printf("[Oficina] Sillas: %d, Escritorios: %d, Estanterías: %d%n", 
                         nroSillas, nroEscritorios, nroEstanterias);
    }

    @Override
    public int cantidadMuebles() {
        return nroSillas + nroEscritorios + nroEstanterias;
    }
}
