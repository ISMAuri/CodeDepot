// Necesario para el envio y recepcion de bases de datos

const objeto = {variable1 : 'pedro', variable2 : 'jorge'} // esta serializado

const serializar = JSON.stringify(objeto)

const deserializar =  JSON.parse(serializar)

console.log(typeof objeto, objeto)

console.log(typeof serializar, serializar)

console.log(typeof deserializar, deserializar)
