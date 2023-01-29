// Crear un fx (sin retorno de datos)
function saludar(){
    console.log("Hola!");
}

function saludarNombre(nombre){ //una fx con 1 parámetro
    console.log("Hola " + String(nombre) + "!");
}

// Crear un fx (con retorno de datos)
function sumar(num1, num2){
    let suma= num1 + num2;
    return suma; //Retornando un valor
}

function sumar2(num1, num2){
    return num1 + num2; //Retornando un valor
}

// Función flecha
var aSumar= (num1,num2)=>num1+num2;

// Buenas prácticas
function maximo(num1, num2){
    /*
    pre: recibe dos valores
    pos: devuelve el valor máximo entre dos valores
    */
   if (num1>num2){
       valorMax= num1;
   } else {
       valorMax= num2
   }
   return valorMax;
   //console.log("----------");
}

function esPar(num){ //mal hecho: return corta ciclos
    if (num%2==0){
        return true;
    } else {
        return false;
    }
}

function esPar2(num){
    if (num%2==0){
        rta= true;
    } else {
        rta= false;
    }
    return rta;
}

function esPar3(num){
    let rta= (num%2==0)?true:false;
    return rta;
}

var esPar4= num=>(num%2==0);

// Prog ppal
// Llamar a fx
console.log("Funciones:");
saludar();
saludar();
var nom= "Agostina";
//var nombre= "Agostina";
// saludarNombre("Agostina");
saludarNombre(nom);
//saludarNombre(nombre); //llamar a 1 fx y le paso 1 argumento

var s= sumar(12, 25);
console.log("Suma:", sumar(12, 25));
console.log("Suma:", s);

//Función flecha
console.log("Suma:", aSumar(12,25));

//Buenas prácticas
console.log(maximo(12,23));
console.log(maximo(130,130));

console.log(esPar(10));
console.log(esPar2(10));
console.log(esPar3(11));
console.log(esPar4(11));

