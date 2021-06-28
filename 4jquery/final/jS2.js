function mostrarMensaje(){
    $('.alert').click(function(){
        alert("Me han clickeado");
    });
};

$(document).ready(function(){
    mostrarMensaje();
    $('.nuevo_btn').click(function(){
        $('#buttons').append("<button class='alert'>Soy un boton generado dinamicamente</button><br>");
        mostrarMensaje();
    });
    
});