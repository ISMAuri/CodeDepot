// Obtencion y modificacion de elementos

document.querySelector('b').style.color = 'red';

const titulo = document.querySelector('.titulo');

console.log(titulo.textContent);
// console.log(titulo.innerText);
// console.log(titulo.outerText);
console.log(titulo.innerHTML);
console.log(titulo.outerHTML);

titulo.textContent = 'hola';