
if (2>1) {
    document.write('si' + '<br>');
}

let numero = 2;

while (numero<3) {
    document.write(numero + '<br>');
    numero++;
}


// se ejucuta primero do y despues se verifica while
do {
    document.write(numero + '<br>')
    numero++;
}
while (numero<5);



//break

while (numero<100) {
    document.write(numero + '<br>');
    if (numero == 10) {
        break
    }
    numero++;
}





