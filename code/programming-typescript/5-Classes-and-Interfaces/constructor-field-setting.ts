class Person {
	constructor(public name: string) {}
}

// ... is equivalent to:
// class Person {
// 	public name: string;

// 	constructor(name: string) {
// 		this.name = name;
// 	}
// }

const person: Person = new Person('Linus Torvalds');
console.log(person.name);
