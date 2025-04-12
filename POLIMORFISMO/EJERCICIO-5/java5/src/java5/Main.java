package java5;
import java.util.ArrayList;
import java.util.List;


public class Main {
    public static void main(String[] args) {
        Oficina of1 = new Oficina(4, 2, 1);
        Oficina of2 = new Oficina(6, 3, 2);

        Aula aula1 = new Aula("Aula Magna", 100, 95);
        Aula aula2 = new Aula("Aula B", 40, 38);

        Laboratorio lab1 = new Laboratorio("Lab Física", 30, 15, 20);

        List<Ambiente> ambientes = new ArrayList<>();
        ambientes.add(of1);
        ambientes.add(of2);
        ambientes.add(aula1);
        ambientes.add(aula2);
        ambientes.add(lab1);

        for (Ambiente amb : ambientes) {
            amb.mostrar();
            System.out.println("Total muebles: " + amb.cantidadMuebles());
            System.out.println("************************************************************");
        }
    }
}