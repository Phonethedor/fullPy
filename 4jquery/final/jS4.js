$(document).ready(function(){
    $('#myDiv').children().css('background-color','skyblue');
    /* $('h3 , p').click(function(){
        $(this).parent().append('<h2>Falta poco para la segunda prueba</h2>');
    });*/
    $('h3, p').click(function(){
        $(this).siblings().hide();
    });

    $('button').click(function(){
        $(this).siblings().children().children().text('David Mix');
    });
});