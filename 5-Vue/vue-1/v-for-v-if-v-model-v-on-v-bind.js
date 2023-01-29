const ejemplo2 = new Vue({
    el: '#ejemplo2',
    data: {
        titulo: 'Ejemplo 2',
        frutas: [
            { nombre: 'Pera', cantidad: 10 },
            { nombre: 'Manzana', cantidad: 0 },
            { nombre: 'Banana', cantidad: 11 }
        ],
        nuevaFruta: '',
        total: 0
    },
    methods: {
        agregarFruta() {
            this.frutas.push({ nombre: this.nuevaFruta, cantidad: 0 })
            this.nuevaFruta = ''
        },
        otroMetodo() {

        }
    },
    // Propiedad computada
    computed: {
        sumarFrutas() {
            this.total = 0;
            for (fruta of this.frutas) {
                this.total += fruta.cantidad;
            }
            return this.total;
        }
    }
})

ejemplo2.titulo = 'Título: v-for y v-if';
