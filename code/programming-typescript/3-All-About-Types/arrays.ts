// You can use T[] or Array<T> to represent an array of items of type T. They're the same.
const items1: number[] = [1, 2];
const items2: Array<number> = [3, 4];

// When arrays are not homogenous, that is, of one type, you'd have to do some type checking to work with its items.
const arr: (string | number)[] = [42, 'Hello'];

arr.forEach((item) => {
	if (typeof item === 'number') {
		// You can use `item` as a number after you've type-checked it.
		const num = item * 3;
		console.log('Number: ', num);
	} else {
		// `item` must be a string
		const s = item + ' world';
		console.log('String: ', s);
	}
});
