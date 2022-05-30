package Java;

import java.util.ArrayList;
import java.util.Map;

public class UberBlack extends Car {

    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial; 

    public UberBlack(String License, Account Driver, Map<String, Map<String,Integer>> typeCarAccepted, ArrayList<String> seatsMaterial){
        super(License, Driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
                
        }
}
