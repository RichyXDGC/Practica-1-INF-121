package gen3;

import java.util.ArrayList;
import java.util.List;

public class Catalogo<T> {
    private List<T> elementos = new ArrayList<>();

    public void agregar(T item) {
        elementos.add(item);
    }

    public boolean buscar(T item) {
        return elementos.contains(item);
    }

    public void mostrarTodos() {
        for (T item : elementos) {
            System.out.println(item);
        }
    }

    public static void main(String[] args) {
        Catalogo<String> catalogoLibros = new Catalogo<>();
        catalogoLibros.agregar("El Quijote");
        catalogoLibros.agregar("1984");
        catalogoLibros.mostrarTodos();
        System.out.println("¿Contiene '1984'? " + catalogoLibros.buscar("1984"));

        Catalogo<String> catalogoProductos = new Catalogo<>();
        catalogoProductos.agregar("Laptop");
        catalogoProductos.agregar("Teléfono");
        catalogoProductos.mostrarTodos();
        System.out.println("¿Contiene 'Tablet'? " + catalogoProductos.buscar("Tablet"));
    }
}
