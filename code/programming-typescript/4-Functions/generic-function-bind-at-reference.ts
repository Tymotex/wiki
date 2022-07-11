// Note: depending on where you put <T>, T will be bound when the function gets
// invoked, OR when the type gets referenced.
// Here, T would get bound whenever the `Filter` type is referenced.
type Filter<T> = (array: T[], predicate: (elem: T) => boolean) => T[];

// Anywhere you use `Filter`, you would have to explicitly bind `T` like `Filter<T>`.
const filter: Filter<number> = (array, predicate) => {
	const arr: number[] = [];
	array.forEach((elem) => {
		if (predicate(elem)) arr.push(elem);
	});
	return arr;
};

console.log(filter([1, 2, 3, 4, 5], (num) => num % 2 === 0));
