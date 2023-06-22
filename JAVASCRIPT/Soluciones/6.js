
const contenedor = document.querySelector('.flex-container');

crearLlave = (nombre, modelo, precio)=>{

    nombre = `<h2>${nombre}</h2>`;
    modelo = `<h3>${modelo}</h3>`;
    precio = `<p><b>Precio</b>: $${precio}</p>`;
    return {'nombre' : nombre,
    'precio' : precio,
    'modelo' : modelo
};
};

const changeHidden = (number) => {
    document.querySelector('.key-data').value = number
}

let documentFragment = document.createDocumentFragment();

for (let i = 1; i <= 20; i++) {

    let modeloRandom = Math.round(Math.random()*300);
    let precioRandom = (Math.random()*100).toFixed(2);

    let llave = crearLlave(`Llave ${i}`,`modelo ${modeloRandom}`, precioRandom);

    let div = document.createElement('div');
    div.addEventListener('click',()=>{changeHidden(modeloRandom)})
    div.tabIndex = i;
    div.classList.add(`item-${i}`,`flex-item`);

    div.innerHTML = "<img src='https://previews.123rf.com/images/sqback/sqback2002/sqback200200005/141253737-llave-antigua-aislada-sobre-fondo-blanco.jpg'>" + llave['nombre'] + llave["modelo"] + llave['precio'];

    documentFragment.appendChild(div);
}

contenedor.appendChild(documentFragment);


