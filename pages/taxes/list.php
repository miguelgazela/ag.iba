<?php
    // initialize
    include_once('../../common/init.php');

    // include needed database functions
    include_once($BASE_PATH.'database/taxes.php');

    if(isset($_SESSION['s_username'])) {

        // 1 -> Escritorio, 2 -> Casa

        if(!isset($_GET['t']) || !is_numeric($_GET['t'])) {
            $_GET['t'] = 1;
        } else {
            if($_GET['t'] == 2 && $_SESSION['s_permission'] != 3) {
                $_GET['t'] = 1;
            } else if($_GET['t'] != 1 && $_GET['t'] != 2) {
                $_GET['t'] = 1;
            }
        }

        // fetch taxes
        $taxes = getAllTaxes($_GET['t']);

        foreach($taxes as &$tax) {
            $tax['nome'] = htmlspecialchars(stripslashes($tax['nome']));
            $tax['viatura'] = htmlspecialchars(stripslashes($tax['marca'])) . " " . htmlspecialchars(stripslashes($tax['modelo']));
            $tax['matricula'] = htmlspecialchars(stripslashes($tax['matricula']));
            $tax['data_matricula'] = getNormalDate($tax['data_matricula']);
            $tax['data_pagamento'] = getNormalDate($tax['data_pagamento']);
        }

        // fetch latest activities

        // assign data to smarty and display template
        $smarty->assign('taxes', $taxes);
        $smarty->assign('taxes_counter', count($taxes));
        $smarty->display("taxes/list.tpl");
    } else {
        header("Location: $BASE_URL"."pages/login.php");
    }
?>