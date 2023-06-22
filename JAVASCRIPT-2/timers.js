// Nota: consumen bastantes recursos

const temporizador = setTimeout( () => {
    console.log('se expresa en milisegundos, se ejecuta una vez')
}, 200 )


clearTimeout(temporizador)


intervalo = setInterval(() => {
    console.log('se ejecuta cada .2 segundos')
}, 200)


setTimeout(() => {
    clearInterval(intervalo)
}, 1000);
