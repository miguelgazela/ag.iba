<?php /* Smarty version Smarty-3.1.13, created on 2013-10-20 23:55:33
         compiled from "/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/clients/add.tpl" */ ?>
<?php /*%%SmartyHeaderCode:402644644524ae76cad2df9-80697671%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '6565778a90bb3042ab419f3b45d5c7f872730a22' => 
    array (
      0 => '/Users/migueloliveira/Dropbox/projects/agiva-3.0/templates/clients/add.tpl',
      1 => 1382306131,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '402644644524ae76cad2df9-80697671',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.13',
  'unifunc' => 'content_524ae76cb61273_14934997',
  'variables' => 
  array (
    'BASE_URL' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_524ae76cb61273_14934997')) {function content_524ae76cb61273_14934997($_smarty_tpl) {?>
<!DOCTYPE html>
<html lang="en">
  <?php echo $_smarty_tpl->getSubTemplate ("header.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array('title'=>"Ag.iba - Novo cliente"), 0);?>


  <body>

    <?php echo $_smarty_tpl->getSubTemplate ("navbar.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array(), 0);?>


    <div class="container add_client">
      <div class="row">
        <h3>Adicionar novo cliente</h3>
          <form class="form-horizontal" id="add_client_form" role="form" action="<?php echo $_smarty_tpl->tpl_vars['BASE_URL']->value;?>
actions/clients/add.php" method="post">
            <div class="form-group">
              <label for="input_name" class="col-lg-2 control-label">Nome</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_name" name="name" placeholder="nome" onblur="validateClientName()">
                <span class="help-block hide">Primeiro e último nome no mínimo, sem números</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_address" class="col-lg-2 control-label">Morada</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_address" name="address" placeholder="morada" onblur="validateClientAddress()">
                <span class="help-block hide">Morada demasiado curta</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_city" class="col-lg-2 control-label">Cidade</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_city" placeholder="cidade" name="city" onblur="validateClientCity()">
                <span class="help-block hide">Deve ter pelo menos 3 caracteres, sem números</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_village" class="col-lg-2 control-label">Freguesia</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_village" name="village" onblur="validateClientVillage()" placeholder="freguesia">
                <span class="help-block hide">Deve ter pelo menos 3 caracteres, sem números</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_postal" class="col-lg-2 control-label">Código-Postal</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_postal" name="postal" onblur="validateClientPostal()" placeholder="código postal">
                <span class="help-block hide">Deve ter formato #### ou ####-###</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_nif" class="col-lg-2 control-label">NIF/NIPC</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_nif" name="nif" onblur="validateClientNif()" onkeyup="checkNifType()" placeholder="nif/nipc">
                <span class="help-block hide">Deve ter 9 algarismos e começar por um dos seguintes: 1, 2, 5, 6, 7, 8 ou 9</span>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-offset-2 col-lg-6">
                <button type="submit" class="btn btn-default">Gravar cliente</button>
              </div>
            </div>
          </form>
      </div>
    </div> <!-- /container -->

    <?php echo $_smarty_tpl->getSubTemplate ("js-dependencies.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array(), 0);?>

  </body>
</html>
<?php }} ?>