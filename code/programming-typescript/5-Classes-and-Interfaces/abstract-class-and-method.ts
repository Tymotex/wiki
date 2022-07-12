abstract class Employee {
	constructor(public salary: number) {}
	public getSalary(): number { return this.salary; }
	public abstract slackOff(): void;
}

class SoftwareEngineer extends Employee {
	constructor() { super(100000); }
	public override slackOff() { console.log('Time to browse r/ProgrammerHumor...'); }
}

const linus: Employee = new SoftwareEngineer();
linus.slackOff();
