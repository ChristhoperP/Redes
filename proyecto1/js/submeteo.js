// Example starter JavaScript for disabling form submissions if there are invalid fields
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

$("#formulario-submeteo").submit(function () {
    return false;
});

$("#tamanio").val(3);

var ta=parseInt($("#tamanio").val());
var letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

$("#tamanio").change(function(){
    
    var tn=parseInt($(this).val());
    /* alert(tn); */

    if(tn>0 && tn<=27){
        
        if(tn>ta){
            for (var index = ta+1; index <= tn; index++) {
                $("#subredes").append(
                    `<div class="col-md-6 mb-1 red-${index}">
                        <input type="text" class="form-control" name="primer-nombre" id="primer-nombre" placeholder=""
                            value="${letras[index-1]}" required>
                        <div class="invalid-feedback">
                            Se requiere una red.
                        </div>
                    </div>
                    <div class="col-md-6 mb-1 red-${index}">
                        <input type="number" class="form-control" name="segundo-nombre" id="segundo-nombre" placeholder=""
                            value="" required>
                        <div class="invalid-feedback">
                            Se requiere una cantidad.
                        </div>
                    </div>
                    `
                );
            }
        }else if(tn<ta){
            for (var index = ta; index > tn; index--) {
                $(".red-"+index).remove();
            }
        }

        ta=tn;
    }else{
        alert("tiene que ser un número mayor que 0 y menor que 27.");
        $(this).val(ta);
    }

});

function direccion(dir) {
    /* . & / */
    
}