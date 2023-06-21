let cadena = 'cadena de prueba prueba prueba';
cadena2 = 'prueba ';

Hola = '  Pedro    ';


resultado = Hola.trimStart();



document.write(resultado.length);

// .concat(concatenar)

// .startWith(verifica si empieza con)
// .endsWith(verifica si termina con)
// .includes(como start y ends, pero en cualquier parte de la cada)
// .indexOf(devuelve el primer indice en el que se encuentra la cadena si no se encuentra en la misma tira -1)
// .lastIndexOf(como indexOf pero si hay varias veces la misma cadena, tira el primer indice de la ultima cadena encontrada)

// .padStart(numero de indices que queremos que tenga la cadena cuando se rellene la cadena con el segundo parametro, cadena con la que queremos que lo rellene) todo esto al inicio
// .padEnd(como padStart pero al final) 
// .repeat(repetir la cadena la cantidad de veces especificadas)

// .split(especificamos a partir de que caracter o caracteres dividir la cadena y devuelve un array separandolos)
// .substring(especificas adonde quieres empezar la nueva cadena, especificas donde queres que termine) Crea una nueva cadena especificando de cual a cual indice
// .toLowerCase(texto minuscula)
// .toUpperCase(texto mayuscula)
// .toString(convierte a string)
// .trim(elimina espacios en blanco al inicio y al final) este empieza contar de 1
// .trimEnd(trim al final)
// .trimStart(trim al inicio)
// .valueOf() retorna el valor primitivo de un objeto