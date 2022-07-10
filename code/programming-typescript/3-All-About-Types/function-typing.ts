let a: number = 42;
let b: string;

// Typing function parameters and return values:
function increment(num: number): number {
	return num + 1;
}
const decrement = (num: number): number => num - 1;

console.log(increment(42));
console.log(decrement(42));
