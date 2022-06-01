<?php
require_once('Car.php');
class UberVan extends Car {
    public $typeCarAccepted;
    public $seatsMaterials;

        public function __construct($license, $driver, $typeCarAccepted, $seatsMaterials){
            parent::__construct($license, $driver);
            $this->typeCarAccepted = $typeCarAccepted;
            $this->seatsMaterials  = $seatsMaterials;
        }


        
}
?>