function sumar(){
    //Definiendo las variables para guardar los números
    var num1=0, num2=0, suma=0;
    // Capturando los valores ingresados
    num1 = document.getElementById("n1").value;
    num2 = document.getElementById("n2").value;
    //Sumando los valores
    suma = parseFloat(num1) + parseFloat(num2);
    // Incando el lugar para imprimir la respuesta a la suma
    document.getElementById("respuesta").innerHTML=suma;
}