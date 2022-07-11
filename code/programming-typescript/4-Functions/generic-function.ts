type Filter = <T>(array: T[], predicate: (elem: T) => boolean) => T[];

const filter: Filter = <T>(array: T[], predicate: (elem: T) => boolean) => {
	const arr: T[] = [];
	array.forEach((elem) => {
		if (predicate(elem)) arr.push(elem);
	});
	return arr;
};

// TypeScript can infer that `T` should be `number`.
console.log(filter([1, 2, 3, 4, 5], (num) => num % 2 === 0));

// To explicitly set `T`, use angle brackets after the function name.
console.log(filter<number>([1, 2, 3, 4, 5], (num) => num % 2 === 0));
