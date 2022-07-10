type Person = { age: number; name: string };

// By default, you can't assign null to types that don't explitly allow you to
// have null values. This means there's no need to do those if-statement null
// checks.
const person: Person = null;
