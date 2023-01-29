document.addEventListener("DOMContentLoaded", function () {
document.getElementById("formulario").addEventListener('submit', validarFormulario);
});
    function validarFormulario(evento) {
        evento.preventDefault();
        var nombre = document.getElementById('nombre').value;
        if (nombre.length == 0) {
            alert('No has escrito nada en el nombre');
            return;
        }
        var mail = document.getElementById('mail').value;
        if (mail.length == 0) {
            alert('El email ingresado no es válido');
            return;
        }
        var mensaje = document.getElementById('mensaje').value;
        if (mensaje.length == 0) {
            alert('No has escrito ningún mensaje');
            return;
        }
        this.submit();
    }
   