

function Mudarestado(el, el2) {
    var display = document.getElementById(el).style.display;
    if(display == "none")
        document.getElementById(el).style.display = 'block';
    else {
        document.getElementById(el).style.display = 'none';
        document.getElementById(el2).style.display = 'block';
    }
}