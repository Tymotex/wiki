type Assert = <T>(val1: T, val2: T, ...vals: T[]) => boolean;

const is: Assert = <T>(val1: T, val2: T, ...vals: T[]) => {
	if (!vals || vals.length <= 0) return val1 === val2;
	else
		return (
			val1 === val2 &&
			vals.reduce((isEq, currVal) => {
				if (!isEq) return false;
				return isEq && currVal === val1;
			}, true)
		);
};

// Compare a string and a string
console.log(is('string', 'otherstring')); // false
// Compare a boolean and a boolean
console.log(is(true, false)); // false
// Compare a number and a number
console.log(is(42, 42)); // true
// Comparing two different types should give a compile-time error
// is(10, 'foo'); // Error TS2345: Argument of type '"foo"' is not assignable
// to parameter of type 'number'.

console.log(is(1, 1, 1));
console.log(is(1, 2, 1));
console.log(is(1, 2, 2));
console.log(is(2, 2, 2));
