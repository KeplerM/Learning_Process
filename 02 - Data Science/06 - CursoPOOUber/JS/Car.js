class Car {

    constructor(license, driver){
        this.id;
        this.license = license;
        this.driver = driver;
        this.passenger;
    }

    printDataCar() { 
        console.log(this.driver)
        //imprimirá una tabla con todos los datos.
        console.log(this.driver.name)
        console.log(this.driver.document)
        
    }
}