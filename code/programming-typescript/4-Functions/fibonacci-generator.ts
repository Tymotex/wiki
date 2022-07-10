function* fibGen() {
    let a = 0;
    let b = 1;
    while (true) {
        yield b;
        [a, b] = [b, a + b]
    }
}

const fibNums = fibGen();
console.log(fibNums.next());
console.log(fibNums.next());
console.log(fibNums.next());
console.log(fibNums.next());
console.log(fibNums.next());
console.log(fibNums.next());
console.log(fibNums.next());
