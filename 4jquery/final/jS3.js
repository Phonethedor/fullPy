$(document).ready(function(){
    $('button').click(function(){
        $('div').append('<h3>Tag generado dinamicamente</h3>');
    });
    $('h3').click(function(){
        alert("mensaje de h3");
    });
});