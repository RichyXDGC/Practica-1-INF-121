package ejercicio1;

public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public void saludar() {
        System.out.println("Hola, soy " + this.nombre + " de " + this.ciudad);
    }

    public boolean mayor() {
        return this.edad >= 18;
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Roger", 20, "Brasil");
        Persona persona2 = new Persona("Luis", 15, "Chile");
        Persona persona3 = new Persona("Ana", 33, "Bolivia");

        persona1.saludar();
        persona2.saludar();
        persona3.saludar();

        System.out.println(persona1.nombre + " es mayor de edad: " + persona1.mayor());
        System.out.println(persona2.nombre + " es mayor de edad: " + persona2.mayor());
        System.out.println(persona3.nombre + " es mayor de edad: " + persona3.mayor());
    }
}