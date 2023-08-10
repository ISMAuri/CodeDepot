let request;

if (window.XMLHttpRequest) request = new XMLHttpRequest();
else request = new ActiveXObject('Microsoft.XMLHTTP');

// NO SE HACE ASI, un ejemplo
request.addEventListener('load', () => {
    if (request.status === 200) console.log(JSON.parse(request.response)) // viene serializado, sin el parse;
    else console.log('ha ocurrido un error.')
})

request.open('get','info.txt');
request.send();

console.log(request);
