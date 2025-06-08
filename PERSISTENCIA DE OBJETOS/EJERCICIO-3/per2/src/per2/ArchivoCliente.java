package per2;
import java.io.*;
import java.util.*;

public class ArchivoCliente {
    private String nomA;

    public ArchivoCliente(String n) {
        this.nomA = n;
        crearArchivo();
    }

    private void crearArchivo() {
        File file = new File(nomA);
        if (!file.exists()) {
            try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
                oos.writeObject(new ArrayList<Cliente>());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public void guardaCliente(Cliente c) {
        List<Cliente> clientes = leerClientes();
        clientes.add(c);
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
            oos.writeObject(clientes);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Cliente buscarCliente(int id) {
        for (Cliente c : leerClientes()) {
            if (c.getId() == id) {
                return c;
            }
        }
        return null;
    }

    public String buscarCelularCliente(int id) {
        Cliente c = buscarCliente(id);
        if (c != null) {
            return "Cliente: " + c.getNombre() + ", Teléfono: " + c.getTelefono();
        }
        return "Cliente no encontrado";
    }

    @SuppressWarnings("unchecked")
    private List<Cliente> leerClientes() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
            return (List<Cliente>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            return new ArrayList<>();
        }
    }

    public static void main(String[] args) {
        ArchivoCliente archivo = new ArchivoCliente("clientes.dat");

        archivo.guardaCliente(new Cliente(1, "Ana", 987654321));
        archivo.guardaCliente(new Cliente(2, "Luis", 123456789));

        System.out.println(archivo.buscarCliente(1));
        System.out.println(archivo.buscarCelularCliente(2));
    }
}
