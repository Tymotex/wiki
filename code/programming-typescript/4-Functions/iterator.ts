const favouriteNums = {
    [Symbol.iterator]: function* () {
        yield 42;
        yield 2;
        yield 4;
    }
}

for (const item of favouriteNums) {
    console.log(item);
}
