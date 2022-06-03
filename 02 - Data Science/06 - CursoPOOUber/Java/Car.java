package Java;

public class Car {
    Integer ID;
    String License; 
    Account Driver;
    Integer Passengen;
    
    public Car(String License, Account Driver){
        this.License = License;
        this.Driver = Driver;

    }

    public void printDataCar() {
        System.out.println("License: " + License + " Name Driver: " + Driver.Name + " Passengers:" + Passengen);
    }

    
}
