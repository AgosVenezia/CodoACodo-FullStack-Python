// while: mientras
// Ejemplo: Ciclo exacto. Contador de 1 a 10.
var cont= 1; //1) Iniciar la var contadora
while (cont<=10) {  //2) Condición
    console.log(cont); //3) Orden de las instrucciones dentro del ciclo
    cont++; //cont= cont+1 4) La instrucción que modifica el valor de mi condición
}

// Ciclo condicional
// Ejemplo: sumatoria de valores hasta ingresar el cero.
console.clear()
var suma= 0;
var num= parseInt(prompt("Ingrese un número:"));
while (num!=0) { 
    suma+=num; //suma= suma+num
    num= parseInt(prompt("Ingrese un número:"));
}
console.log("Sumatoria:", suma);

// do-while (hacer-mientras) do-while se ejecuta al menos una vez
// Idem ejemplo anterior
console.clear()
var suma= 0;
do {
    num= parseInt(prompt("Ingrese un número:"));
    suma+=num; //suma= suma+num
} while (num!=0); 
console.log("Sumatoria:", suma);

// for: Ciclo exacto
// Ejemplo: Ciclo exacto. Contador de 1 a 10.
for (let cont = 0; cont <= 10; cont++) {
    //Instrucciones
    console.log(cont); //3) Orden de las instrucciones dentro del ciclo
}
