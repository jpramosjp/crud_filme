function pegarFilmeUsuario(){
    $colunas = $('#teste td');
    $colunas.each(function(){
        $(this).eq(0).children('div').eq(0).html('');
    }); 
    $.post('ajax_pegar_filmes_usuarios.php', {
        acao: "trazerDados"
    }, function(obj) {
        if (obj.erro == 1) {

            alert(obj.mensagem);

            alterna_protecao(false);

            return false

        }
        let html= "";

        $.each(obj.dados, function(i, filme){
            $colunas.each(function () {
                if(filme[3] == $(this).attr('id')) {
                    var imagem = new Image();
                    imagem.src = 'data:image/png;base64,' + filme[2];
                    imagem.width = 150;
                    imagem.height = 150;
                    imagem.draggable =false;
                    html = "<div style = 'border: 2px solid red; padding:5px;' ondrop='drop(event)' draggable='true' ondragstart='drag(event)' id = 'filme_"+filme[0] + "' onclick = 'abrirModal(" + filme[4] +")'></div>";
                    $(this).eq(0).children('div').eq(0).append(html);
                    document.getElementById("filme_"+filme[0]).appendChild(imagem);                    
                }
            });
        });

    },"json");

}
