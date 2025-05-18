package ej1;

import java.time.LocalDate;
import java.time.Period;

public class Persona {
    String ci, nombre, apellido, celular;
    LocalDate fechaNac;

    public Persona(String ci, String nombre, String apellido, String celular, LocalDate fechaNac) {
        this.ci = ci;
        this.nombre = nombre;
        this.apellido = apellido;
        this.celular = celular;
        this.fechaNac = fechaNac;
    }

    public void mostrar() {
        System.out.println(nombre + " " + apellido + " - CI: " + ci);
    }

    public int edad() {
        return Period.between(fechaNac, LocalDate.now()).getYears();
    }
}
