// 2 formas de crear un String

// Literal
const TEXTO_1= "Hola Mundo! ";

// Objeto
//const TEXTO_2= new String("Hola a todos!");
var texto2= new String("Hola a todos!");

// Acceder a una posición determinada
console.log(TEXTO_1[1]); // o

// Intento modificar una parte del String
texto2[1]= "X";
console.log(texto2); // no funciona

// Sí puedo hacer esto:
texto2= "Hxla a todos!";
console.log(texto2);

// Propiedades
console.log(TEXTO_1.length); // 12

// Métodos (comportamiento)
// Fuente: https://www.w3schools.com/js/js_string_methods.asp
console.log(TEXTO_1.charAt(1)); // o
console.log(texto2.length); // 13
console.log(texto2.charAt(1)); // X
console.log(texto2.indexOf("la")); // 2
console.log(texto2.indexOf("la", 3)); // -1
console.log(texto2.toLowerCase()); // hxla a todos!
console.log(texto2.substring(2,4)); // la
console.log(texto2.substring(2)); // la a todos!
console.log(texto2.substr(2, 2)); // la
console.log(texto2); // hxla a todos!
//console.log(texto2.replace("la", "LA")); // HxLA a todos!
nuevaCadena= texto2.replace("la", "LA");
console.log(nuevaCadena); // HxLA a todos!


