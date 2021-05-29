$(document).ready(function(){
    for (let x = 1; x<=151; x++){
        $('#pokemon').append("<a href='#'><img id="+x+" src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+x+".png'></a>");
    }
    $('img').click(function(){
        $('#datos').empty();
        let x = $(this).attr('id');
        $.get('https://pokeapi.co/api/v2/pokemon/'+x+'/',function(res){
            $('#datos').append('<h2>'+res.name+'</h2>');
            $('#datos').append("<img id="+x+" src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+x+".png'><br>");
            $('#datos').append('<h2>Tipos</h2>');
            $('#datos').append('<ul>');
            for (let i = 0; i<res.types.length;i++){
                $('#datos').append('<li>'+res.types[i].type.name+'</li>');
            }
            $('#datos').append('</ul>')
            $('#datos').append('<h2>Altura</h2>')
            $('#datos').append('<p>'+res.height+'</p>');
            $('#datos').append('<h2>Peso</h2>');
            $('#datos').append('<p>'+res.weight+'</p>');
        }, 'json');
    });
});