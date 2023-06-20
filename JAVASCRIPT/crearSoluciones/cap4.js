//PROBLEMA 3

const materias = {
fisica: ['pedro', 'alberto', 'daniel', 'sebastian'],
programacion: ['pedro', 'alberto',],
quimica: ['pedro', 'alberto', 'daniel', 'sebastian'],
biologia: ['alberto', 'daniel', 'sebastian']
};


const inscribir = (alumno, materia) => {
    let alumnos = materias[materia];
    
    if (alumnos.length >= 20) {
        return `Mil disculpas ${alumno}, las clases de ${materia} ya estan llenas.`;
    } else {
        alumnos.push(alumno);
        return `¡Felicidades ${alumno}! Te has inscrito a la clase de ${materia}.`
    }
}


document.write(materias['biologia'] + '<br>')


document.write(inscribir('isma','biologia') + '<br>')


document.write(materias['biologia'] + '<br>')






//PROBLEMA 2

// const obtenerInformacion = (materia) => {
//     const materias = {
//         fisica: ['Perez', 'pedro', 'alberto', 'daniel', 'sebastian'],
//         programacion: ['Rodriguez', 'pedro', 'alberto',],
//         quimica: ['Hernandez', 'pedro', 'alberto', 'daniel', 'sebastian'],
//         biologia: ['Dalto', 'alberto', 'daniel', 'sebastian']
//     };

//     if (materias[materia] !== undefined) {
//         return [materias, materia, materias[materia]];
//     } else {
//         return materias;
//     }
// };

// const mostrarInformacion = (materia) =>{
//     const informacion = obtenerInformacion(materia);
//     const profe = informacion[2][0];
//     const alumnos = informacion[2];
//     alumnos.shift();

//     if (informacion !== false){
//         document.write(`Alumnos presentes en la clase de ${informacion[1]} del profesor ${profe}: <b>${alumnos}`)
//     }
// };

// // mostrarInformacion('fisica')

// const cantidadDeClases = (alumno)=> {
//     const informacion = obtenerInformacion();
//     let clasesPresentes = [];
//     let cantidadTotal = 0;

//     for (const info in informacion) {
//         const alumnos = informacion[info];
//         if (alumnos.includes(alumno)) {
//             cantidadTotal++;
//             clasesPresentes.push(" " + info)
//         }
//     }
//     return `${alumno} a asiste a ${cantidadTotal} clases. <br> Esta cursando las clases ${clasesPresentes}.`
// };
// cantidadClases = cantidadDeClases('pedro')
// document.write(cantidadClases)





//PROBLEMA 1

// class Operaciones {
//     sumar(x, y) {
//         return parseInt(x) + parseInt(y);
//     }
  
//     restar(x, y) {
//         return parseInt(x) - parseInt(y);
//     }
  
//     multiplicar(x, y) {
//         return parseInt(x) * parseInt(y);
//     }
  
//     dividir(x, y) {
//         return parseInt(x) / parseInt(y);
//     }

//     potenciar(x, y) {
//         return parseInt(x)**parseInt(y)
//     }

//     raizCuadrada(x) {
//         return Math.sqrt(parseInt(x))
//     }
//     raizCubica(x) {
//         return Math.cbrt(parseInt(x))
//     }
//   }

// const operar = new Operaciones(); 

// function calculadora(){
//     operacion = prompt('¿Que operacion deseas utilizar? \n\n 1: Suma \n 2: Resta \n 3: Multiplicacion \n 4: Division \n 5: Potenciacion \n 6: Raiz Cuadrada \n 7: Raiz Cubica' )
//     if (operacion == 1) {
//         let num1 = prompt('Primer numero para sumar');
//         let num2 = prompt('Segundo numero para sumar');
//         resultado = operar.sumar(num1,num2);
//         alert(`tu resultado es: ${resultado}`);
//     }
//     else if (operacion == 2) {
//         let num1 = prompt('Primer numero para restar');
//         let num2 = prompt('Segundo numero para restar');
//         resultado = operar.restar(num1,num2);
//         alert(`tu resultado es: ${resultado}`);
//     }
//     else if (operacion == 3) {
//         let num1 = prompt('Primer numero para multiplicar');
//         let num2 = prompt('Segundo numero para multiplicar');
//         resultado = operar.multiplicar(num1,num2);
//         alert(`tu resultado es: ${resultado}`);
//     }
//     else if (operacion == 4) {
//         let num1 = prompt('Primer numero para dividir');
//         let num2 = prompt('Segundo numero para dividir');
//         resultado = operar.dividir(num1,num2);
//         alert(`tu resultado es: ${resultado}`);
//     }
//     else if (operacion == 5) {
//         let num1 = prompt('Numero a potenciar');
//         let num2 = prompt('Potencia del numero');
//         resultado = operar.potenciar(num1,num2);
//         alert(`tu resultado es: ${resultado}`);
//     }
//     else if (operacion == 6) {
//         let num1 = prompt('Raiz cuadrada de:');
//         resultado = operar.raizCuadrada(num1);
//         alert(`tu resultado es: ${resultado}`);
//     }
//     else if (operacion == 7) {
//         let num1 = prompt('Raiz cubica de:');
//         resultado = operar.raizCubica(num1);
//         alert(`tu resultado es: ${resultado}`);
//     }
//     else {
//         alert('No añadiste un valor valido. Ingresa un valor del 1 al 7 como se especifica.');
//         return calculadora();
//     }
// }
// calculadora()

