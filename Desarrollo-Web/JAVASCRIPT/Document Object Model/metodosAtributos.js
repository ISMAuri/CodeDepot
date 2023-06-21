// Metodos para definir obtener y eliminar valores de atributos.

const rango = document.querySelector('.rango');

rango.setAttribute('type','range')

//Atributo = rango.getAttribute('type') 
// range

Atributo = rango.removeAttribute('type')

document.write(`<br> ${Atributo}`)
