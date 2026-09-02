const API_URL = "http://127.0.0.1:8000";

// Mostrar usuarios
async function cargarUsuarios() {
    const respuesta = await fetch(`${API_URL}/usuarios`);
    const usuarios = await respuesta.json();

    const lista = document.getElementById("lista-usuarios");
    lista.innerHTML = "";

    usuarios.forEach((u) => {
        const li = document.createElement("li");

        li.innerHTML = `
            ${u.nombre} — ${u.email}
            <button onclick="eliminarUsuario('${u._id}')">Eliminar</button>
        `;

        lista.appendChild(li);
    });
}

// Crear usuario
document.getElementById("form-usuario").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;

    await fetch(`${API_URL}/usuarios`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nombre, email })
    });

    document.getElementById("mensaje").textContent = "Usuario creado";

    e.target.reset();

    cargarUsuarios();
});

// Eliminar usuario
async function eliminarUsuario(id) {
    const respuesta = await fetch(`${API_URL}/usuarios/${id}`, {
        method: "DELETE"
    });

    if (respuesta.ok) {
        document.getElementById("mensaje").textContent =
            "Usuario eliminado correctamente";

        cargarUsuarios();
    }
}

// Iniciar
cargarUsuarios();