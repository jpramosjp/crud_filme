var nomeFilme = document.getElementById('nome_filme');
var detalheFilme = document.getElementById('detalhes_filme');
var dataLancamentoFilme = document.getElementById('data_lancamento_filme');
var tipoFilme = document.getElementById('tipo_filme');


const socket = new WebSocket('ws://localhost:9990/chat');


function table() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        document.getElementById("filmes_usuarios").innerHTML = this.responseText;
    }
    xhttp.open("GET","request.php");
    xhttp.send();
}

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

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.append(document.getElementById(data));
    console.log('teste: '+ev.target);
    console.log('teste: '+data);
    atualizarDados(data, ev.target.id);
    setTimeout(function(){
        socket.send(JSON.stringify('atualizou'));
    }, 300);
    
}

function atualizarDados(id,status) {
    $.post('ajax_pegar_filmes_usuarios.php', {
        acao: "atualizarDados",
        filme: id,
        status: status
    }, function(obj) {
        if (obj.erro == 1) {

            alert(obj.mensagem);

            alterna_protecao(false);

            return false
        }
    },"json");
}
 
function abrirModal (id) {
    $.post('ajax_pegar_filmes_usuarios.php', {
        acao: "filme",
        filme: id
    }, function(obj) {
        if (obj.erro == 1) {

            alert(obj.mensagem);

            return false
        }
      

        $.each(obj.dados, function(i, filme){
            nomeFilme.textContent = filme[0];
            detalheFilme.textContent = filme[4];
            tipoFilme.textContent = filme[2];
            dataLancamentoFilme.textContent = filme[1];
        });


    },"json");

    document.getElementById("myModal").style.display = 'block';
    

}

// When the user clicks on <span> (x), close the modal
function fecharModal() {
    nomeFilme.textContent = '';
    detalheFilme.textContent = '';
    tipoFilme.textContent = '';
    dataLancamentoFilme.textContent = '';
    document.getElementById("myModal").style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == document.getElementById("myModal")) {
    nomeFilme.textContent = '';
    detalheFilme.textContent = '';
    tipoFilme.textContent = '';
    dataLancamentoFilme.textContent = '';
    document.getElementById("myModal").style.display = "none";
  }
}



// Ao receber mensagens do servidor
socket.addEventListener('message', function (event) {
    // Deserializamos o objeto
    const data = JSON.parse(event.data);
    console.log(data);
    if(data == 'atualizou') {
        table();
    }
});

