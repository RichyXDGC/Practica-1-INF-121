package hern1;

public class Main {
    public static void main(String[] args) {
        Coche c1 = new Coche("Toyota", "Corolla", 2025, 20000, 4, "Gasolina");
        Coche c2 = new Coche("Ford", "Explorer", 2025, 5, 30000, "Diesel");
        Moto m1 = new Moto("Yamaha", "R1", 2025, 15000, 1000, "4T");

        System.out.println("---- Coche 1 ----");
        c1.mostrarInfo();

        System.out.println("\n---- Coche 2 ----");
        c2.mostrarInfo();

        System.out.println("\n---- Moto ----");
        m1.mostrarInfo();

        // Coches con más de 4 puertas
        System.out.println("\n--- Coches con más de 4 puertas ---");
        for (Coche coche : new Coche[]{c1, c2}) {
            if (coche.getNumPuertas() > 4) {
                coche.mostrarInfo();
            }
        }

        // Vehículos del año 2025
        System.out.println("\n--- Vehículos del año 2025 ---");
        for (Vehiculo v : new Vehiculo[]{c1, c2, m1}) {
            if (v.año == 2025) {
                v.mostrarInfo();
            }
        }
    }
}