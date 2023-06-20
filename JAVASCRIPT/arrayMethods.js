let nombres = ['pedro', 'maria', 'francisco', 'leonardo'];

// let resultado = nombres.slice(0,2);

// document.write(nombres);

let resultado = nombres.filter(nombre => nombre.length > 5)

document.write(resultado)

//            __Transformadores__
// .pop(elimina el ultimo elemento del array y lo retorna)
// .shift(elimina el primer elemento del array y lo retorna)
// .push(puede añadir cadenas si le añadimos parametros(las añade al final) y retorna el numero de elementos(aunque no añadamos parametros))
// .reverse(invierte el orden)
// .unshift(añade elementos al principio y retorna el numero de elementos(aunque no añadamos parametros))
// .sort(ordena los elementos segun el alfabeto)
// .splice(le voy a dedicar un buen parrafo):
//en el primer param especificamos el indice del que queremos empezar, en el segundo hasta que indice queremos seleccionar, elimina los elementos desde el primer indice hasta el segundo indice -1(si seleccionamos por ejem 0,2 eliminara elementos encontrados en 0 y 1,pero no 2), podemos añadir mas parametros para insertar cadenas basicamente añadiendolas en el lugar en el que se encontraban los otros elementos; si en el segundo parametro escribimos 0 no elimina nada y podemos añadir sin necesidad de eliminar. Resumen: elimina o no, agrega o no.

//  __Accesores__
// .join(crea una cadena de texto con el array y podemos separar cada elemento con algun o algunos caracteres que añadamos como parametro)
// .slice(especificamos primer indice, y el segundo) devuelve los elementos del array del indice que especificamos desde el primer al segundo(-1) parametro, si queremos que devuelva todo el array no añadimos parametros 


//    __De Repeticion__
// .forEach(filtra elementos de un array)
// .filter(puede filtrar elementos de un array pero se pueden imponer ciertos criterios o requisitos) 
// Estas dos se entienden mas viendolas en acción