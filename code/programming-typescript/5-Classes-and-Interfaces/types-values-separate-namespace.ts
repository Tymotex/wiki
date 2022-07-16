// This is totally fine. TypeScript maintains a separate namespace for values
// and types.
type hello = 'world';
const hello: hello = 'world';

console.log(hello);
