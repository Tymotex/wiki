type Person = { name: string, greet: (this: Person) => void };
const person: Person = {
	name: "Linus Torvalds",
	greet: function(this: Person) {
		console.log(`Hi, I'm ${this.name}`);
	}
}


person.greet();   // This works as expected since `this` is bound to `person`.

const greet = person.greet;
greet();          // This fails since the `this` is lost and is no longer bound to `person`.
