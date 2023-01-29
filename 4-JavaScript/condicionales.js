/* 
Estructuras de control:
1) Estructuras secuenciales
2) Estructuras condicionales/alternativas/de decisión
3) Estructuras iterativas/repetitivas (ciclos/bucle)
*/

// 2) Estructuras condicionales/alternativas/de decisión
// Condicional simple (if)
// Ejemplo: verificar si un número es positivo
num= parseInt(prompt("Ingrese un número entero"))
if (num>0) { 
    alert("El número es positivo.");
}
// Condicional doble (if-else)
// Ejemplo: verificar si un número es positivo o negativo
if (num>0) { 
    // Bloque de verdad
    alert("El número es positivo.");
} else { 
    // Bloque de falsedad
    alert("El número es negativo (o cero).");
}
// Condicionales anidados (if-else-if, if-if-else)
// Ejemplo: verificar si un número es positivo, negativo o cero
if (num>0) { 
    alert("El número es positivo.");
} else {
    if (num<0) { 
        alert("El número es negativo (o cero).");
    } else { 
        alert("El número es cero.");
    }
}
// else-if (elif:Python)
if (num>0) { 
    alert("El número es positivo.");
} else if (num<0) { 
    alert("El número es negativo (o cero).");
} else { 
    alert("El número es cero.");
}

console.clear();
// Operador ternario
var num= parseInt(prompt("Ingrese su número:"));
resultado= num>0 ? "Positivo" : "Negativo (o cero)";
console.log(resultado);



