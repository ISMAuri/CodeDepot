// get por defecto
// axios('info.txt').then(res => console.log(res));


axios.post('https://reqres.in/api/users', {
    'saludo' : 'hola'
}).then(res => console.log(res));

