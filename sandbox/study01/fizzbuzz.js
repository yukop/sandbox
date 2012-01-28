// document.write をまとめて最後に出力して、substring で最後のカンマを取る

var yukop = '';

for (var i = 1 ; i < 101; i++) {
    if (i % 3 === 0 && i % 5 === 0){
        yukop += 'FizzBuzz, ';
    }
    else if (i % 3 === 0){
        yukop += 'Fizz, ';
    }
    else if (i % 5 === 0) {
        yukop += 'Buzz, ';
    }
    else {
        yukop += i + ', ';
    }
}

document.write(yukop.substring(0, yukop.length - 2));
