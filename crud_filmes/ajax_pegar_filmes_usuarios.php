<?php
header("Content-Type: text/html; charset=UTF-8",true);
require_once('classe/repositorios/UsuarioFilme.php');
require_once('classe/repositorios/FilmeRepo.php');
session_start();
try {
    $usuarioFilmeRepo = new UsuarioFilme();
    $acao = isset($_POST['acao']) ? $_POST['acao'] : '';
    $filmeRepo = new FilmeRepo();
    switch ($acao) {
        case 'trazerDados' :

            $retornoUsuarioFilme = $usuarioFilmeRepo->pegarUsuarioFilme($_SESSION['usuario']);
            if ($retornoUsuarioFilme === false) {
                throw new Exception("Erro na query");
            }

            // foreach($retornoUsuarioFilme as $key => $valores ) {
            // $retornoUsuarioFilme[$key][2] = base64_decode($retornoUsuarioFilme[$key][2]);
            // //     $bin =base64_decode();
            // //     $size = getImageSizeFromString($bin);
            // //     $im = imageCreateFromString($bin);
            // //     $ext = substr($size['mime'], 6);
            // //     $img_file = "/arquivos/temp/" . $retornoUsuarioFilme[$key][0] . ".{$ext}";
            // //     $args = [$im, $img_file];
            // //     imagepng($im, $img_file, 0);
            // // if ($ext == 'png') {
            // //     $args[] = 0; // No compression for PNGs
            // // } 
            // // if ($ext == 'jpeg') {
            // //     $args[] = 100; // 100% quality for JPEGs
            // // }
            // // $fn = "image{$ext}";
            // // $teste = call_user_func_array($fn, $args);
               
            // }
            echo json_encode(['erro' => 0, 'mensagem' => utf8_encode('Filmes Encontrados'), 'dados' =>  $retornoUsuarioFilme]);
            break;
        case 'atualizarDados' :
            $filme = isset($_POST['filme']) ? str_replace('filme_','',trim($_POST['filme'])) : '';
            $status = isset($_POST['status']) ? $_POST['status'] : '';
            $parametros = array (
                'status' => $status,
                'codigo' => $filme
            );
            $retornoUsuarioFilme = $usuarioFilmeRepo->atualizarFilmeUsuario($parametros);
            if ($retornoUsuarioFilme === false) {
                throw new Exception("Erro ao atualizar os dados");
            }

            echo json_encode(['erro' => 0, 'mensagem' => utf8_encode('Atualizado com sucesso')]);
            break;

        case 'filme':
            $retornoDetalheFilme = $filmeRepo->pegardetalhesFilme($_POST['filme']);
            if ($retornoDetalheFilme === false) {
                throw new Exception("Erro na query");
            }
            $teste = json_encode(['erro' => 0, 'mensagem' => utf8_encode('Filmes Encontrados'), 'dados' =>   $retornoDetalheFilme]);
           echo json_encode(['erro' => 0, 'mensagem' => utf8_encode('Filmes Encontrados'), 'dados' =>   $retornoDetalheFilme]);
            break;

        default:
            throw new Exception("Não recebeu uma ação");
            break;
    }

}
catch (Exception $e) {
    echo json_encode(['erro' => 1, 'mensagem' => utf8_encode($e->getMessage())]);
}

?>