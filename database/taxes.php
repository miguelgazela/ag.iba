<?php
    // initialize
    include_once($BASE_PATH.'common/DatabaseException.php');

    function getAllTaxes($type) {
        global $db;
        $query = "SELECT imposto.*, cliente.nome, cliente.id_cliente FROM imposto, cliente WHERE imposto.id_cliente = cliente.id_cliente AND imposto.tipo = ?";

        $stmt = $db->prepare($query);
        $stmt->execute(array($type));
        return $stmt->fetchAll();
    }
?>