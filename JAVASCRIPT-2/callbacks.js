// algo ya mas obsoleto, las promesa o await y async proporcionan un código más legible y manejo más sencillo de las operaciones asíncronas.

// prueba = cb => cb('Lorem ipsum');

// prueba( nombre => console.log(nombre) );

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

const obtenerPersona = (id,cb) =>{
    if (personas[id] === undefined) {
        cb("no se ha encontrado a la persona");
    } else {
        cb(null, personas[id]);
    }
}

obtenerPersona(1, (err,persona) => {
    if (err) {
        console.log(err);
    } else {
        console.log(persona.nombre);
        
        if (persona.edad === undefined) {
            console.log('No se encontraron registros de su edad.')}
        else {
            console.log(persona.edad);
    }
    }
})



