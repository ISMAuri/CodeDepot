// Problema 1
// class celular{
//     constructor(modelo,color,peso,resolucionPantalla,cam,ram){
//         this.modelo = modelo;
//         this.color = color;
//         this.peso = peso;
//         this.rdp = resolucionPantalla;
//         this.cam = cam;
//         this.ram = ram; 
//         this.encendido = false;
//     }
//     power(){
//     if (this.encendido == false){
//         alert('celular encendido.');
//         this.encendido = true;
//     } else {
//         alert('celular apagado.');
//     }
//     }
//     reiniciar(){
//         if (this.encendido == true){
//             alert('reiniciando celular.');
//         }else {
//             alert('celular apagado');
//         }
//     }
//     tomarFoto(){
//         alert(`tomando foto con una resolucion de ${this.cam}.`);
//     }
//     grabarVideo(){
//         alert(`grabando video con una resolucion de ${this.cam}.`);
//     }
//     info(){
//         return `
//         <br><br> <b style= "color: #355c7d;">${this.modelo}</b> <br><br>
//         <b style= "color: gray;">Características principales</b> <br>
//         Color: <b>${this.color}</b><br>
//         Peso: <b>${this.peso}</b><br>
//         Resolucion de Pantalla: <b>${this.rdp}</b><br>
//         Resolucion de Camara: <b>${this.cam}</b><br>
//         Memoria RAM: <b>${this.ram}</b>
//         `
//     }
// }
// //    constructor(color,peso,resolucionPantalla,camara,ram){
// j2Prime = new celular('Galaxy J2 Prime','negro','160g','540 x 960 px','8 MP','1.5GB' )
// j5 = new celular('Galaxy J5','plateado','146g','720 x 1280 px', '13MP','1.5GB')
// j1Mini = new celular('Galaxy J1 Mini','gris','120g','480 x 800 px','5 MP', '0.76GB')

// // j2Prime.power()
// // j2Prime.reiniciar()
// // j2Prime.tomarFoto()
// // j2Prime.grabarVideo()
// // j2Prime.power()

// document.write(`Celulares <br> <br> ${j2Prime.info()} <br> ${j5.info()} <br> ${j1Mini.info()} <br>
// `)

// Problema 2

// class celularGamaAlta extends celular {
//     constructor(modelo,color,peso,resolucionPantalla,cam,ram,extracam){
//         super(modelo,color,peso,resolucionPantalla,cam,ram);
//         this.extracam = extracam;
// }
// grabarVideoLento(){
//     alert('grabando video en camara lenta.')
// }
// reconocimientoFacial(){
//     alert('iniciando reconocimiento facial.')
// }
// infoGamaAlta(){
//     return `${this.info()}<br> Resolucion de Camara Extra: <b>${this.extracam}</b>`
// }
// }

// i14 = new celularGamaAlta('iPhone 14','blanco estelar','172g','1170 x 2532 px', '12 MP','6GB','12 MP')
// s22 = new celularGamaAlta('Galaxy S22','phantom black','167g','1080 x 2340 px','50 MP','8GB','12 MP + 10 MP')

// document.write(`<br><br><br>Celulares Gama Alta <br><br> ${i14.infoGamaAlta()} <br> ${s22.infoGamaAlta()}`)

// Problema 3 
class App {
    constructor(descargas,puntuacion,peso){
        this.descargas = descargas;
        this.puntuacion = puntuacion;
        this.peso = peso;
        this.iniciada = false;
        this.instalada = false;
    }
    iniciar(){
        if (this.iniciada == false && this.instalada == true){
            this.iniciada = true;
            alert('app inicializada.');
        } else {
            alert('...')
        }
    }
    cerrar(){
        if (this.iniciada == true && this.instalada == true){
            this.iniciada = false;
            alert('app cerrada.');
        } else {
            alert('...')
        } 
    }
    instalar(){
        if (this.instalada == false){
            this.instalada = true;
            alert('app instalada correctamente.')
        } else {
            alert('...')
        }
    }
    desinstalar(){
        if (this.instalada == true){
            this.instalada = false;
            alert('app desinstalada correctamente.')
        } else {
            alert('...')
        }
    }
    appInfo(){
        return `INFORMACION <br><br> Descargas: ${this.descargas}<br>Puntuación: ${this.puntuacion}<br>Espacio en Memoria: ${this.peso}`
    }
}

randomApp1 = new App('20.000+','5 estrellas','900mb')
randomApp2 = new App('16.000+','4.6 estrellas','200mb')
randomApp3 = new App('112.000+','3.9 estrellas','80mb')

// randomApp.instalar()
// randomApp.iniciar()
// randomApp.cerrar()
// randomApp.desinstalar()
document.write(`${randomApp1.appInfo()}<br>${randomApp2.appInfo()}<br>${randomApp3.appInfo()}<br>`)