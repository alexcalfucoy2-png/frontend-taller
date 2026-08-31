const API_URL = "http://127.0.0.1:8000";


// Cargar usuarios
async function cargarUsuarios() {

    const contenedor = document.querySelector("#lista-usuarios");

    contenedor.innerHTML = "<li>Cargando...</li>";

    try {

        const respuesta = await fetch(`${API_URL}/usuarios`);

        if (!respuesta.ok) {
            throw new Error(`Error ${respuesta.status}`);
        }

        const usuarios = await respuesta.json();

        renderizarUsuarios(usuarios);

    } catch (error) {

        contenedor.innerHTML =
            "<li>No se pudo conectar con el servidor.</li>";

        console.error(error);
    }
}


// Mostrar usuarios
function renderizarUsuarios(usuarios) {

    const contenedor = document.querySelector("#lista-usuarios");

    contenedor.innerHTML = usuarios
        .map((u, indice) =>
            `<li>
                ${u.nombre} — ${u.email}
                <button onclick="eliminarUsuario(${indice})">
                    Eliminar
                </button>
            </li>`
        )
        .join("");
}


// Crear usuario
document
    .querySelector("#form-usuario")
    .addEventListener("submit", async (evento) => {

        evento.preventDefault();

        const nombre = document.querySelector("#nombre").value;
        const email = document.querySelector("#email").value;

        // Validar campos
        if (nombre == "" || email == "") {

            document.querySelector("#mensaje").textContent =
                "Completá todos los campos";

            return;
        }

        const nuevoUsuario = {
            nombre: nombre,
            email: email
        };

        await fetch(`${API_URL}/usuarios`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(nuevoUsuario)
        });

        document.querySelector("#mensaje").textContent =
            "Usuario creado correctamente";

        evento.target.reset();

        cargarUsuarios();
    });


// Eliminar usuario
async function eliminarUsuario(indice) {

    await fetch(`${API_URL}/usuarios/${indice}`, {
        method: "DELETE"
    });

    document.querySelector("#mensaje").textContent =
        "Usuario eliminado correctamente";

    cargarUsuarios();
}


// Cargar usuarios al iniciar
cargarUsuarios();