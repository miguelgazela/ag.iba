<?php

    // initialize
    include_once($BASE_PATH.'common/DatabaseException.php');

    function getUserByUsername($username) {
        global $db;
        $stmt = $db->prepare("SELECT id_utilizador FROM utilizador WHERE username = ?");
        $stmt->execute(array($username));
        return $stmt->fetch();
    }

    function createAccount($username, $pass_hash) {
        global $db;
        $errors = new DatabaseException();

        try {
            $stmt = $db->prepare("INSERT INTO utilizador (username, pass_hash, tipo) VALUES (?, ?, 1)");
            $stmt->execute(array($username, $pass_hash));
        } catch(Exception $e) {
            $errors->addError('utilizador', 'error processing insert into table utilizador');
            $errors->addError('exception', $e->getMessage());
            throw($errors);
        }
    }
?>