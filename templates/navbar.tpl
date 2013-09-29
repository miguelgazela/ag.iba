<!-- Fixed navbar -->
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
        <li class="dropdown _clients">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown"><strong>CLIENTES</strong> <b class="caret"></b></a>
          <ul class="dropdown-menu">
            <li><a href="{$BASE_URL}pages/clients/list.php">Ver clientes</a></li>
            <li><a href="{$BASE_URL}actions/clients/add.php">Adicionar cliente</a></li>
            <!--<li><a href="#">Outro</a></li>-->
          </ul>
        </li>
        <li class="dropdown _taxes">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown"><strong>IMPOSTOS</strong> <b class="caret"></b></a>
          <ul class="dropdown-menu">
            <li><a href="{$BASE_URL}pages/taxes/list.php">Ver impostos</a></li>
            <li><a href="{$BASE_URL}actions/taxes/add.php">Adicionar imposto</a></li>
            <!--<li><a href="#">Outro</a></li>-->
          </ul>
        </li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown"><strong>OUTROS</strong> <b class="caret"></b></a>
          <ul class="dropdown-menu">
            <li><a href="#">Reportar erro</a></li>
            <li><a href="#">Enviar sugestão</a></li>
            <!--<li><a href="#">Outro</a></li>-->
          </ul>
      </ul>
      {if $s_username != ""}
      <ul class="nav navbar-nav navbar-right">
        <li><a href="{$BASE_URL}actions/auth/logout.php"><span class="glyphicon glyphicon-log-out"></span> <strong>Logout</strong></a></li>
      </ul>
      {/if}
    </div><!--/.nav-collapse -->
  </div>
</div>