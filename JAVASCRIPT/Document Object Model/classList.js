
const titulo = document.querySelector('.titulo');

titulo.classList.remove('titulo')
titulo.classList.add('grande')
titulo.classList.replace('grande', 'pequeño')

valor = titulo.classList.item(0)

console.log(valor)

contener = titulo.classList.contains('esternocleidomastoideo') 

console.log(contener)



// Basicamente ALTERA, si la clase existe la elimina, si no existe la agrega
titulo.classList.toggle('title')

//si como segundo parametro ponemos true siempre la agrega(o no la elimina) y si ponemos false siempre la saca(o no la agrega)

//Explicacion
// Si toggle detecta que no existe 'x', la agrega devolviendo true, si 'x' existe la elimina devolviendo false


