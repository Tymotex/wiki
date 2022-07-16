// The built-in utility types are implemented with 'mapped types'.
type MyPartial<T> = {
	[K in keyof T]?: T[K];
};

interface Human {
	limbs: string[];
	organs: string[];
	memories: string[];
	soul: boolean;
}

type Husk = MyPartial<Human>; // The same as `Human`, but all properties are optional.

// After programming in Java, I have no soul or memories.
const me: Husk = {
	limbs: ['arms', 'legs', '...'],
	organs: ['brain', 'heart', '...'],
};
