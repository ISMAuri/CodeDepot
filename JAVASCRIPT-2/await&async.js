// const objeto = {
//     propiedad1 : 'valor1',
//     propiedad2 : 'valor2',
//     propiedad3 : 'valor3'
// };


// const obtenerInformacion = () => {
//     return new Promise((res) => {
//         setTimeout(() => {res(objeto)},1000)
//     })
// };

// obtenerInformacion().then(res => console.log(res));


const obtenerInfo = (text) => {
    return new Promise((res) => {
        setTimeout(() => {res(text)},Math.random()*200)
    })
};

const mostrarInfo = async () => {
    data1 = await obtenerInfo('1. fernando');
    data2 = await obtenerInfo('2. bernardo');
    data3 = await obtenerInfo('3. alfredo');
    console.log(data1);
    console.log(data2);
    console.log(data3);
}

mostrarInfo()