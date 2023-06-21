for (let i = 0; i <= 20; i++) {
    if (i==9) {
        continue;
    }
    document.write(i + '<br>')
    if (i==13) {
        break;
    }
}

document.write('<br>')
let animales = ['gato', 'perro', 'tiranosaurio rex'];

// for in imprime clave, posicion, etc.
for (animal in animales) {
    document.write(animal + '<br>');
}

document.write('<br>')

// for of imprime valor
for (animal of animales) {
    document.write(animal + '<br>');
}

document.write('<br>')

array1 = ['hola','pa']
array2 = ['si','nvkadfjsk',array1,'jose']

elfor:
for (let array in array2) {
    if (array == 2) {
        for (let array of array1) {
            document.write(array + '<br>')
            break elfor;
        }
    } else {
        document.write(array2[array] + '<br>')
    }
}


//forEach

let nombres = ['Juan', 'María', 'Pedro', 'Ana'];

// nombres.forEach(function(nombre) {
//     console.log(nombre);
// });

nombres.forEach(nombre => console.log(nombre));





