Vue.component('contador', {
    template: //html 
        `
        <div>
            <h3>{{num}}</h3>
            <button @click="num++">+</button>
        </div>
        `,
    // Ahora data en forma de función y puede retornar más de un dato
    data() {
        return {
            num: 0
        }
    }
})