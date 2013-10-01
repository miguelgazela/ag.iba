
<!DOCTYPE html>
<html lang="en">
  {include file="header.tpl" title="Ag.iba - Novo cliente"}

  <body>

    {include file="navbar.tpl"}

    <div class="container add_client">
      <div class="row">
        <h3>Adicionar novo cliente</h3>
          <form class="form-horizontal" role="form" action="{$BASE_URL}actions/clients/add.php" method="post">
            <div class="form-group">
              <label for="input_name" class="col-lg-2 control-label">Nome</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_name" name="name" placeholder="nome" onblur="validateClientName()">
                <span class="help-block hide">Primeiro e último nome no mínimo, sem números.</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_address" class="col-lg-2 control-label">Morada</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_address" name="address" placeholder="morada" onlbur="validateClientAddress()">
                <span class="help-block hide">Morada demasiado curta.</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_city" class="col-lg-2 control-label">Cidade</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_city" placeholder="cidade">
                <span class="help-block hide">Deve ter pelo menos 3 caracteres, sem números.</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_village" class="col-lg-2 control-label">Freguesia</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_village" placeholder="freguesia">
                <span class="help-block hide">Deve ter pelo menos 3 caracteres, sem números.</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_postal" class="col-lg-2 control-label">Código-Postal</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_postal" placeholder="####[-###]">
                <span class="help-block hide">Deve ter formato ####-### ou ####.</span>
              </div>
            </div>
            <div class="form-group">
              <label for="input_nif" class="col-lg-2 control-label">NIF/NIPC</label>
              <div class="col-lg-6">
                <input type="text" class="form-control" id="input_nif" placeholder="nif/nipc">
                <span class="help-block hide">Deve ter 9 algarismos e começar por um dos seguintes: 1,2,5,6,8 ou 9.</span>
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


    {include file="js-dependencies.tpl"}
  </body>
</html>
