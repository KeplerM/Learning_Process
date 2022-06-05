package Java;

public class Car {
    private Integer ID;
    private String License; 
    private Account Driver;
    protected Integer passenger;
    
    public Car(String License, Account Driver){
        this.License = License;
        this.Driver = Driver;
        // passenger =3;
        // System.out.println("passenger: " + passenger);

    }

    void printDataCar() {
        if(passenger != null){

        }
        System.out.println("License: " + License + " Name Driver: " + Driver.Name + " Passengers:" + passenger);
    }

    public Integer getPassenger(){
        return passenger;
    }

    public void setPassenger(Integer passenger){
        if(passenger == 4){
            this.passenger=passenger;
        }
        else {
            System.out.println("Necesitas asignar cuatro pasajeros");
        }
    }

    public Integer getID() {
        return ID;
    }

    public void setID(Integer iD) {
        ID = iD;
    }

    public String getLicense() {
        return License;
    }

    public void setLicense(String license) {
        License = license;
    }

    public Account getDriver() {
        return Driver;
    }

    public void setDriver(Account driver) {
        Driver = driver;
    }

    

    
}
