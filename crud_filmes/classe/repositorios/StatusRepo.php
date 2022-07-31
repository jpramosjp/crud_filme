<?php
require_once ('classe/xsql.php');

class StatusRepo{
    protected $conexao;
    function __construct()
    {
       $this->conexao = new Xsql();     
    }


    /**
     * 
     */
    function pegarStatus() 
    {
        try {
            $sql = "
            SELECT
                codigo,
                descricao as status
            FROM
                status";
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
?>