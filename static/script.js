document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.getElementById('title');
    const yearInput = document.getElementById('year');
    const authorInput = document.getElementById('author');
    const guardarBtn = document.getElementById('guardar-btn');

    // Declarar las variables para los mensajes de error fuera de la función validarCampos
    const titleError = document.getElementById('title-error');
    const yearError = document.getElementById('year-error');
    const authorError = document.getElementById('author-error');

    // Función para validar los campos
    function validarCampos() {
        const title = titleInput.value.trim();
        const year = yearInput.value.trim();
        const author = authorInput.value.trim();

        // Validar campos vacíos y mostrar mensajes de error específicos
        titleError.textContent = title === "" ? "Por favor, ingrese un título." : "";
        yearError.textContent = year === "" ? "Por favor, ingrese un año." : "";
        authorError.textContent = author === "" ? "Por favor, ingrese un autor." : "";

        // Validar el formato del año y el rango
        const yearPattern = /^\d{4}$/;
        if (!yearPattern.test(year)) {
            yearError.textContent = "El año debe ser un número válido de 4 dígitos.";
        } else {
            yearError.textContent = ""; // Limpiar el mensaje de error
        }

        // Habilitar o deshabilitar el botón "Guardar"
        guardarBtn.disabled = !title || !year || !author || !yearPattern.test(year);
    }

    // Restablecer los campos y deshabilitar el botón después de enviar el formulario
    document.getElementById('mi-formulario').addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar el envío real del formulario

        // Restablecer los campos
        titleInput.value = "";
        yearInput.value = "";
        authorInput.value = "";
        titleError.textContent = "";
        yearError.textContent = "";
        authorError.textContent = "";
        guardarBtn.disabled = true; // Deshabilitar el botón después de enviar
    });

    // Escuchar cambios en los campos
    titleInput.addEventListener('input', validarCampos);
    yearInput.addEventListener('input', validarCampos);
    authorInput.addEventListener('input', validarCampos);
});

// Evento que se ejecuta cuando se envía el formulario
document.getElementById("mi-formulario").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto

    // Obtener los valores del formulario
     const title = document.getElementById("title").value;
     const year = document.getElementById("year").value;
     const author = document.getElementById("author").value;

    // Agregar el libro a la tabla
    agregarLibroATabla(title, year, author);

    // Restablecer el formulario
    this.reset();
});


/* script para el modal */
$(document).ready(function(){
    // Cuando se hace clic en el botón de edición
    $(".btn-edit").click(function(){
        // Obtener los datos del libro de la fila de la tabla
        const titulo = $(this).closest("tr").find("td:eq(1)").text();
        const año = $(this).closest("tr").find("td:eq(2)").text();
        const descargas = $(this).closest("tr").find("td:eq(3)").text();

        // Llenar el formulario de edición con los datos del libro
        $("#editTitle").val(titulo);
        $("#editYear").val(año);
        $("#editScore").val(descargas);

        // Mostrar el modal de edición
        $("#editModal").modal("show");
    });
});


 // Función para agregar una nueva fila a la tabla con los datos del libro
 function agregarLibroATabla(title, year, author) {
    const table = document.getElementById("libros-table").getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    // Insertar celdas con los datos del libro
    let cellIndex = newRow.insertCell(0);
    let cellTitle = newRow.insertCell(1);
    let cellYear = newRow.insertCell(2);
    let cellAuthor = newRow.insertCell(3);
    let cellEdit = newRow.insertCell(4);
    let cellDelete = newRow.insertCell(5);

    // Llenar las celdas con los datos del libro
    cellIndex.innerHTML = table.rows.length - 1; // Número de fila
    cellTitle.innerHTML = title;
    cellYear.innerHTML = year;
    cellAuthor.innerHTML = author;
    cellEdit.innerHTML = '<button class="btn btn-primary btn-sm btn-edit">Edit</button>';
    cellDelete.innerHTML = '<form><button type="submit" class="btn btn-danger btn-sm btn-delete">Delete</button></form>';

      // Agregar evento de clic al botón de eliminar
      cellDelete.querySelector('.btn-delete').addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario por defecto
        // Obtener la fila a la que pertenece el botón
        const row = this.closest('tr');
        // Eliminar la fila de la tabla
        row.parentNode.removeChild(row);
    });

}

