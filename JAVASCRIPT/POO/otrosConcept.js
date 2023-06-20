// Otros Conceptos
// HERENCIA
// METODOS ESTATICOS
// METODOS ACCESORES (Getters, Setters)
class Animal {
    constructor(especie, edad, color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} años y soy de color ${this.color}.`;
    
    }
    verInfo(){
        document.write(this.info + '<br>');
    }    
}

class Perro extends Animal {
    constructor(especie,edad,color,raza) {
        super(especie,edad,color);
        this.raza = null;
    }
    set setRaza(newName){
        this.raza = newName;
    }
    get getRaza(){
        return this.raza;
    }
    // static ladrar() {
    //     alert(`${this.especie}: ¡Guau!`);
    // }
}
// Los getters y setters suelen utilizarse para acceder  a propiedades privadas, en el caso de JavaScript, a datos encapsulados

const perro = new Perro('perro','5','marrón','doberman');
const gato = new Animal('gato','6','gris');
const pajaro = new Animal('pajaro','7','verde');

perro.setRaza = 'Beagle';
document.write(perro.getRaza)
