const API_URL = "http://127.0.0.1:8000";


// Mostrar usuarios
async function cargarUsuarios() {

    const respuesta = await fetch(API_URL + "/usuarios");

    const usuarios = await respuesta.json();

    const lista = document.querySelector("#lista-usuarios");

    lista.innerHTML = "";

    usuarios.forEach(function(usuario) {

        lista.innerHTML += `
            <li>
                ${usuario.nombre} - ${usuario.email}
            </li>
        `;

    });
}


// Crear usuario
document.querySelector("#form-usuario").addEventListener("submit", async function(evento) {

    evento.preventDefault();

    const nombre = document.querySelector("#nombre").value;
    const email = document.querySelector("#email").value;

    await fetch(API_URL + "/usuarios", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            nombre: nombre,
            email: email
        })

    });

    alert("Usuario agregado");

    document.querySelector("#form-usuario").reset();

    cargarUsuarios();

});


// Cargar usuarios al abrir
cargarUsuarios();