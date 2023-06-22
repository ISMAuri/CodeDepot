
button = document.querySelector('.button');
contenedor1 = document.querySelector('.contenedorrojo');
input = document.querySelector('.input');



input.addEventListener( "keydown", () => { console.log('tecla presionada'); } );

input.addEventListener( "keypress", () => { console.log('tecla añadida'); } );

input.addEventListener( "keyup", () => { console.log('tecla soltada'); } );

input.addEventListener( "select", (e) => { console.log(e); } );

