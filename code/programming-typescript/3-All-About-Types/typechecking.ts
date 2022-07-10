
const a: unknown = new Number(123);

// This doesn't work because instanceof checks the prototypal chain, and 'Number' does not appear for literal numbers.
if (a instanceof Number) {   
    console.log("instanceof: a is a number");
}

// `typeof` is the way you check against primitive built-in types.
if (typeof a === 'number') {
    console.log("typeof: a is a number");
}