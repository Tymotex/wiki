type TwoOrFour = 2 | 4;                         // The set consisting of 2 and 4.
type Value = string | number;                   // The set of all strings and all numbers.
type RandomMess = "Hello" | 0 | null | RegExp;  // The set consisting of "Hello", 0, null and all instances of `RegExp`.

const a: TwoOrFour = 3;        // Error.
const b: RandomMess = "World"; // Error.
const c: RandomMess = /regex/; // This is fine since it's an instance of RegExp.
