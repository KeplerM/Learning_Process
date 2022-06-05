package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123"), "Chevrolet", "Sonic" );
        //uberX.passenger=4;
        uberX.setPassenger(4);
        uberX.printDataCar(); 
        
        UberVan UberVan = new UberVan("FGH345", new Account("Andres Herrera", "AND123"));  
        UberVan.setPassenger(6);
        UberVan.printDataCar(); 
        // Car car2 = new Car("QWE567", new Account("Andrea Herrera","AND456"));
        // car2.Passengen=3;
        // car2.printDataCar();
    }
}