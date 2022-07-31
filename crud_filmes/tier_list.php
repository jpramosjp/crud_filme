<?php
session_start();
try {

?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/style.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

    </head>
    <body onload="table();">
        <table id="filmes_usuarios" width = '100px' border = '1'>
        </table>
        <div id="myModal" class="modal">
            <div class="modal-content">
                <div class="modal-header">
                    <span class="close" onclick="fecharModal()">&times;</span>
                    <h2 id='nome_filme'></h2>
                </div>
                <div class="modal-body">
                    <p id='detalhes_filme'></p>
                    <p id = "tipo_filme"></p>
                </div>
                <div class="modal-footer">
                    <h3 id = 'data_lancamento_filme'></h3>
                </div>
            </div>
        </div>
        <script type="text/javascript" src="js/tier_list.js"></script>
    </body>
</html>
<?php
}
catch (Exception $e) {
    trigger_error($e);
    return false;
}    


?>
