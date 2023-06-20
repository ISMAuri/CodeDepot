//Obtencion y modificacion de childs

const contenedor = document.querySelector('.contenedor');

// const primerHijo = contenedor.firstChild;
//const ultimoHijo = contenedor.lastChild;

const primerHijo = contenedor.firstElementChild;
const ultimoHijo = contenedor.lastElementChild;

// const hijos = contenedor.childNodes;

const hijosElementos = contenedor.children;

console.log(hijosElementos);


// hijos.forEach(hijo => console.log(hijo));
for (hijo of hijosElementos) {
    console.log(hijo)
}