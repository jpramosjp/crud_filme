<?php
require_once('classe/xsql.php');

class FilmeRepo{
    protected $conexao;
    function __construct()
    {
       $this->conexao = new Xsql();     
    }


    /**
     * 
     */
    function pegardetalhesFilme ($filme) {
        try {
            $sql = "
            SELECT
            A.nome,
            data_lancamento,
            (SELECT x.descricao FROM tipo_filme x WHERE x.codigo = A.tipo_filme) AS tipo_filme,
            (SELECT x.nome FROM pessoas x WHERE x.codigo = A.ator_principal) AS ator_principal,
            A.detalhes
        FROM 
            filmes A
        WHERE 
            A.codigo = $filme";
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
}