// const getName = () => {
//     fetch('info.txt')
//     .then(res => {
//         if (res.ok) Promise.resolve(res)
//         else Promise.reject(res)
//     }).then(res => console.log(res)).catch(e => console.log(e))
// };   undefined

const getName = async () => { 

    let request = await fetch('info.txt');
    let result = await request.json();
    console.log(result)


}

getName()