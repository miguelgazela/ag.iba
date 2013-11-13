<?php /* Smarty version Smarty-3.1.13, created on 2013-10-20 23:38:49
         compiled from "/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/navbar.tpl" */ ?>
<?php /*%%SmartyHeaderCode:1805843046524822938dba73-91903260%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '5c86d1a44b702977f85f28ac59327755d600d154' => 
    array (
      0 => '/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/navbar.tpl',
      1 => 1382305106,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '1805843046524822938dba73-91903260',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.13',
  'unifunc' => 'content_52482293924392_05188462',
  'variables' => 
  array (
    'BASE_URL' => 0,
    's_username' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_52482293924392_05188462')) {function content_52482293924392_05188462($_smarty_tpl) {?><!-- Fixed navbar -->
<div class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Ag.iba</a>
    </div>
    <div class="navbar-collapse collapse">
      <ul class="nav navbar-nav">
        <li><a href="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
pages/clientes/list.php">Ver Clientes</a></li>
        <li><a href="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
pages/clients/add.php">Adicionar cliente</a></li>
        <li><a href="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
pages/taxes/list.php">Ver impostos</a></li>
        <li><a href="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
pages/taxes/add.php">Adicionar imposto</a></li>
      </ul>
      <?php if ($_smarty_tpl->tpl_vars['s_username']->value!=''){?>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
actions/auth/logout.php"><span class="glyphicon glyphicon-log-out"></span> <strong>Logout</strong></a></li>
      </ul>
      <?php }?>
    </div><!--/.nav-collapse -->
  </div>
</div><?php }} ?>