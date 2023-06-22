
const contenedor = document.querySelector('.contenedor');

const parrafo = document.createElement('P');
parrafo.innerHTML = 'Parrafo';
const h2Nuevo = document.createElement('H2');
h2Nuevo.innerHTML = 'Titulo';


h2Antiguo = document.querySelector('.h2')



contenedor.replaceChild(h2Nuevo, h2Antiguo)

contenedor.removeChild(document.querySelector('.h3'))

console.log(contenedor.hasChildNodes())

//Nota: el texto tambien cuenta como child