<?php /* Smarty version Smarty-3.1.13, created on 2013-10-20 10:44:42
         compiled from "/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/login.tpl" */ ?>
<?php /*%%SmartyHeaderCode:8349882205244612de9fb05-51549537%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'bfbb633dfc4223961b5219f025f4bb2455c5f9a1' => 
    array (
      0 => '/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/login.tpl',
      1 => 1382258610,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '8349882205244612de9fb05-51549537',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.13',
  'unifunc' => 'content_5244612e0ddd84_84538171',
  'variables' => 
  array (
    'BASE_URL' => 0,
    's_error' => 0,
    's_values' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5244612e0ddd84_84538171')) {function content_5244612e0ddd84_84538171($_smarty_tpl) {?><!DOCTYPE html>
<html lang="en">
  <?php echo $_smarty_tpl->getSubTemplate ("header.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array('title'=>"Ag.iba"), 0);?>


  <body>
      <div class="jumbotron">
        <div class="container">
          <h1><strong>Ag.iba</strong></h1>
          <div class="row">
            <div class="col-md-6">
              <p>Login em conta existente</p>
              <form role="form" id="signin_form" action="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
actions/auth/login.php" method="post">
                <?php if ($_smarty_tpl->tpl_vars['s_error']->value['login']=="invalid_access"){?>
                <div class="form-group has-error">
                <?php }else{ ?>
                <div class="form-group">
                <?php }?>
                  <input type="text" class="form-control" id="input_username_1" placeholder="username" name="username" onblur="validateSignInUsername()" value="<?php echo $_smarty_tpl->tpl_vars['s_values']->value['username_login'];?>
">
                  <span class="help-block hide">Username inválido.</span>
                </div>
                <?php if ($_smarty_tpl->tpl_vars['s_error']->value['login']=="invalid_access"){?>
                <div class="form-group has-error">
                <?php }else{ ?>
                <div class="form-group">
                <?php }?>
                  <input type="password" class="form-control" id="input_password_1" placeholder="password" name="password" onblur="validateSignInPassword()">
                  <?php if ($_smarty_tpl->tpl_vars['s_error']->value['login']=="invalid_access"){?>
                   <span class="help-block">Username inexistente ou password inválida.</span>
                   <?php }else{ ?>
                   <span class="help-block hide">Password inválida.</span>
                  <?php }?>
                </div>
                <?php if ($_smarty_tpl->tpl_vars['s_error']->value['login']=="inactive_account"){?>
                <p>Esta conta ainda não foi ativada.</p>
                <?php }else{ ?>
                <button type="submit" class="btn btn-default">Login</button>
                <?php }?>
              </form>
            </div>
            <div class="col-md-6">
              <p>Criar uma nova conta</p>
              <form role="form" id="signup_form" action="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
actions/auth/signup.php" method="post">
                <?php if ($_smarty_tpl->tpl_vars['s_error']->value['username']==''){?>
                <div class="form-group">
                <?php }else{ ?>
                <div class="form-group has-error">
                <?php }?>
                  <input type="text" data-placement="bottom" rel="tooltip" data-original-title="Mínimo 4 caracteres, sem espaços, pode conter . e _" class="form-control" id="input_username_2" placeholder="username" name="username" onblur="validateNewUsername()" value="<?php echo $_smarty_tpl->tpl_vars['s_values']->value['username'];?>
">
                  <?php if ($_smarty_tpl->tpl_vars['s_error']->value['username']=="no_username"||$_smarty_tpl->tpl_vars['s_error']->value['username']=="invalid"){?>
                  <span class="help-block">Username inválido.</span>
                  <?php }elseif($_smarty_tpl->tpl_vars['s_error']->value['username']=="username_taken"){?>
                  <span class="help-block">Já existe uma conta com esse username.</span>
                  <?php }else{ ?>
                  <span class="help-block hide">Username inválido.</span>
                  <?php }?>
                </div>

                <?php if ($_smarty_tpl->tpl_vars['s_error']->value['password_2']=="invalid"){?>
                <div class="form-group has-error">
                <?php }else{ ?>
                <div class="form-group">
                <?php }?>
                  <input type="password" data-placement="bottom" rel="tooltip" data-original-title="Mínimo 6 caracteres, sem espaços" class="form-control" id="input_password_2" name="password_2" placeholder="password" onblur="validateNewPassword()" value="<?php echo $_smarty_tpl->tpl_vars['s_values']->value['password_2'];?>
">
                  <?php if ($_smarty_tpl->tpl_vars['s_error']->value['password_2']=="invalid"){?>
                  <span class="help-block">Password inválida.</span>
                  <?php }else{ ?>
                  <span class="help-block hide">Password inválida.</span>
                  <?php }?>
                </div>
                <?php if ($_smarty_tpl->tpl_vars['s_error']->value['password_3']=="no_match"){?>
                <div class="form-group has-error">
                <?php }else{ ?>
                <div class="form-group">
                <?php }?>
                  <input type="password" class="form-control" id="input_password_3" placeholder="confirmar password" name="password_3" onblur="matchPasswords()" value="<?php echo $_smarty_tpl->tpl_vars['s_values']->value['password_3'];?>
">
                  <?php if ($_smarty_tpl->tpl_vars['s_error']->value['password_3']=="no_match"){?>
                  <span class="help-block">Passwords não são iguais.</span>
                  <?php }else{ ?>
                  <span class="help-block hide">Passwords não são iguais.</span>
                  <?php }?>
                </div>
                <?php if ($_smarty_tpl->tpl_vars['s_values']->value['message']=="account_created"){?>
                <p style="color: #3acf93;">Conta criada com sucesso.</p>
                <?php }else{ ?>
                <button type="submit" class="btn btn-default">Criar</button>
                <?php }?>
              </form>
            </div>
          </div>
        </div>
    </div>

    <?php echo $_smarty_tpl->getSubTemplate ("js-dependencies.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array(), 0);?>

  </body>
</html>
<?php }} ?>