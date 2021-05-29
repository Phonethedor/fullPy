$(document).ready(function(){
    for (let x = 1; x<=151; x++){
        $('#pokemon').append("<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+x+".png'>")
    }
});