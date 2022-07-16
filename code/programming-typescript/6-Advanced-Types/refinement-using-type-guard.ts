// const isString = (s: unknown): boolean => {
// 	return typeof s === 'string';
// };

const isString = (s: unknown): s is string => {
	return typeof s === 'string';
};

const refinementTest = (val: string | number) => {
	if (isString(val)) {
		val.toLowerCase(); // Error. TypeScript still thinks `val` is `string | number`.
		// ...
	} else {
		const num = val * 2;
		// ...
	}
};
