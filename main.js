// Dirección de nuestra API
const API_URL = "http://127.0.0.1:8000";


// Cargar usuarios desde la API
async function cargarUsuarios() {

    const contenedor = document.querySelector("#lista-usuarios");

    contenedor.innerHTML = "<li>Cargando...</li>";

    try {

        // GET: pide los usuarios a la API
        const respuesta = await fetch(`${API_URL}/usuarios`);

        if (!respuesta.ok) {
            throw new Error(`Error ${respuesta.status}`);
        }

        // Convertimos la respuesta a JSON
        const usuarios = await respuesta.json();

        renderizarUsuarios(usuarios);

    } catch (error) {

        contenedor.innerHTML =
            "<li>No se pudo conectar con el servidor.</li>";

        console.error(error);
    }
}


// Mostrar usuarios en la página
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

        // Validamos que no estén vacíos
        if (nombre == "" || email == "") {

            document.querySelector("#mensaje").textContent =
                "Completá todos los campos";

            return;
        }

        // Datos del nuevo usuario
        const nuevoUsuario = {
            nombre: nombre,
            email: email
        };

        // POST: enviamos el usuario a la API
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

    // DELETE: elimina un usuario de la API
    await fetch(`${API_URL}/usuarios/${indice}`, {
        method: "DELETE"
    });

    document.querySelector("#mensaje").textContent =
        "Usuario eliminado correctamente";

    cargarUsuarios();
}


// Carga los usuarios cuando abrimos la página
cargarUsuarios();