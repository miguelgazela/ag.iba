<?php /* Smarty version Smarty-3.1.13, created on 2013-09-29 09:30:15
         compiled from "/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/header.tpl" */ ?>
<?php /*%%SmartyHeaderCode:20322947565244612e0f1440-20451122%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '6fabce0bbbf403585e2a13cb4c40fbaf41f2caaa' => 
    array (
      0 => '/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/header.tpl',
      1 => 1380360161,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '20322947565244612e0f1440-20451122',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.13',
  'unifunc' => 'content_5244612e1b4218_98867572',
  'variables' => 
  array (
    'title' => 0,
    'BASE_URL' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5244612e1b4218_98867572')) {function content_5244612e1b4218_98867572($_smarty_tpl) {?><head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="@miguelgazela">
    <link rel="shortcut icon" href="../favicon.png"> <!-- no resource for now -->

    <title><?php echo (($tmp = @$_smarty_tpl->tpl_vars['title']->value)===null||$tmp==='' ? "Ag.iba" : $tmp);?>
</title>

    <!-- Bootstrap core CSS -->
    <link href="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
css/main.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="../../assets/js/html5shiv.js"></script>
      <script src="../../assets/js/respond.min.js"></script>
    <![endif]-->
</head><?php }} ?>