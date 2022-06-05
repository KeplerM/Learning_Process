package Java;

import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car{

    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial; 
    //private Integer passenger;

    public UberVan(String License, Account Driver){//, Map<String, Map<String, Integer>> typeCarAccepted
        super(License, Driver);
        //this.typeCarAccepted = typeCarAccepted;
        // this.seatsMaterial = seatsMaterial;

                       
    }

    // public UberVan(String License, Account Driver, Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterial){
    //         super(License, Driver);
    //         this.typeCarAccepted = typeCarAccepted;
    //         this.seatsMaterial = seatsMaterial;

    //}
    
    @Override
    public void setPassenger(Integer passenger) {
        // TODO Auto-generated method stub
        if(passenger == 6){
            this.passenger=passenger;
        }
        else {
            System.out.println("Necesitas asignar 6 pasajeros");
        }
    }
}
