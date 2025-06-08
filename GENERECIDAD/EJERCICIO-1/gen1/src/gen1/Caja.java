package gen1;

public class Caja<T> {
    private T contenido;

    public void guardar(T item) {
        this.contenido = item;
    }

    public T obtener() {
        return contenido;
    }

    public static void main(String[] args) {
        Caja<String> cajaString = new Caja<>();
        cajaString.guardar("Hola Mundo");

        Caja<Integer> cajaEntero = new Caja<>();
        cajaEntero.guardar(123456);

        System.out.println("Contenido de cajaString: " + cajaString.obtener());
        System.out.println("Contenido de cajaEntero: " + cajaEntero.obtener());
    }
}