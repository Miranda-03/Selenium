
let estado = document.getElementById('status');

function logearse() {
    let nombre = document.getElementById("nombre").value;
    let contraseña = document.getElementById('contraseña').value;
    if (nombre === "ipm" && contraseña === "ipmpass") {
        estado.innerHTML = "logeado"
    }
    else {
        estado.innerHTML = "no"
    }
}