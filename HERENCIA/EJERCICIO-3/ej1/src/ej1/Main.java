package ej1;
import java.time.LocalDate;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Estudiante> estudiantes = new ArrayList<>();
        estudiantes.add(new Estudiante("123", "Ana", "López", "789456", LocalDate.of(1997, 5, 3), "RU001", LocalDate.of(2020, 2, 1), 8));
        estudiantes.add(new Estudiante("124", "Luis", "Pérez", "789457", LocalDate.of(2002, 6, 10), "RU002", LocalDate.of(2022, 3, 1), 4));
        estudiantes.add(new Estudiante("133", "Yoni", "Martínez", "123450", LocalDate.of(1999, 4, 20), "RU003", LocalDate.of(2020, 3, 1), 3));

        System.out.println("Estudiantes mayores de 25 años:");
        for (Estudiante e : estudiantes) {
            if (e.edad() > 25) {
                e.mostrar();}
        }
        List<Docente> docentes = Arrays.asList(
        	    new Docente("456", "Carlos", "Ramírez", "123456", LocalDate.of(1980, 1, 1), "NIT01", "Ingeniero", "Sistemas", "M"),
        	    new Docente("457", "Marta", "García", "123457", LocalDate.of(1985, 7, 15), "NIT02", "Licenciada", "Educación", "F"),
        	    new Docente("458", "Jorge", "Martínez", "123458", LocalDate.of(1975, 3, 20), "NIT03", "Ingeniero", "Civil", "M")
);
        	Docente mayorDocente = null;
        	for (Docente d : docentes) {
        	    if (d.profesion.equals("Ingeniero") && d.sexo.equals("M")) {
        	        if (mayorDocente == null || d.edad() > mayorDocente.edad()) {
        	            mayorDocente = d;
        	        }
        	    }
        	}

        	System.out.println("Docente varón más viejo con profesión 'Ingeniero':");
        	if (mayorDocente != null) {
        	    mayorDocente.mostrar();
        	}
        	System.out.println("Personas con el mismo apellido:");

        	for (Estudiante est : estudiantes) {
        	    for (Docente doc : docentes) {
        	        if (est.apellido.equals(doc.apellido)) {
        	            System.out.println("Coincidencia:");
        	            est.mostrar();
        	            doc.mostrar();
        	        }
        	    }
        	}


    }
}