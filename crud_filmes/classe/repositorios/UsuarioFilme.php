<?php
require_once('classe/xsql.php');

class UsuarioFilme{
    protected $conexao;
    function __construct()
    {
       $this->conexao = new Xsql();     
    }


    /**
     * 
     */
    function pegarUsuarioFilme ($usuario) 
    {
        try {
            $sql = "
            SELECT
                B.codigo,
                A.nome,
                A.imagem_b64, 
                C.codigo,
                A.codigo
            FROM 
                filmes A
            INNER JOIN
                usuarios_filmes B
            ON
                B.filme  = A.codigo 
            INNER JOIN 
                status C
            ON
                C.codigo = B.status
            WHERE
                B.usuario = $usuario";
            $retorno = $this->conexao->requisitar($sql);
            if ($retorno === false) {
                throw new Exception($this->conexao->mensagem);
            }
            return $retorno;
        }
        catch (Exception $e) {
            trigger_error($e->getMessage());
            return false;
        }
    }

    function atualizarFilmeUsuario ($condicao) {
        try {
            $sql = "UPDATE usuarios_filmes SET status = " . $condicao['status'] . " WHERE codigo = " . $condicao['codigo'];
            $retorno = $this->conexao->requisitar($sql);
            if ($retorno === false) {
                throw new Exception($this->conexao->mensagem);
            }
            return true;

        }
        catch (Exception $e) {
            trigger_error($e->getMessage());
            return false;
        }
    }
}   
?>