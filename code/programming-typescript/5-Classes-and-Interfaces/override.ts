class Base {
	// Methods are virtual by default.
	public foo(): void {
		console.log('Foo');
	}
}

class Sub extends Base {
	// Explicitly re-implementing the parent's `foo` method.
	public override foo(): void {
		console.log('Bar');
	}
}

const obj: Base = new Sub();
obj.foo();
