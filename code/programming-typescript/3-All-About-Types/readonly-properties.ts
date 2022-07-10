type Person = {
	name: string;
	readonly dateOfBirth: string;
};

const me: Person = { name: 'Tim', dateOfBirth: '09/03/2001' };
me.name = 'Andrew'; // This is fine.
me.dateOfBirth = '01/01/1970'; // Error.
