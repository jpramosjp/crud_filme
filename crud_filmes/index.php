<?php
require_once('classe/repositorios/UsuarioRepo.php');
session_start();
$usuarioRepo = new UsuarioRepo();

$acao = isset($_POST['acao']) ? $_POST['acao'] : '' ;
if($acao == '') {
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script type="text/javascript" src="js/index.js"></script>
    </head>
    <body>
   
        <div id = "caixa">
            <form method="post" id="formulario">
               <label> Login: </label>
               <input id = "login" name = 'usuario'> </input>
               <br>
               <label> Senha: </label>
               <input type = "password" id = "senha" name = 'senha'> </input>
               <br>
               <input type="submit" name = 'acao' value="Entrar"> 
               <button type="button" onclick="Mudarestado('caixa','divCadastro')">Cadastrar</button>
            </form>
        </div>

        <div id="divCadastro" style="display:none;">
            <form method="post" id ="cadastroFormulario">
                <label> Nome: </label>
                <input type="text" name="nome"></input>
                <br>
                <label>Nome de acesso: </label>
                <input type="text" name="usuario"></input>
                <br>
                <label>Senha: </label>
                <input type="text" name="senha"></input>
                <br>
                <input type="submit" name = 'acao' value="Cadastrar"> 
               <button type="button" onclick="Mudarestado('divCadastro','caixa')">Logar</button>
            </form>
        </div>

    </body>
</html>
<?php }
if ($acao == 'Entrar') {
    $parametros = [
        "nome_acesso" => $_POST['usuario'],
        "senha" => $_POST['senha']
    ];
    $retornoUsuario = $usuarioRepo->pegarUsuario($parametros);
    if ($retornoUsuario != false && count($retornoUsuario) > 0) {

        $_SESSION['usuario'] = $retornoUsuario[0][0];
        header("Location: tier_list.php");
    }
}

if($acao == 'Cadastrar') {
    $parametros = [
        "nome_acesso" => $_POST['usuario'],
        "nome" =>$_POST['nome'],
        "senha" => $_POST['senha']
    ];
    $retornoUsuario = $usuarioRepo->cadastrarUsuario($parametros);
    header("Refresh:0; url=index.php");

}
?>
