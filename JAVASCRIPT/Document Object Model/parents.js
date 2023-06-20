
const contenedor = document.querySelector('.contenedor');

const h2Nuevo = document.createElement('H2');
h2Nuevo.innerHTML = 'Titulo';

h2Antiguo = document.querySelector('.h2')

console.log(contenedor.parentElement)


console.log(contenedor.parentNode)

//parentElement devuelve el elemento padre directo. Mientras tanto, parentNode devuelve el nodo padre.