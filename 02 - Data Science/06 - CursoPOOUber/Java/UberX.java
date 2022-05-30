package Java;

public class UberX extends Car {
    String brand; 
    String model;

    public UberX(String License, Account Driver, String brand, String model){
        super(License, Driver);
        this.brand = brand;
        this.model = model;

        }
}