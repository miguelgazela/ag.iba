<?php /* Smarty version Smarty-3.1.13, created on 2013-09-26 12:23:52
         compiled from "../templates/login.tpl" */ ?>
<?php /*%%SmartyHeaderCode:188696851552440b3855f4f6-73233889%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '927222f66c1cabf1737d32d5161fdb6810b2fdcc' => 
    array (
      0 => '../templates/login.tpl',
      1 => 1380189236,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '188696851552440b3855f4f6-73233889',
  'function' => 
  array (
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.13',
  'unifunc' => 'content_52440b388fe033_00470351',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_52440b388fe033_00470351')) {function content_52440b388fe033_00470351($_smarty_tpl) {?>
<!DOCTYPE html>
<html lang="en">
  <?php echo $_smarty_tpl->getSubTemplate ("header.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array('title'=>"Ag.iba - Signin or Signup"), 0);?>


  <body>
      <div class="jumbotron">
        <div class="container">
          <h1>Ag.iba</h1>
          <div class="row">
            <div class="col-md-6">
              <p>Login em conta existente</p>
              <form role="form">
                <div class="form-group">
                  <input type="text" class="form-control" id="input_username" placeholder="username">
                  <span class="help-block hide">A block of help text that breaks onto a.</span>
                </div>
                <div class="form-group">
                  <input type="password" class="form-control" id="input_password" placeholder="password">
                  <span class="help-block hide">A block of help text that breaks onto a new line and may extend beyond one line.</span>
                </div>
                <button type="submit" class="btn btn-default">Login</button>
              </form>
            </div>
            <div class="col-md-6">
              <p>Criar uma nova conta</p>
              <form role="form">
                <div class="form-group">
                  <input type="text" class="form-control" id="input_username" placeholder="username">
                  <span class="help-block hide">A block of help text that breaks onto a.</span>
                </div>
                <div class="form-group">
                  <input type="password" class="form-control" id="input_password_2" placeholder="password">
                  <span class="help-block hide">A block of help text that breaks onto a.</span>
                </div>
                <div class="form-group">
                  <input type="password" class="form-control" id="input_password_3" placeholder="confirmar password">
                  <span class="help-block hide">A block of help text that breaks onto a.</span>
                </div>
                <button type="submit" class="btn btn-default">Criar</button>
              </form>
            </div>
          </div>
        </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
  </body>
</html>
<?php }} ?>