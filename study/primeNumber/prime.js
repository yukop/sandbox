//prime number

function printPrimeNum(num) {
  var numList = [];
  for (var k = 1; k <=num; k++) {
    numList = numList.concat(k);
  }
  for (var i = 2, l = numList.length; i < l; i++){
    for (var j = 2; j < i; j++){
      if (numList[i] % j === 0) {
        numList[i] = null;
      }
    }
  }
  var primeNumList = [];
  for (var i = 1, l = numList.length; i < l; i++) {
    if (numList[i] !== null) {
      primeNumList = primeNumList.concat(numList[i]);
    }
  }
  document.form1.primeNum.value = primeNumList + ' ( total: ' + primeNumList.length + ' )';  
}
