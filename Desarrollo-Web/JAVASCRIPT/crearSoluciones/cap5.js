console.time()
let trabajosPracticos = '100 minutos de trabajos practicos';
let estudio = '100 minutos de estudio';
let trabajo = '240 minutos de trabajo';
let homework = '30 minutos tareas del hogar';
let descanso = '10 minutos de descanso';

console.log('TAREAS');

for (let i = 1; i <= 14; i++) {
    
    if (i == 1) {
        console.group('Semana 1');
    }

    console.groupCollapsed(`dia ${i}`);
    console.log(trabajo);
    console.log(descanso);
    console.log(estudio);
    console.log(trabajosPracticos);
    console.log(homework)
    console.groupEnd()

    if (i == 7) {
        console.groupEnd()
        console.group('Semana 2')
    }

};

console.groupEnd()
console.log('hol')
console.timeEnd()





// const materias = {
//     fisica: [90,6,3,'fisica'],
//     quimica: [84,8,2,'quimica'],
//     biologia: [92,7,4,'biologia'],
//     programacion: [96,10,4,'programacion'],
//     matematica: [89,6,3,'matematica'],
//     ingles: [95,9,2,'ingles']
// };

// const aprobacion = () => {
//     for (materia in materias) {

//         let asistencias = materias[materia][0];
//         let promedio = materias[materia][1];
//         let trabajos = materias[materia][2];

//         console.log(materias[materia][3]);

//         if (asistencias >= 90) {
//             console.log('%cAsistencias en orden','color:green');
//         } else {
//             console.log('%cFalto de Asistencias','color:red');
//         }

//         if (promedio >= 7) {
//             console.log('%cPromedio Aprobado','color:green');
//         } else {
//             console.log('%cPromedio Desaprobado','color:red');
//         }
        
//         if (trabajos >= 3) {
//             console.log('%cTrabajos practicos en orden','color:green');
//         } else {
//             console.log('%cFaltan trabajos practicos','color:red');
//         }
//     }
// };

// aprobacion()