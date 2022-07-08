TypeScript is a programming language made by Microsoft that is *superset* of [[JavaScript]]. The reason that TypeScript exists is to make complex JavaScript projects more maintainable and less error-prone by introducing a [[Type System#Static Typing|static]] and [[Type System#Strong Typing|strong]] type system. Essentially, it just gives developers a lot of quality-of-life improvements over JavaScript.

TypeScript gets compiled (or more precisely, '*transpiled*') to JavaScript in the end. This is not new, languages like CoffeeScript, Dart, Scala, etc. can all have JavaScript as what we call a *compilation target*.

**Why TypeScript is [loved](https://survey.stackoverflow.co/2022/#most-loved-dreaded-and-wanted-language-love-dread)**
- Your IDE/editor gets more information about your code and give you very helpful intellisense and code-completion that is not possible with JavaScript. This reason alone, in my experience, pretty much negates any loss in developer velocity from using TypeScript over JavaScript.
- Many errors will surface *as you're developing* rather than after your code is deployed to production and angry customers complain to you.
- Types serve as a very useful form of documentation for how your functions are to be used and fields an object should contain. You can have a lot more confidence in refactoring a function when you have confidence about what the input types are.
- Complex objects are much *less unpleasant* to work with. You'll know what its *shape* is (basically what properties it has and what its nested objects look like), what properties are compulsory or optional and you'll actually know when you've mispelt a property name.
- You'll *almost* never have `cannot read property '...' of undefined` again with *non-nullable types*.

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

## Typing

- **Type inference**: you don't have to always supply an explicit type. Often, there'll be enough context for TypeScript to figure it out without ambiguity. In general, we prefer type inference over explict types for conciseness.
	```typescript
	const a: number = 1;	
	const b = 2
	```
- 






