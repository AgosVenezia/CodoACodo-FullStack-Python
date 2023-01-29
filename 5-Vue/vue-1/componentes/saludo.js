// Componente
Vue.component('saludo', {
    template: //html 
        `
        <div>
            <h1>{{msj}}</h1>
            <h2>{{msj2}}</h2>
        </div>
        `,
    data() {
        return {
            msj: 'Hola dinámico (componentes)',
            msj2: "Título H2"
        }
    }
})