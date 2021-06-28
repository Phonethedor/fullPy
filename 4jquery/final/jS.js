$(document).ready(function(){
    $('.alert').click(function(){
        alert("Me han clickeado");
    });

    $('.nuevo_btn').click(function(){
        $('#buttons').append("<button class='alert'>Soy un boton generado dinamicamente</button><br>");
    });

    $(document).on('click','.alert', function(){
        alert("me han clickeado");
    });

    
});