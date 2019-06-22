//Variables locales
var primerooct;
var segundooct;
var terceroct;
var cuartooct;
var prefijo;
var br;//bits de red
var brc;//bits de host del octeto cambiante
var occ;//octeto que cambia
var ocval;//el número del octeto que cambia
var id;
var broad;
var mask;
var tipoRed;

// Función para validar los campos del formulario
(function () {
    'use strict';

    window.addEventListener('load', function () {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');

        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                    form.classList.add('was-validated');
                    console.log("tamos mal :c");
                } else {
                    /* console.log("tamos bien"); */
                    var parametros = $("#formulario-submeteo").serialize();
                    console.log(parametros);
                }

            }, false);
        });
    }, false);
})();

//Evita que recargue la página :v
$("#formulario-submeteo").submit(function () {
    return false;
});

//ID, Broadcast, mascara
function calcular() {
    br = prefijo - Math.floor(prefijo / 8) * 8;
    brc = 8 - br;
    occ = 4 - Math.floor(prefijo / 8);

    //aqui se obtendría el ocval segun el occ
    ocval = parseInt($('#o' + occ).val());
    alert('octeto cambia: ' + occ + ' valor del octeto: ' + ocval);

    id = Math.floor(ocval / Math.pow(2, brc)) * Math.pow(2, brc);

    broad = id + Math.pow(2, brc) - 1;

    var c = 0;
    for (let index = 0; index < brc; index++) {
        c = c + Math.pow(2, index);
    }

    if (occ == 3) {

        mask = '255.' + (255 - c).toString() + '.0.0';

    } else if (occ == 2) {

        mask = '255.255.' + (255 - c).toString() + '.0';

    } else if (occ == 1) {
        mask = '255.255.255.' + (255 - c).toString();
    }

}

//aquí ejecutar las funciones
$(document).ready(function () {
    //calcular();
});

function TipoRed() {
    if (prefijo >= 24) {
        if (cuartooct >= 192 && cuartooct <= 223)
            tipoRed = "C";
    }
    if (prefijo >= 16) {
        if (cuartooct >= 128 && cuartooct <= 191)
            tipoRed = "B";
    }
    if (prefijo >= 8) {
        if (cuartooct >= 0 && cuartooct <= 127)
            tipoRed = "A";
    }

}


function validarSiNumero(numero) {
    if (!/^([0-9])*$/.test(numero))
        alert("El valor " + numero + " no es un numero crack");
    return false;
}

function validar() {

    var o1 = parseInt(document.getElementById('o1').value);
    var o2 = parseInt(document.getElementById('o2').value);
    var o3 = parseInt(document.getElementById('o3').value);
    var o4 = parseInt(document.getElementById('o4').value);
    var prefijoh = parseInt(document.getElementById('prefijo').value);


    if ((o1 >= 0 && o1 <= 255) &&
        (o2 >= 0 && o2 <= 255) &&
        (o3 >= 0 && o3 <= 255) &&
        (o4 >= 0 && o4 <= 255) &&
        (prefijoh >= 0 && prefijoh <= 30)) {
        alert("El valor del prefijo " + prefijoh + " esta vergon ");

        primerooct = o1;
        segundooct = o2;
        terceroct = o3;
        cuartooct = o4;
        prefijo = prefijoh;

        TipoRed();

        if (tipoRed == 'A' || tipoRed == 'B' || tipoRed == 'C') {
            calcular();
            imprimir();
            limpiar();
        }else{
            alert('El prefijo debe corresponder al tipo de red.');
        }

    } else {
        alert("El valor no esta en el rango establecido crack verifica que este en [0-255] y el prefijo en [0-30]");
    }

}

function limpiar() {
    primerooct = 0;
    segundooct = 0;
    terceroct = 0;
    cuartooct = 0;
    prefijo = 0;
    br = 0;
    brc = 0;
    occ = 0;
    ocval = 0;
    id = 0;
    broad = 0;
    mask = '';
    tipoRed = '';
}

function imprimir() {
    alert('Tipo de red: ' + tipoRed +
        '\nbits de red: ' + br + ', \n' +
        'bits de host del oct cambiante: ' + brc + ', \n' +
        'Octeto que cambia: ' + occ + ', \n' +
        'ID: ' + id + ', \n' +
        'Broadcast: ' + broad + '\nmask: ' + mask);
}