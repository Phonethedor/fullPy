var id = '8b36fff08402c0723a662d43549b02df';
$(document).ready(function(){
    $('button').click(function(){
        $('.datos').empty();
        let ciudad = $('#city').val();
        if (ciudad == ''){
            alert("ingrese ciudad");
        }else{
            $.get('http://api.openweathermap.org/data/2.5/weather?q='+ciudad+'&appid='+id,function(data){
                $('.datos').append('<span>'+data.name+': </span>');
                $('.datos').append('<span>'+data.weather[0].description+'</span><br><br>');
                $('.datos').append('<span>Temperatura en Farenheit: </span>');
                $('.datos').append('<span>'+data.main.temp+'</span><br><br>');
                $('.datos').append('<span>Coordenadas: </span>');
                $('.datos').append('<span>Longitud '+data.coord.lon+',</span>');
                $('.datos').append('<span>latitud '+data.coord.lat+',</span>');
            }, 'json');
        }
    });
});//http://api.openweathermap.org/data/2.5/weather?q=California&appid=8b36fff08402c0723a662d43549b02df