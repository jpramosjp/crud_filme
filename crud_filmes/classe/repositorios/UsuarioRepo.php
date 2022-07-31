<?php
require_once('classe/xsql.php');

class UsuarioRepo{
    protected $conexao;
    function __construct()
    {
       $this->conexao = new Xsql();     
    }


    /**
     * 
     */
    function pegarUsuario ($condicao) 
    {
        try {
            $sql = "
                    SELECT 
                        codigo 
                    FROM 
                        usuarios 
                    WHERE 
                        nome_acesso = '".$condicao['nome_acesso']."' 
                        AND senha = '". $condicao['senha'] ."'";
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

    function cadastrarUsuario ($parametros) 
    {
        try {
            $sql = "INSERT INTO usuarios (nome_acesso,nome,senha) VALUES
                    ('" . $parametros['nome_acesso'] . "', '" . $parametros['nome'] . "', '" . $parametros['senha'] . "');";
            $retorno = $this->conexao->requisitar($sql);
            if($retorno === false) {
                throw new Exception ($this->conexao->mensagem);
            }
        }
        catch (Exception $e) {
            trigger_error($e->getMessage());
            return false;
        }
    }
}   
?>