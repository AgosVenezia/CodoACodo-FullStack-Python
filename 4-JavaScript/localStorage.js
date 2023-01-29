if (typeof(Storage)!== "undefined"){
    localStorage.setItem("nombre", "Juan"); //si no existe, lo crea
    localStorage.setItem("apellido", "Paz");
    localStorage.setItem("nombre", "Agostina"); //si existe, lo sobreescribe
    console.log(localStorage.getItem("nombre"));
} else {
    console.log("SU NAVEGADOR NO ES COMPATIBLE CON WEB STORAGE!");
}