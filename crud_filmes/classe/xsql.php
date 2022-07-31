<?php

class Xsql {
    protected $conexao;
    public $mensagem;
	public $sql;
    
    public function conectar()
		{	$this->sql='';

      	 /**   DEVELOP **/
        //$this->conexao=pg_connect('host=172.25.5.3 port=5432 dbname=hcosta user=postgres password=GX5+W68$Pt&W');
        /**   OFICIAL * */
    	//    $this->conexao = pg_connect('host=172.25.5.12 port=5432 dbname=hcosta user=silva_marcus password=lczy#p[@');
        $this->conexao = mysqli_connect("localhost", "root", "","crud_filmes");
			if($this->conexao===false)
			{	$this->mensagem=__METHOD__.': N�o foi poss�vel conectar-se';
				return false;
			}
			return true;
		}

        public function requisitar($sql,$considerar_limit=true)
		{ global $nome_modulo;
			if(strpos($nome_modulo, 'relatorio'))
			{	file_put_contents("relatorios.log",$sql,FILE_APPEND);	}
			$this->sql='';
			$sql=trim($sql);
			$this->encontrados=0;
			if($sql=='')
			{	$this->mensagem=__METHOD__.': Requisi��o n�o definida';
				return false;
			}

			$retorno=$this->conexao->query($sql);
			if($retorno===false)
			{
				$this->mensagem=__METHOD__.': N�o foi poss�vel executar a requisi��o';
        trigger_error("$sql");
				$this->sql=$sql;
				return false;
			}

			if (preg_match('/\bINSERT\b/', $sql) || preg_match('/\bUPDATE\b/', $sql) ) {
				return true;
			}
			return $retorno->fetch_all();
		}

        public function __construct($auto_conectar=true)
		{	
			//$this->conexao=false;
			$this->mensagem='';
			$this->sql='';
			if($auto_conectar)
			{	
                $this->conectar();
				$this->conexao->set_charset("utf8");
            }
		}
}

?>