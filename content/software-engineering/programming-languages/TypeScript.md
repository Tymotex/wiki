---
title: TypeScript
description: TypeScript is a programming language made by Microsoft that is superset of JavaScript.
---
TypeScript is a programming language made by Microsoft that is *superset* of [[JavaScript]]. The reason that TypeScript exists is to make complex JavaScript projects more maintainable and less error-prone by introducing a [[Type System#Static Typing|static]] and [[Type System#Strong Typing|strong]] type system. Essentially, it just gives developers a lot of quality-of-life improvements over JavaScript.

TypeScript gets compiled (or more precisely, '*transpiled*') to JavaScript in the end. This is not new, languages like CoffeeScript, Dart, Scala, etc. can all have JavaScript as what we call a *compilation target*.

**Why TypeScript is [loved](https://survey.stackoverflow.co/2022/#most-loved-dreaded-and-wanted-language-love-dread)**
- Your IDE/editor gets more information about your code and give you very helpful intellisense and code-completion that is not possible with JavaScript. This reason alone, in my experience, pretty much negates any loss in developer velocity from using TypeScript over JavaScript.
- Many errors will surface *as you're developing* rather than after your code is deployed to production and angry customers complain to you.
- Types serve as a very useful form of documentation for how your functions are to be used and fields an object should contain. You can have a lot more confidence in refactoring a function when you have confidence about what the input types are.
- Complex objects are much *less unpleasant* to work with. You'll know what its *shape* is (basically what properties it has and what its nested objects look like), what properties are compulsory or optional and you'll actually know when you've mispelt a property name.
- You'll *almost* never have `cannot read property '...' of undefined` again.

The only main reasons *not* to use TypeScript are because:
- You're stuck with a legacy JavaScript codebase.
- You or your teammates are not willing to learn it, and you need to produce output fast in the short-term (like in a hackathon).
- The project is a very simple or one-off thing that it's not worth setting up the build system.

## Setup
Install Node.js, `npm` or `yarn`. Then, install `tsc`, the open-source typescript compiler, as a dev dependency in a javascript project:
```bash
yarn init   # Inside the project root directory, if it's a new project.
yarn add --dev typescript @types/node ts-node
```
### tsconfig.json
Every typescript project should have a `tsconfig.json` file at the root of the project directory. It tells `tsc` which files to compile, where to dump the resulting javascript, and so on. A basic config looks like this (but there are so many [more options](https://www.typescriptlang.org/tsconfig)):
```json
{
	"compilerOptions": {
		"lib": [   // Which APIs are available to the transpiled JS code? Eg. es2015 has Function.prototype.bind, etc.
			"es2015"
		],
		"module": "commonjs", // Which module system should be used by the transpiled JS code?
		"outDir": "dist",     // Where should the output JS files go?
		"sourceMap": true,    // Whether to generate a source map.
		"strict": true,       // All code must be properly typed.
		"target": "es2015"    // What JS version to compile to.
	},
	"include": [   // Directories containing .ts files we want to transpile.
		"src"
	]
}
```
Alternatively, you can generate a `tsconfig.json` with `tsc --init`.

Some recommended flags include:
- `noImplicitThis`, which forces a type to be explicitly assinged to `this` inside functions. See [[TypeScript#this]].

## Typing
Broadly speaking, in programming languages, a *type* is a [[Set Theory#Sets|set]] of values, plus the properties/methods available to them.

### Assigning Types
Assigning types is straightforward in TypeScript, you just postfix a variable or parameter with a colon and a type. 
```typescript
// Typing variables.
let a: number = 42;
let b: string;
```

### Defining Types
Remember, types are just [[Set Theory#Sets|sets]] of values. When you define a *type*, you are just defining a set of values. The following are all examples of custom types you can define:
```typescript
type TwoOrFour = 2 | 4;                           // The set consisting of 2 and 4.
type Value = string | number;                     // The set of all strings and all numbers.
type RandomThings = "Hello" | 42 | null | RegExp; // The set consisting of "Hello", 42, null and all instances of `RegExp`.
```

#### Type Alias
You can declare *type aliases* in a very similar way as to how you define variables. Type aliases are block-scoped, just like local variables.
```typescript
type Person = { age: number, name: string };

// Typescript will never infer that `me` is of type `Person` unless you explicitly say.
const me: Person = {
	age: 21,
	name: "Tim"
};
```

#### Union and Intersection
Again, types are just *sets* of values. To expand the size of a set, you can union it with other sets, and to narrow the size of a set, you can intersect it other sets. In TypeScript, we use `|` to union two types and `&` to intersect two types.
```typescript
type Student = { id: string; degree: string };
type Tutor = { id: string; courses: string[] };

type StudentOrTutor = Student | Tutor;    // Set of all objects that are either `Student`, `Tutor`, or both.
type StudentAndTutor = Student & Tutor;   // Set of all objects containing all fields of `Student` AND `Tutor`.

const student: Student = { id: '111', degree: 'Bachelor of Science' };
const tutor: Tutor = { id: '222', courses: ['CS101'] };
const studentTutor: StudentAndTutor = {
	id: '333',
	degree: 'Bachelor of Computer Science',
	courses: ['CS201'],
};

// For `Student | Tutor`: you can assign any of: `Student`, `Tutor`, or `Student & Tutor`
const uniGoers: StudentOrTutor[] = [student, tutor, studentTutor];

// For `Student & Tutor`: you can only have people who are simultaneously `Student` and `Tutor`.
const studentTutors: StudentAndTutor[] = [studentTutor];
```
- To make a type nullable, you can union it with `null` like this: `type MiddleName = string | null;`

### TypeScript Built-In Types
TypeScript introduces some new built-in data types that aren't present in JavaScript. These are: `any`, `unknown`, `void`, [`never`](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-never-type).
#### any
The `any` type represents the set of *all* values. You can assign a variable of type `any` to a number, a string, a WebServer object, etc. Only use `any` as a last resort – always prefer assigning the most specific type that you can. Often, people treat `any` as a way to 'opt' out of TypeScript for a small part of the code. When something is `any`, you are free to do erroneous things on it such as invoking methods on it that don't exist, using in arithmetic expressions, accessing undefined properties, etc.

#### unknown
The `unknown` type represents the set of *all* values, just like `any`. The difference is that TypeScript does not allow you to use an `unknown` value until you perform [[TypeScript#Type checking|type checks]] to narrow down what specific type the `unknown` value is. For this reason, `unknown` is considered the type-safe version of `any`.
```typescript
const a: unknown = 30;
if (typeof a === 'number') {
	const b: number = a + 1; // Now that we are certain `a` is a number, we can use it as one.
} else {
	const b: number = a + 1; // Error.
}
```
```typescript
const a: any = "Hello";
const b: unknown = "World";

a.toLowerCase();   // This is fine since `a` is `any`.
b.toLowerCase();   // Error. We need a type check before 
```
> A useful way to think about `any` and `unknown` is: `any` means "I don't care", `unknown` means "I don't know (yet)". 

### Object Shape
An important part of using TypeScript effectively is in defining the *shape* of object values, or in other words, what properties they have and which ones must be assigned a value or are optional.
```typescript
// Let typescript infer the object shape.
// `person` will be of type: { age: number, name: string }.
const person = {
	age: 42,
	name: "Andrew"
};

// You can also explicitly specify the object type. You might do this if you want to set narrower types for the properties.
const person: { age: number, name: "Andrew" } = {
	age: 42,
	name: "Andrew"
};

// Or more cleanly, define a type:
type Andrew = { age: number, name: "Andrew" };
const person: Andrew = {...};
```
**Note**: the built-in `object` type is the set of all objects, whether it's `{}`, `{hello: "world"}`, `[]`, `new Date()`, etc. It's only slightly more restrictive than `any`.

#### Optional Properties
By default, all properties are treated as compulsory. To allow an object to not define a property, just postfix the property name with `?`.
```typescript
type Person = {  
	firstName: string;
	lastName: string;	
	middleName?: string;   // Objects of type `Person` can optionally set the `middleName` property.
};
```

#### Immutable Properties
You can make properties immutable by prefixing the property name with the `readonly` property. It's like as if you declared a property as `const`, so once it's assigned for the first time, it cannot be reassigned.
```typescript
type Person = {
	name: string;
	readonly dateOfBirth: string;
};

const me: Person = { name: 'Tim', dateOfBirth: '09/03/2001' };
me.name = 'Andrew';             // This is fine.
me.dateOfBirth = '01/01/1970';  // Error.
```

#### Index Signatures
When you want the flexibility for an object to contain more arbitrary properties with a certain key-value pair type, you can use the index signature syntax, `[key: K]: V`, where `key` can be any name you choose.
```typescript
type FruitRatings = {
	[fruitName: string]: number;
};

const myFruitRatings: FruitRatings = {
	apple: 6,
	banana: 7,
	cherry: 9
};
```

### Arrays
To denote a type as an array of items of type `T`, you can do `T[]` or `Array<T>` (they're [exactly the same](https://stackoverflow.com/questions/36842158/arraytype-vs-type-in-typescript)). 
```typescript
// Array type declaration examples.
type Names = string[];
type People = { name: string; }[];
type Values = (string | number)[];
```
In general, try to keep arrays *homogenous*, that is, of a singular type, otherwise you'd have to do type-checking before TypeScript can let you use the items of the array.
```typescript
// When arrays are not homogenous, that is, of one type, you'd have to do some type checking to work with its items.
const arr: (string | number)[] = [42, "Hello"];

arr.forEach(item => {
	if (typeof item === 'number') {
		// You can use `item` as a number after you've type-checked it.
		const num = item * 3;
		console.log('Number: ', num);
	} else {
		// `item` must be a string
		const s = item + " world";
		console.log('String: ', s);
	}
})
```

Arrays are always mutable by default in TypeScript, that is, you can reassign the value at any index and invoke methods that make in-place modifications like `push` or `reverse`. To make them immutable, you would prefix them with the `readonly` modifier.
```typescript
type Names = readonly string[];
const radioheadMembers: Names = ['Thom', 'Johnny', 'Colin', 'Phil', 'Ed'];

radioheadMembers[1] = 'Tim';  // Error.
```

### Tuples
Remember, tuples are just *fixed-length arrays*. In typescript, we define a tuple by specifying the type of each item like: `[T1, T2, ...]`:
```typescript
type FullName = [string, string, string?];  // You can make items optional in a tuple, just like for objects.
                                            // Note: this is basically the same as: `[string, string] | [string, string, string]`.
const elon: FullName = ["Elon", "Reeve", "Musk"];
const jeff: FullName = ["Jeff", "Bezos"];
```
You can also make use of the [[JavaScript#Rest Operator|rest operator]], `...`, to allow for tuples of arbitrary lengths.
```typescript
type FullName = [string, string, ...string[]];
const queenElizabethII = ['Elizabeth', 'Alexandra', 'Mary', 'Windsor'];
```

**Caveat**: *tuples are not immutable by default*.
Unlike in other languages like Python, the items of a tuple in TypeScript *can* be mutated, that is, reassigned after definition. To make tuples immutable, you would do the same thing as you would for making arrays immutable: prefix it with the `readonly` modifier.
```typescript
type Coordinate = readonly [number, number];
const point: Coordinate = [1, 2];

point[0] = 3;   // Error.
```

### Enums
Enums are data types that have a *fixed set* of constant values. They're a great way to group together a lot of related constants. *Note*: JavaScript doesn't have enums.
```typescript
enum Theme {
	Light,
	Dark,
	HighContrastLight,
	HighContrastDark
};

// You access the fields of the enum in the same way that you'd access an object.
const theme: Theme = Theme.Dark;
```
In the example above, every enum value gets implicitly assigned a counter value starting from 0. It's equivalent to doing the following:
```typescript
enum Theme {
	Light = 0,
	Dark = 1,
	HighContrastLight = 2,
	HighContrastDark = 3
}
```
You can also map enum keys to string values instead of integers. 
```typescript
enum Theme {
	Light = '#CCCCCC',
	Dark = '#333333',
	HighContrastLight = '#FFFFFF',
	HighContrastDark = '#000000',
}
```

#### Caveats
One annoying issue is that you can freely assign numbers to enum types that are clearly outside the bounds of the enum values.
```typescript
enum Theme {
	Light,
	Dark,
	HighContrastLight,
	HighContrastDark,
}
const theme: Theme = 6; // No complaints from TypeScript.
```
In general, the official docs advise you to avoid enums unless they help significantly with readability. Alternatives to enums include string literals, eg. `type Theme = "Light" | "Dark" | ...`, or object literals, eg. `const Theme = { Light: "Light", Dark: "Dark", ... }`

### Type Inference
You don't have to always supply an explicit type. Often, there'll be enough context for TypeScript to figure it out without ambiguity. In general, we prefer type inference over explict assigning types to varaibles/parameters/etc. for conciseness.
```typescript
let a: number = 42;   // There is no need to do this. It's clear what type `a` is from the RHS of the assignment.
let b = 42;           // Equivalent to above, but it lets typescript assign the type implicitly.
```
This extends to functions as well, meaning that often you won't have to specify the return value.

#### Type Widening/Narrowing [TODO]
An important implicit rule in TypeScript is that when you let type inference happen for `const` variables, TypeScript will assign it the *narrowest type possible* since it knows that a `const` variable cannot possibly take any other value after its defined.
```typescript
let a = 2;    // `a` is of type `number`.
const b = 2;  // `b` is of type `2`, a specific member of `number`.
```
	
### Type Checking
Although type checking is done for you statically, there are times when you must perform run-time type checks such as when you're fetching external data. In these times, rely on JavaScript's operators: `typeof` and `instanceof`.
1. Use the `instanceof` binary operator to check some value is of a custom type, or a complex built-in type like `RegExp`.
	- Note that `val instanceof T` works by checking if `T` exists anywhere along `val`'s [[JavaScript#Prototypes|prototype chain]]. This is why you get unintuitive results when you use `instanceof` on primitive types. For example, `42 instanceof Number` is `false`, but `new Number(42) instanceof Number` is `true`.
2.  Use the `typeof` unary operator to check some value is some built-in primitive type such as `undefined`, `number`, `string`, `boolean`, etc.

### Type Assertions [TODO]
When you're confident that some value should be a certain type but TypeScript isn't, you can make a type assertion with the `as` keyword.

You can also make type assertions by prefixing an expression with `<T>`, eg. `<Person>person` which is the same as `person as Person`.


## Functions
**Typing Function Delcarations**
To type a function declaration, you just assign types for each parameter it takes in and then specify the return type by postfixing the parameter list with a colon and a type.
```typescript
// Typing function parameters and return values.
// To assign a return type to a function, you postfix the parameter list with a colon and a type.

// Regular functions:
function increment(num: number): number {
	return num + 1;
}

// Arrow functions:
const decrement = (num: number): number => num - 1;
```
**Typing Function Expressions or Arrow Functions**
What if you want to specify the type of a callback rather than a function declaration? You would use the syntax: `(param: Type, ...) => RetType`. Although the syntax is inspired by arrow functions, it is not actually defining a function.
```typescript
type Greeting = (a: string, b: string) => void;

// Note that the parameter names above don't need to match that of the assigned
// callback's parameter names, they're purely for documentation.
const callback: Greeting = (name, message) => {
	console.log(`Hi, I'm ${name}. ${message}`);
}
callback("Linus", "F*** you, Nvidia.");
```

### Optional & Default Parameters
Just like how you can make [[TypeScript#Object Shape|object properties optional]] and [[TypeScript#Tuples|tuple items optional]], you can make function parameters optional by postfixing the parameter name with a `?`. Alternatively, you can set a default value for a parameter by assigning a value directly after the parameter name, which is pretty much the same as making it optional.
```typescript
// Optional parameter.
const greet = (name: string, message?: string) => {
	console.log(`Hi ${name}!`);
	if (message) console.log(message);
}

// Default parameter. Notice that the parameter type can often be inferred from the
// default value that you supply.
// You can also choose to explicitly set the type anyway like: 
//   `message: string = "You rock."`
const greet = (name: string, message = "You rock.") => {
	console.log(`Hi ${name}! ${message}`);
}
```

### Variadic Functions
A **variadic function** is just one that takes in an arbitrary number of arguments. The vast majority of functions take in a fixed list of parameters, we call these 'fixed-arity' functions. Normally in JavaScript, defining a variadic function requires you to make use of the implicit [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) array in the function body. In TypeScript, it's way more intuitive and can be done in a type-safe way with the rest operator, `...`.
```typescript
const max = (...nums: number[]): number => {
	if (!nums || nums.length === 0) return -Infinity;
	return nums.reduce((maxSoFar, currNum) => (maxSoFar > currNum) ? maxSoFar : currNum, -Infinity);
}
```

### this
In JavaScript, `this` is a nightmare for most programmers to work with because its value is different depending on how it is called. In TypeScript, you can minimise surprises around the value of `this` by assigning a type to it as the first function parameter.

To illustrate the problem:
```typescript
type Person = { name: string, greet: () => void };
const person: Person = {
	name: "Linus Torvalds",
	greet: function() {
		console.log(`Hi, I'm ${this.name}`);
	}
}
person.greet(); // This works as expected since `this` is bound to `person`.

const greet = person.greet;
greet();        // This fails since the `this` is lost and is no longer bound to `person`.
```
The 'solution' is to assign a type for `this` so that the developer is warned when `this` takes on the wrong type when they invoke a function that uses it.
```typescript
type Person = { name: string, greet: (this: Person) => void };
const person: Person = {
	name: "Linus Torvalds",
	greet: function(this: Person) {
		console.log(`Hi, I'm ${this.name}`);
	}
}
```

### Generators
See [[Generators|generators]]. In JavaScript, you can create a [[JavaScript#Generators|generator function]] by postfixing `function` with an asterisk, `*`. *Note*: you cannot define arrow functions as generator functions (at least as of 2022's ES standard).
```typescript
function* fooGenerator() {
	yield 42;
	yield 24;
}

const fooNums = fooGenerator();
console.log(fooNums.next());    // → { value: 42, done: false }
console.log(fooNums.next());    // → { value: 24, done: false }
console.log(fooNums.next());    // → { value: undefined, done: false }

// You can loop through a generator's values with JavaScript's for-of loops.
for (const item of fooGenerator()) {
    console.log(item);
}
```
TypeScript automatically infers the return type of the generator to be `IterableIterator<number>`. To assign an explicit type for what gets yielded, do it the same way that you'd specify the return value, but wrap it around with `IterableIterator`.
```typescript
function* fooGenerator(): IterableIterator<number> {
	...
}
```

### Iterators
See [[Iterators|iterators]]. In JavaScript, an *iterable* is an object containing the `Symbol.iterator` property with the value being a function that returns an *iterator* (which can be done by defining Symbol.iterator to be a [[TypeScript#Generators|generator function]], which always returns an iterator). An *iterator* is an object that defines a `next` method which returns an object of shape: `{ value: any, done: boolean }`.

An object can be both an *iterable* and an *iterator* at the same time. When you invoke a generator function, for example, you get an object 
of type `IterableIterator` which is both, meaning it has a `Symbol.iterator` property, whose value is a function that returns an iterator, and the `next` method.
```typescript
const favouriteNums = {
	*[Symbol.iterator]() {
		yield 42;
		yield 2;
		yield 4;
	}
}

for (const item of favouriteNums) {
	console.log(item);
}
```
**Note**: the syntax for defining `Symbol.iterator` as a generator function might seem strange. See this post for clarifications. As for the square brackets around `Symbol.iterator`, it's called the [computed property name syntax](https://stackoverflow.com/questions/32515598/square-brackets-javascript-object-key), introduced in ES6.

### Function Overloading
You can define a function type that actually consists of multiple function signatures. See the [Function Overloads](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads).

## Generic Functions
See [[Generics]]. In TypeScript, you can define generic functions by specifying a comma-separated list of generic type parameters in angle brackets `<>` right before the parameter list of function. You would use generic functions if you wanted a function to be reusable across multiple types without giving up type safety by resorting to `any`.
```typescript
type Filter = <T>(array: T[], predicate: (elem: T) => boolean) => T[];

const filter: Filter = <T>(array: T[], predicate: (elem: T) => boolean) => {
	const arr: T[] = [];
	array.forEach((elem) => {
		if (predicate(elem)) arr.push(elem);
	});
	return arr;
};

// TypeScript can infer that `T` should be `number`.
console.log(filter([1, 2, 3, 4, 5], (num) => num % 2 === 0));

// To explicitly set `T`, use angle brackets after the function name.
console.log(filter<number>([1, 2, 3, 4, 5], (num) => num % 2 === 0));
```
To make regular function declarations generic, you also place the generic type parameters between angle brackets right before the parameter list:
```typescript
function filter<T>(array: T[], predicate: (elem: T) => boolean) => { ... }
```

#### Bind on Reference
In the above example, `T` gets *bound* when the function gets invoked, but you could also bind `T` whenever the type alias gets referenced by placing the generic type parameters *after* the type name instead of before the function parameter list:
```typescript
type Filter<T> = (array: T[], predicate: (elem: T) => boolean) => T[];

// Wherever you use `Filter`, you have to explicitly bind `T` like `Filter<T>`.
const filter: Filter<number> = (array, predicate) => ...;
```


