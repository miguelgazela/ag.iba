<?php
    // initialize
    include_once("../../common/init.php");
    include_once($BASE_PATH . "database/users.php");

    if(isset($_SESSION['s_username'])) {
        $smarty->display("clients/add.tpl");
    } else {
        header("Location: $BASE_URL"."pages/login.php");
    }
?>