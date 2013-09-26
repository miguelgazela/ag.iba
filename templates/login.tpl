
<!DOCTYPE html>
<html lang="en">
  {include file="header.tpl" title="Ag.iba - Signin or Signup"}

  <body>
      <div class="jumbotron">
        <div class="container">
          <h1><strong>Ag.iba</strong></h1>
          <div class="row">
            <div class="col-md-6">
              <p>Login em conta existente</p>
              <form role="form">
                <div class="form-group">
                  <input type="text" class="form-control" id="input_username_1" placeholder="username">
                  <span class="help-block hide">Username inválido.</span>
                </div>
                <div class="form-group">
                  <input type="password" class="form-control" id="input_password_1" placeholder="password">
                  <span class="help-block hide">A block of help text that breaks onto a new line and may extend beyond one line.</span>
                </div>
                <button type="submit" class="btn btn-default">Login</button>
              </form>
            </div>
            <div class="col-md-6">
              <p>Criar uma nova conta</p>
              <form role="form">
                <div class="form-group">
                  <input type="text" data-placement="bottom" rel="tooltip" data-original-title="Mínimo 4 caracteres, sem espaços, pode conter . e _" class="form-control" id="input_username_2" placeholder="username" onblur="validateNewUsername()">
                  <span class="help-block hide">Username inválido.</span>
                </div>
                <div class="form-group">
                  <input type="password" data-placement="bottom" rel="tooltip" data-original-title="Mínimo 6 caracteres, sem espaços" class="form-control" id="input_password_2" placeholder="password" onblur="validateNewPassword()">
                  <span class="help-block hide">Password inválida.</span>
                </div>
                <div class="form-group">
                  <input type="password" class="form-control" id="input_password_3" placeholder="confirmar password" onblur="matchPasswords()">
                  <span class="help-block hide">Passwords não são iguais.</span>
                </div>
                <button type="submit" class="btn btn-default">Criar</button>
              </form>
            </div>
          </div>
        </div>
    </div>

    {include file="js-dependencies.tpl"}
  </body>
</html>
