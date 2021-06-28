var img = "";
            for (let x = 0; x < 8; x++){
                img += '<img src="ninja.jpg">';
            };
            $(document).ready(function(){
                $('.container').append(img)
                $('.container').append("<br><button id='devolver'>Devolver</button>")
                $('img').click(function(){
                    $(this).hide("slow");
                });
                $('#devolver').click(function(){
                    $('img').show("slow");
                });
            });