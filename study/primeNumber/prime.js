//prime number

function makeArray(num) {
  for (var i = 1; i < num; i++){
    var numList = [i];
  }
}

function printPrimeNum(num) {
  var numList = [];
  for (var k = 2; k <= num; k++){
    numList = numList.concat(k);
  }

  var numList = numList;
  for (var i = 1; i < num; i++){
    for (var j = 2; j < i; j++){
      console.log(i + ' / ' + j + ' remains ' + i % j);
      if (i !== j && i % j == 0) {
        console.log(i + 'is not prime number');
        break;
      }
    }
  }
  console.log(numList);
}
printPrimeNum(10);