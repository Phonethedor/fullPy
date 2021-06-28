$(document).ready(function(){
    $('#slide').hide();

    $('#addClass').click(function(){
        $('#textor').addClass('red');
    });

    $('#slideToggle').click(function(){
        $('#slide').slideToggle();
    })

    $('#append').click(function(){
        $('#extra').append("<p>parrafo nuevo</p>");
    });
});