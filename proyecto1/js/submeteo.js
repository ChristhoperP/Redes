//Variables locales
var primerooct;
var segundooct;
var terceroct;
var cuartooct;
var prefijo = 19;
var br;//bits de red
var brc;//bits de host del octeto cambiante
var occ;//octeto que cambia
var ocval = 129;//el número del octeto que cambia
var id;
var broad;
var mask;

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

    //alert(br + ', ' + brc + ', ' + occ + ', ' + id + ', ' + broad + ' mask: ' + mask);

}

//aquí ejecutar las funciones
$(document).ready(function () {
    calcular();
});