<?php
require_once('account.php');
class Car{
    public $id=integer;
    public $license=string;
    public $driver=string;
    public $passenger=integer;

    public function __construct($license, $driver){
        $this->license = $license;
        $this->driver  = $driver;
    }

    public function PrintDataCar(){
        echo"license: $this->license, Driver: {$this->driver->name}, document: {$this->driver->document}";
        
    }
}