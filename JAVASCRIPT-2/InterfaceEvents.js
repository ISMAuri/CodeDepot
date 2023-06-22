// USER INTERFACE EVENTS
button = document.querySelector('.button');
contenedor1 = document.querySelector('.contenedorrojo');
contenedor2 = document.querySelector('.contenedorazul');
img = document.querySelector('img');
input = document.querySelector('input');

img.addEventListener( "error", () => { console.log('error al cargar la imagen'); } ); // cuando un archivo multimedia no se llega a cargar bien

addEventListener( "load", () => { console.log('el sitio a cargado correctamente'); } );

// addEventListener( "beforeunload", () => { console.log('cuando te vas del sitio'); } );

addEventListener( "unload", () => { console.log('antes que te vayas del sitio'); } );

addEventListener( "resize", () => { console.log('ajustando resolucion(?'); } );

addEventListener( "scroll", () => { console.log('cuando se scrolea'); } );

addEventListener( "unload", () => { console.log('antes que te vayas del sitio'); } );

input.addEventListener( "select", (e) => { 
    console.log(input.value.substring(e.target.selectionStart, e.target.selectionEnd))
 } );

 