<?php
require_once("Car.php");
require_once("uberX.php");
require_once("Account.php");
require_once("UberPool.php");

$uberX = new uberX("CVB123", new Account("Andres", "ANDA"), "chevrolet", "aveo");
?>
