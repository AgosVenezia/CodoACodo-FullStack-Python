var a= ["a", "b", "c", "d"];
//console.log(a);

// for-in

for (var prop in a){
    console.log(prop);
}

for (var i in a){
    console.log(a[i]);
}

// for-of

for (var valor of a){
    console.log(valor);
}