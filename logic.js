function formularioEnter() {

    let datos = document.getElementById("datos-cargados")

    let primero = document.getElementById("in-1").value
    let segundo = document.getElementById("in-2").value
    let tercero = document.getElementById("in-3").value
    let cuarto  = document.getElementById("in-4").value
    
    primero === document.getElementById("in-1").value && 
    segundo === document.getElementById("in-2").value &&
    tercero === document.getElementById("in-3").value &&
    cuarto  === document.getElementById("in-4").value ? 
    datos.innerHTML = "datos cargados" : 
    datos.innerHTML = "datos no cargados"
       
}

function loginCargar(){

    let datos = document.getElementById("logDatos")

    let nombre = document.getElementById("input-nombre").value
    let contraseña = document.getElementById("input-pass").value

    nombre === "alumno" &&
    contraseña == "123" ?
    datos.innerHTML = "logeado" :
    datos.innerHTML = "datos incorrectos"

}

function Buscador(){
    
    let malBuscado = document.getElementById("malBuscado");
    let buscar = document.getElementById("inputBuscador").value

    buscar === "log in" ? window.location.href = "login.html" :
    buscar === "formulario" ? window.location.href = "formulario.html" :
    buscar === "home" ? window.location.href = "index.html" :
    malBuscado.innerHTML = "la busqueda no se encuentra";

}