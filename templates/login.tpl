
<!DOCTYPE html>
<html lang="en">
  {include file="header.tpl" title="Ag.iba - Signin or Signup"}

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
