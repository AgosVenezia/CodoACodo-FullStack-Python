// Declaración de var
num1= 10;
num2= 12;
var num3= 99; //Numérica
var texto= "Agostina"; //String
var nombreApellido= "Agostina Venezia";
var nombre_apellido= "Agostina Venezia";

// Operadores aritméticos
console.log(num1+num2);
console.log(num1-num2);
console.log(num1*num2);
console.log(num1/num2);
console.log(String(num1/num2));
console.log(num1%num2); //módulo resto de la división entera 5/2= 2 (cociente) resto=1

// Operador incremental
i= 0;
console.log(i);
i++; // i= i+1
console.log(i);
i++; // i= i+1
console.log(i);
i++; // i= i+1
console.log(i);
i++; // i= i+1
console.log(i);
i--; // i= i-1

// Constantes
const VALOR_PI= 3.14159;
//radio= parseInt(prompt("Ingrese el radio: "));
//sup= radio*VALOR_PI**2; //Exponente
raiz= num1**(1/2); //Raiz cuadrada

// Booleanos (True/False)
var es_par= true; //false
console.log(es_par); 

// Limpiar la consola
//console.clear();

// Tipado dinámico
// var num1 texto es_par
console.log(typeof num1);
console.log(typeof texto);
console.log(typeof es_par);

num1= "100";
console.log(typeof num1); 

// Conversión a String, Int, Float
texto= "100.1";
textoInt= "20"; 
textoStr= "Agostina";
numInt= parseInt(textoInt);
console.log(numInt);
numFloat= parseFloat(textoInt);
console.log(numFloat);
txtFloat= String(numFloat);
console.log(txtFloat);

txtFloat= "$" + String(numFloat);
console.log(txtFloat);