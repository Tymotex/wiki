type Person = {
	greet: () => void;
} | null;

function foo(person: Person): void {
	person.greet();
}

const person = null;
foo(person);
