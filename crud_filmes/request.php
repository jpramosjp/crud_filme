<?php
require_once('classe/repositorios/StatusRepo.php');
require_once('classe/repositorios/UsuarioFilme.php');
session_start();
try {
    $statusRepo = new StatusRepo;
    $usuarioFilmeRepo = new UsuarioFilme();

    $retornoStatus = $statusRepo->pegarStatus();
    if ($retornoStatus === false) {
        throw new Exception("Erro na query");
    }
    $retornoUsuarioFilme = $usuarioFilmeRepo->pegarUsuarioFilme($_SESSION['usuario']);
    if ($retornoUsuarioFilme === false) {
        throw new Exception("Erro na query");
    }
?>
<!DOCTYPE html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    </head>

    <body onload = 'pegarFilmeUsuario()'>
        <table width = '100px' border = '1'>
        <thead>
            <tr>
                 <?php foreach ($retornoStatus as $key => $valores) {
                     ?> 
                     <td> <?php echo $valores[1] ?> </td>
                     <?php
                 }
                 ?>
             </tr>
        </thead>
        <tbody id = 'teste'>
            <tr>
                <?php foreach ($retornoStatus as $key => $valores) {
                     ?> 
                     <td id="<?php echo $valores[0] ?>" ondrop="drop(event)" ondragover="allowDrop(event)">
                        <div id= "coluna_<?php echo $key ?>">
                            <?php
                                foreach ($retornoUsuarioFilme as $key2 => $filme) {
                                    if($filme[3] == $valores[0]) {
                                        ?>
                                            <div style = 'border: 2px solid red; padding:5px;' ondrop='drop(event)' draggable='true' ondragstart='drag(event)' id = "filme_<?php echo $filme[0]?>" onclick = "abrirModal(<?php echo $filme[4]?>)">
                                                <img src="data:image/png;base64,<?php echo $filme[2] ?>" width="150" height="150">
                                            </div>
                                        <?php
                                    }
                                }  
                            ?>
                        </div > 
                    </td>
                     <?php
                    }
                ?>
            </tr>
        </tbody>
        </table>
        <script type="text/javascript" src="js/request.js"></script>
    </body>
</html>
<?php
}
catch (Exception $e) {
    trigger_error($e);
    return false;
}    


?>
