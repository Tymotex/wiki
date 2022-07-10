function* fooGenerator(): IterableIterator<number> {
	yield 42;
	yield 24;
}

const fooNums = fooGenerator();
console.log(fooNums.next());  // → 42
console.log(fooNums.next());  // → 24
console.log(fooNums.next());  // → undefined

// Looping through a generator's value using for-of.
for (const item of fooGenerator()) {
    console.log(item);
}

