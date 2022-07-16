// With type aliases, to add additional fields on top another type, you'd use `&`.
// type Employee = { id: string };
// type SoftwareEngineer = Employee & { techStack: string[] };

// With interfaces, you just use `extends`, similar to how you do class inheritance.
interface Employee {
	id: string;
}
interface SoftwareEngineer extends Employee {
	techStack: string[];
}

const linus: SoftwareEngineer = {
	id: '123',
	techStack: ['C'],
};
