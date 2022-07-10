
const a: unknown = 30;

if (typeof a === 'number') {
    const b: number = a + 1;  // Now that we are certain `a` is a number, we can use it as one.
} else {
    const b: number = a + 1;  // Error.
}
