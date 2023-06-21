// Conceptos Basicos de POO
// "CLASE"
// "OBJETO"
// "ATRIBUTO"
// "METODO"
// "CONSTRUCTOR"
// "INSTANCIACION"

// Caracteristicas de la POO
// "ABSTRACCION"
// "MODULARIDAD"
// "ENCAPSULAMIENTO"
// "POLIMORFISMO"



class animal {
    constructor(especie, edad, color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        if (this.color === 'multicolor') {
            this.info = `Soy ${this.especie}, tengo ${this.edad} años, soy ${this.color}, y tengo un nombre realmente raro.`;
        } else {
            this.info = `Soy ${this.especie}, tengo ${this.edad} años y soy de color ${this.color}.`;
        }
    }
    verInfo(){
        document.write(this.info + '<br>')
    }
}
const perro = new animal('perro','5','marron');

const gato = new animal('gato','6','gris');
const WunderpusPhotogenicus = new animal('WunderpusPhotogenicus','7','multicolor');


perro.verInfo()
gato.verInfo()
WunderpusPhotogenicus.verInfo()
// document.write(perro.info + '<br>')
// document.write(gato.info + '<br>')
// document.write(WunderpusPhotogenicus.info + '<br>')

console.log(perro)

// Resumen de cada concepto y caracteristica

// "CLASE": Plantilla para crear objetos que define atributos y métodos.
// "OBJETO": Instancia de una clase que contiene datos y comportamientos específicos.
// "ATRIBUTO": Variables que almacenan datos en un objeto.
// "METODO": Funciones en una clase que realizan operaciones o manipulan los datos del objeto.
// "CONSTRUCTOR": Método especial para inicializar un objeto cuando se crea una instancia de una clase.
// "INSTANCIACION": Proceso de crear un objeto específico a partir de una clase.

// "ABSTRACCION": Enfocarse en las características relevantes de un objeto y ocultar los detalles internos complejos.
// "MODULARIDAD": Dividir un programa en módulos independientes para facilitar el desarrollo, mantenimiento y reutilización del código.
// "ENCAPSULAMIENTO": Ocultar los detalles internos de un objeto y proporcionar una interfaz para interactuar con él.
// "POLIMORFISMO": Capacidad de objetos de diferentes clases para responder a la misma llamada a métodos de manera distinta según su tipo.