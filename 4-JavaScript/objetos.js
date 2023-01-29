var persona = {
    nombre: "Juan",
    apellido: "Paz",
    dni: 12345678, //el último no lleva coma
    // Métodos
    nombreCompleto: function(){
        return this.nombre + " " + this.apellido;
    }
};
    
console.log(persona);
console.log(persona.nombre);
console.log(persona.nombreCompleto());

// for-in

for (var prop in persona){
    console.log(prop);
}

for (var prop in persona){
    console.log(prop + ": " + persona[prop]);
}
