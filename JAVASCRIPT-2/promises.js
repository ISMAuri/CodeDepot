// let nombre = 'pedwefro'

// const promesa = new Promise((resolve, reject) => {
//     if (nombre !== 'pedro') reject('El nombre no es pedro.')
//     else resolve(nombre)
// })

// promesa.then(resultado => 
//     {console.log(resultado)}).catch((e) => {console.log(e)})

class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
};

const datos = [
    ['Fernando Ando', 19],
    ['Camila Nesa'],
    ['Alberto Doliso', 20],
    ['Andaluz Ramirez', 32],
    ['Juan Sevida', 18]
];

const personas = [];

for (let i = 0; i < datos.length; i++) {
    personas[i] = new Persona(datos[i][0],datos[i][1]);
    
};

// console.log(personas[3].edad);

const obtenerPersona = (id) =>{
    return new Promise((res, rej) => {
        if (personas[id] === undefined) rej('No se ha encontrado a la persona.')
        else res(personas[id])
    } ) 

}

obtenerEdad = (id) => {
    return new Promise((res, rej) => {
        if (personas[id].edad === undefined) rej('No se han encontrado registros de edad.')
        else res(personas[id].edad)
    } )
}

let id = 1;

obtenerPersona(id).then((persona) => {
    console.log(persona.nombre);
    return obtenerEdad(id);
    }).then((edd) => {
        console.log(edd)
}).catch((e) => console.log(e))



