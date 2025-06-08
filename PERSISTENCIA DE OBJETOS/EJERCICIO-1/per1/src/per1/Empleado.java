package per1;

import java.io.Serializable;

public class Empleado implements Serializable {
    private String nombre;
    private int edad;
    private float salario;

    public Empleado(String nombre, int edad, float salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public String getNombre() {
        return nombre;
    }

    public float getSalario() {
        return salario;
    }

    public String toString() {
        return "Empleado(nombre=" + nombre + ", edad=" + edad + ", salario=" + salario + ")";
    }
}
