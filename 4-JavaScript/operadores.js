// Operadores de asignación
num= 0;
num+= 1; //num= num+1
num-= 1; //num= num-1
num*= 2;
num/= 2;

// Operadores aritméticos (repaso)
num1= 4
num2= 2
console.log(num1+num2);
console.log(num1-num2);
console.log(num1*num2);
console.log(num1/num2);
console.log(String(num1/num2));
console.log(num1**2); // exponente/potencia
console.log(num1%num2); // módulo/resto de la división entera 5/2= 2 (cociente) resto=1
console.clear()

// Operadores relacionales/comparación
var A= 5;
var B= 2;
console.log(A>=5); //True
console.log(A>5); //True
console.log(A<5); //False
console.log(A==5); //False
console.log(A!=5); //True
console.clear()

// Operadores lógicos
// &&(AND)  ||(OR)  !(NOT)
// &&(AND): sólo 1 falso, falso
console.log(true && true); //True
console.log(false && true); //False
console.log(false && true && true && true); //False
// ||(OR): sólo 1 verdadero, verdadero
console.log(false || false); //False
console.log(false || true || false || false); //True
// !(NOT)
console.log(!true); //False
console.log(!false); //True

// Todos combinados:
var A= 5;
var B= 2;
resultado= A>5+B && B<=100 || A+B==50;
//         A>7   && B<=100 || 7==50
//         False && True   || False
console.log(false && true  || false); //False
// console.log(false || false && true); //False
console.log("Resultado:", resultado);
// los paréntesis rompen la jerarquía entre operadores








