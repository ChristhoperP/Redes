function validarSiNumero(numero) {
  if (!/^([0-9])*$/.test(numero))
    alert("El valor " + numero + " no es un numero crack");
  return false;
}

function calcular2() {

  var o1 = parseInt(document.getElementById('o1').value);
  var o2 = parseInt(document.getElementById('o2').value);
  var o3 = parseInt(document.getElementById('o3').value);
  var o4 = parseInt(document.getElementById('o4').value);
  var prefijo = parseInt(document.getElementById('prefijo').value);


  if ((o1 >= 0 && o1 <= 255) &&
    (o2 >= 0 && o2 <= 255) &&
    (o3 >= 0 && o3 <= 255) &&
    (o4 >= 0 && o4 <= 255) &&
    (prefijo >= 0 && prefijo <= 32)) {
    alert("El valor del prefijo " + prefijo + " esta vergon ");
  } else {
    alert("El valor no esta en el rango establecido crack verifica que este en [0-255] y el prefijo en [0-32]");
  }

}


