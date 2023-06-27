// Get por defecto
// let request = fetch("https://reqres.in/api/unknown/2")

//                  .text,.json
// request.then(res => res.json()).then(res => console.log(res))

// let request = fetch('https://reqres.in/api/users', {
//     method : "post",
//     body : JSON.stringify({
//         'nombre' : 'juan',
//         'apellido': 'alberto'
//     }),
//     headers: {'Content-type' : "application/json"}
// });

// request.then(res => res.json()).then(res => console.log(res));

let imagen = document.querySelector('.imagen');

fetch('mc.png').then(res => res.blob()).then(img => imagen.src = URL.createObjectURL(img))

