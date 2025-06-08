package per1;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ArchivoEmpleado {
    private String nomA;

    public ArchivoEmpleado(String n) {
        this.nomA = n;
        crearArchivo();
    }

    private void crearArchivo() {
        File file = new File(nomA);
        if (!file.exists()) {
            try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
                oos.writeObject(new ArrayList<Empleado>());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public void guardarEmpleado(Empleado e) {
        List<Empleado> empleados = leerEmpleados();
        empleados.add(e);
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
            oos.writeObject(empleados);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public Empleado buscaEmpleado(String nombre) {
        List<Empleado> empleados = leerEmpleados();
        for (Empleado e : empleados) {
            if (e.getNombre().equals(nombre)) {
                return e;
            }
        }
        return null;
    }

    public Empleado mayorSalario(float sueldo) {
        List<Empleado> empleados = leerEmpleados();
        for (Empleado e : empleados) {
            if (e.getSalario() > sueldo) {
                return e;
            }
        }
        return null;
    }

    @SuppressWarnings("unchecked")
    private List<Empleado> leerEmpleados() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
            return (List<Empleado>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            return new ArrayList<>();
        }
    }

    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.dat");
        archivo.guardarEmpleado(new Empleado("Ana", 30, 5000));
        archivo.guardarEmpleado(new Empleado("Luis", 40, 7000));
        archivo.guardarEmpleado(new Empleado("Marta", 28, 4500));

        System.out.println("Buscar Ana: " + archivo.buscaEmpleado("Ana"));
        System.out.println("Mayor salario que 4800: " + archivo.mayorSalario(4800));
    }
}
