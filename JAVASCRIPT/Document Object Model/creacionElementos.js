
const contenedor = document.querySelector('.contenedor');

// const item = document.createElement('LI')

// const texto = document.createTextNode('This is a list item.')

// console.log(texto)

// //item.textContent = 'un simple texto';
// item.appendChild(texto)

// console.log(item)

fragmento = document.createDocumentFragment()

for (let i = 0; i < 12; i++) {
    const item = document.createElement('LI');
    item.textContent = 'Este es un item de la lista';
    fragmento.appendChild(item);
}

contenedor.appendChild(fragmento)