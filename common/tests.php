<?php
	include_once('init.php');
    include_once("../database/taxes.php");

    $taxes = getAllTaxes(1);

    echo (count($taxes));
    echo "Hello world!";
?>