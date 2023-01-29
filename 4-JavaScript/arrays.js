// Crear un array
// Fuente: https://www.w3schools.com/js/js_array_methods.asp
var vector= [0,1,5,-1,100]; //Array de números
const ARR_1= ["Agostina",1,true,-1,100,23.4]; //Array de distintos tipos
var arr2= new Array(1,3,5,8);

// Propiedad "largo"
var largo= arr2.length; //propiedad: sin paréntesis, método con paréntesis

// Acceder a una posición determinada y modificar en caso de ser necesario
valor= arr2[2]; // 5
console.log(valor);
arr2[2]= 10000; // de 5 a 10000

// Recorrer un array
/*
for (let i = 0;i < arr2.length;i++) {
    const element = array[i];
}
*/

// Recorrer un Array/String para mostrarlo
console.log("Recorrer un array para mostrarlo: ");
for (let i = 0;i < arr2.length;i++) {
    //arr2[i];
    console.log(arr2[i]);
}

// Mostrar el objeto
console.log(arr2); //toString: f toString()
console.log(ARR_1);

// Métodos
console.clear();
for (let i = 0;i < arr2.length;i++) {
    //arr2[i];
    console.log(arr2[i]);
}

arr2.pop(); //Elimina el último elemento 8
arr2.push(100); //Agrega al final 100
arr2.sort(); //Ordena el array
arr2.reverse(); //Invierte el array

for (let i = 0;i < arr2.length;i++) {
    //arr2[i];
    console.log(arr2[i]);
}

// Ordenar arrays numéricos (ASC)
// Fuente: https://www.w3schools.com/js/js_array_sort.asp
var numeros= [40, 100, 1, 5, 20, 10];
function ordAsc(a,b) {return a-b;}
numeros.sort(ordAsc);
console.log(numeros);
// Ordenar arrays numéricos (DESC)
numeros.sort(function (a,b) {return b-a;}); //Parámetro es una fx anónima
console.log(numeros);

// filter()
console.log("Ejemplo filter");
var edades= [40,18,16,17,81,50];

function mayorDeEdad(edad){
    return edad>=18;
}

var aMayorEdad= edad=>edad>=18; //Fx flecha

console.log(edades.filter(mayorDeEdad));
console.log(edades.filter(aMayorEdad)); //Función flecha
console.log(edades.filter(edad=>edad>=18)); //Función anónima


