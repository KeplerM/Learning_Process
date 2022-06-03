package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123"), "Chevrolet", "Sonic" );
        uberX.Passengen=4;
        uberX.printDataCar(); 
        
        // Car car2 = new Car("QWE567", new Account("Andrea Herrera","AND456"));
        // car2.Passengen=3;
        // car2.printDataCar();
    }
}