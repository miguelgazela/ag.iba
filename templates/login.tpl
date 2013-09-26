
<!DOCTYPE html>
<html lang="en">
  {include file="header.tpl" title="Ag.iba - Signin or Signup"}

  <body>
      {if $s_error.message != ""}
      <p>{$s_error.message}</p>
      {/if}
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
              <form role="form" id="signup_form" action="{$BASE_URL}actions/auth/signup.php" method="post">
                {if $s_error.username == ""}
                <div class="form-group">
                {else}
                <div class="form-group has-error">
                {/if}
                  <input type="text" data-placement="bottom" rel="tooltip" data-original-title="Mínimo 4 caracteres, sem espaços, pode conter . e _" class="form-control" id="input_username_2" placeholder="username" name="username" onblur="validateNewUsername()" value="{$s_values.username}">
                  {if $s_error.username == "no_username" || $s_error.username == "invalid"}
                  <span class="help-block">Username inválido.</span>
                  {elseif $s_error.username == "username_taken"}
                  <span class="help-block">Já existe uma conta com esse username.</span>
                  {else}
                  <span class="help-block hide">Username inválido.</span>
                  {/if}
                </div>

                {if $s_error.password_2 == "invalid"}
                <div class="form-group has-error">
                {else}
                <div class="form-group">
                {/if}
                  <input type="password" data-placement="bottom" rel="tooltip" data-original-title="Mínimo 6 caracteres, sem espaços" class="form-control" id="input_password_2" name="password_2" placeholder="password" onblur="validateNewPassword()" value="{$s_values.password_2}">
                  {if $s_error.password_2 == "invalid"}
                  <span class="help-block">Password inválida.</span>
                  {else}
                  <span class="help-block hide">Password inválida.</span>
                  {/if}
                </div>
                {if $s_error.password_3 == "no_match"}
                <div class="form-group has-error">
                {else}
                <div class="form-group">
                {/if}
                  <input type="password" class="form-control" id="input_password_3" placeholder="confirmar password" name="password_3" onblur="matchPasswords()" value="{$s_values.password_3}">
                  {if $s_error.password_3 == "no_match"}
                  <span class="help-block">Passwords não são iguais.</span>
                  {else}
                  <span class="help-block hide">Passwords não são iguais.</span>
                  {/if}
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
