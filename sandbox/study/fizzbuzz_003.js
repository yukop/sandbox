// 配列にして、join で間にカンマを付ける

var yukop = new Array();
for (var i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0){
        yukop.push('FizzBuzz');
    }
    else if (i % 3 === 0){
        yukop.push('Fizz');
    }
    else if (i % 5 === 0) {
        yukop.push('Buzz');
    }
    else {
        yukop.push(i);
    }
}
document.write(yukop.join(', '));

