<?php
require_once("Car.php");
require_once("uberX.php");
require_once("Account.php");
require_once("UberPool.php");
require_once("UberVan.php");

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Spark");
$uberX->setPassenger(passenger:4);
$uberX->printDataCar();

$uberPool = new UberPool("TYU567", new Account("Andrea Ferran", "ANDA765"), "Dodge", "Attitude");
$uberPool->printDataCar();

$uberVan = new UberVan("OJL345", new Account("Raul Ramírez", "AND456"), "Nissan", "Versa");
$uberVan->setPassenger(passenger:6);
$uberVan->printDataCar();

?>
