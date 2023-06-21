// Problema 1

// let free = false;

// const validarCliente = time => {
//     let edad = prompt('¿Que edad tenes?');
//     if (edad >= 18) {
//             if (time >= 2 && time < 7 && !free) {
//                 alert('Cumples con los requisitos de edad, por ser el primero puedes pasar totalmente GRATIS porque sos la primer persona despues de las 2 PM.');
//                 free = !free;
//             } else {
//                 alert('Cumples con los requisitos de edad, puedes pasar, tenes que pagar la entrada.');
//             }
//     } else {
//         alert('No eres mayor de edad, por ende no puedes entrar.');
//     }
// }

// validarCliente(2);
// validarCliente(24);
// validarCliente(0.2);
// validarCliente(0.6);
// validarCliente(1);
// validarCliente(2);
// validarCliente(2.4);
// validarCliente(3);


//Problema 2

// let cantidad = prompt('¿cuantos alumnos son?');
// let alumnos = [];

// for (i = 0; i < cantidad; i++) {
//     alumnos[i] = [prompt(`Nombre del alumno numero ${i + 1}.`),0];
// }

// const tomarAsistencia = (nombre,p)=>{
//     let presencia = prompt(nombre);
//     if (presencia == 'p' || presencia == 'P') {
//         alumnos[p][1]++;
//     }
// }



// for (i = 0; i < 30; i++) {
//     for (alumno in alumnos) {
//     tomarAsistencia(alumnos[alumno][0], alumno)
//     }
// }

// for (alumno in alumnos) {
//     let resultado = `${alumnos[alumno][0]}: <br> 
//     _______Presentes: ${alumnos[alumno][1]} <br>
//     _______Ausencias: ${30 - parseInt(alumnos[alumno][1])} `;
//     if (30 - alumnos[alumno][1] > 18) {
//     resultado += "<b style='color:red'> REPROBADO POR INASISTENCIAS</b><br><br>";
//     } else {
//         resultado += '<br><br>'
//     } document.write(resultado)

    
// }



// problema 3

// Intentare añadirlo a una funcion para retornarla si el usuario pone un caracter invalido

const sumar = (x,y)=> {
    return parseInt(x) + parseInt(y)
}
const restar = (x,y)=> {
    return parseInt(x) - parseInt(y)
}
const multiplicar = (x,y)=> {
    return parseInt(x) * parseInt(y)
}
const dividir = (x,y)=> {
    return parseInt(x) / parseInt(y)
}

function calculadoraBasica(){
    operacion = prompt('¿Que operacion deseas utilizar? \n\n 1: Suma \n 2: Resta \n 3: Multiplicacion \n 4: Division ')
    if (operacion == 1) {
        let num1 = prompt('Primer numero para sumar');
        let num2 = prompt('Segundo numero para sumar');
        resultado = sumar(num1,num2);
        alert(`tu resultado es: ${resultado}`);
    }
    else if (operacion == 2) {
        let num1 = prompt('Primer numero para restar');
        let num2 = prompt('Segundo numero para restar');
        resultado = restar(num1,num2);
        alert(`tu resultado es: ${resultado}`);
    }
    else if (operacion == 3) {
        let num1 = prompt('Primer numero para multiplicar');
        let num2 = prompt('Segundo numero para multiplicar');
        resultado = multiplicar(num1,num2);
        alert(`tu resultado es: ${resultado}`);
    }
    else if (operacion == 4) {
        let num1 = prompt('Primer numero para dividir');
        let num2 = prompt('Segundo numero para dividir');
        resultado = dividir(num1,num2);
        alert(`tu resultado es: ${resultado}`);
    }
    else {
        alert('No añadiste un valor valido. Ingresa un valor del 1 al 4 como se especifica.');
        return calculadoraBasica();
    }
}
calculadoraBasica()
// Quedo mejor de lo que esperaba 


