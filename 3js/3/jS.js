function calcular() {
    let n1 = document.getElementById("nota1").value;
    let n2 = document.getElementById("nota2").value;
    let n3 = document.getElementById("nota3").value;
    let n4 = document.getElementById("nota4").value;
    let ex = document.getElementById("ex").value;
    let exr = false;
    let msg = 0;
    let error = 0;
    
    if(n1 >= 10 && n1 <= 70){
        msg = 10;
    }else{
        document.getElementById("error1").innerHTML=
        "<span style='color:red'>nota invalida, ingrese entre 10 a 70!!</span>";
        error++;
    }
    document.getElementById("result").innerHTML = msg;
}