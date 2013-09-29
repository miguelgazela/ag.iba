<?php
    include_once('../../common/init.php');
    include_once($BASE_PATH . 'database/users.php');

    $username = $_POST['username'];
    $password = $_POST['password'];

    // Never store passwords in clear text!
    $user = getUser($username, sha1($password));

    if($user) {
        if ($user['tipo'] != 1) {
            $_SESSION['s_username'] = $username;
            $_SESSION['s_user_permission'] = $user['tipo'];
            $_SESSION['s_user_id'] = $user['id_utilizador'];
            header("Location: $BASE_URL" . "index.php");
        } else {
            $_SESSION['s_error']['login'] = "inactive_account";
            $_SESSION['s_values']['username_login'] = $username;
            header("Location: $BASE_URL" . "pages/login.php");
        }
    } else {
        $_SESSION['s_error']['login'] = "invalid_access";
        $_SESSION['s_values']['username_login'] = $username;
        header("Location: $BASE_URL" . "pages/login.php");
    }
?>