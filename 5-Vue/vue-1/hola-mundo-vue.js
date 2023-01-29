var app = new Vue({
    el: '#app',
    data: {
        mensaje: "Hola Mundo!",
        num: 12
    }
})

const app2 = new Vue({
    el: '#app2',
    data: {
        titulo: "Presione clic para dirigirse a la web..."
    }
})

//app.mensaje = "Nuevo valor";
app2.titulo= "Nuevo titulo";
