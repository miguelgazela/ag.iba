<?php
    // initialize
    include_once('../../common/init.php');
    include_once($BASE_PATH . 'database/users.php');
    include_once($BASE_PATH . 'common/DatabaseException.php');

    function validatePassword($pass) {
        if(preg_match('/^[a-zA-Z0-9.,-:;_!#$%&*~]{6,30}$/',$pass)) {
            return true;
        }
        return false;
    }

    function validateUsername($username){
        if(preg_match('/^[a-z0-9A-Z._]{4,64}$/', $username)) {
            return true;
        }
        return false;
    }

    if(!isset($_SESSION['s_username'])) {
        $errors = new DatabaseException();

        if(!isset($_POST['username'])) {
            $errors->addError('username', 'no_username');
        }
        if(!isset($_POST['password_2'])) {
            $errors->addError('password_2', 'no_password_2');
        }
        if(!isset($_POST['password_3'])) {
            $errors->addError('password_3', 'no_password_3');
        }

        // check if this works

        returnIfHasErrors($errors, "pages/login.php");

        $username = $_POST['username'];
        $pass2 = $_POST['password_2'];
        $pass3 = $_POST['password_3'];

        // validate values received
        if(!validateUsername($username)) {
            $errors->addError('username', 'invalid');
        }
        if(!validatePassword($pass2)) {
            $errors->addError('password_2', 'invalid');
        }
        if($pass2 != $pass3) {
            $errors->addError('password_3', 'no_match');
        }

        // check if user already has an account
        if(getUserByUsername($username)) {
            $errors->addError('username', 'username_taken');
        }

        returnIfHasErrors($errors, "pages/login.php");

        // add the new user to the database
        try {
            createAccount($username, sha1($pass1));
            $_SESSION['s_error']['message'] = "account_created";  
            header("Location: $BASE_URL"."pages/login.php");
        } catch(DatabaseException $e) {
            returnIfHasErrors($errors, "pages/login.php");
        }
    }
?>