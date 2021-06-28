//Definiendo un arreglo de los errores
var arreglo = new Array();
arreglo[0] = "errorNombre";
arreglo[1] = "errorApellido";
arreglo[2] = "errorEmail";
arreglo[3] = "errorUsuario";
arreglo[4] = "errorPassword";
arreglo[5] = "errorConfirmacion";

function validar() {
    // Definiendo el arreglo de la captura de valores del formulario
    var entrada = new Array();
    entrada[0] = document.getElementById('nombre').value;
    entrada[1] = document.getElementById('apellido').value;
    entrada[2] = document.getElementById('email').value;
    entrada[3] = document.getElementById('user').value;
    entrada[4] = document.getElementById('password').value;
    entrada[5] = document.getElementById('confirmarpassword').value;

    //Definiendo los mensajes de error 
    var error = new Array();
    error[0] = "<span style='color:red'>Ingrese el nombre!!</span>";
    error[1] = "<span style='color:red'>Ingrese el apellido!!</span>";
    error[2] = "<span style='color:red'>Ingrese el email!!</span>";
    error[3] = "<span style='color:red'>Ingrese el nombre de usuario!!</span>";
    error[4] = "<span style='color:red'>Ingrese el password!!</span>";
    error[5] = "<span style='color:red'>Ingrese el confirmación del password!!</span>";

    //Definiendo un ciclo foreach Javascript para la validación
    for (i in entrada) {
        var mensajeError = error[i];
        var valorArreglo = arreglo[i];

        if (entrada[i] == "") {
            document.getElementById(valorArreglo).innerHTML = mensajeError;
        }

        //Validando el email
        else if (i == 2) {
            var arroba = entrada[i].indexOf("@");
            var punto = entrada[i].lastIndexOf(".");
            //Condiciones de invalidez del correo
            if (arroba < 1 || punto < arroba + 2 || entrada[2].length < punto + 2) {
                document.getElementById('errorEmail').innerHTML =
                    "<span style='color:red'>Ingrese un email válido</span>";
            }
            else {
                document.getElementById('errorEmail').innerHTML =
                    "Campo válido";
            }
        }

        else if (i == 5) {
            var primero = document.getElementById('password').value;
            var segundo = document.getElementById('confirmarpassword').value;
            if (primero != segundo) {
                document.getElementById('errorConfirmacion').innerHTML =
                    "<span style='color:red'>Los password no coinciden</span>";
            }
            else {
                document.getElementById('errorConfirmacion').innerHTML =
                    "Campo válido";
            }
        }
        else {
            document.getElementById(valorArreglo).innerHTML =
                "Campo válido";
        }
    }

}

function validarTodos() {
    var contador = 0;
    for (i = 0; i < 6; i++) {
        var valorArreglo = arreglo[i];
        if (document.getElementById(valorArreglo).innerHTML == "Campo válido") {
            contador++;
        }
    }
    if (contador == 6) {
        document.getElementById("mensajefinal").innerHTML = "Formulario validado!!";
    }
}