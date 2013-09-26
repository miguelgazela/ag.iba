<?php
	include_once('init.php');
    include_once("../database/taxes.php");

    echo "deu";

    $result = $db->query("SELECT * from utilizador");
    
    echo $result->fetch();
?>