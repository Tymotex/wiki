---
title: Go
description: Go
---

![[software-engineering/programming-languages/assets/go-wallpaper.png|800]]

Go is a [[software-engineering/concepts/programming/Programming Paradigm|statically-typed]] *compiled* language inspired by [[software-engineering/programming-languages/C|C]] in design, but aims to provide memory safety, ease of usage, and the high performance of close-to-metal languages like [[software-engineering/programming-languages/C++|C++]] and [[software-engineering/programming-languages/Rust|Rust]], which Go is often compared to. The main overarching difference is that Go makes language design decisions that favour ease of usage over speed.

Notably, Go is credited for improving the developer experience in writing [[software-engineering/concepts/programming/Concurrency|concurrent]] code through *Goroutines*. It's also credited with very fast compilation/build times, which is one reason why Go is prevalent in [[software-engineering/DevOps|DevOps]].

Go is general-purpose, but it's typically used for building:
- Backend servers in combination with a framework like [Gin](https://gin-gonic.com/).
- Complex scripts and CLIs, especially as an [[software-engineering/Site Reliability Engineering|SRE]]. For one-off scripts, [[software-engineering/programming-languages/Python|Python]] is quicker to write, but for long-lived scripts used frequently, Go might be better.
- Data-intensive algorithms.

## Packages
All Go programs consist of *packages*, which consist of source files defining a bunch of functions, variables, etc. Program execution starts in the `main` package. 

### Imports
Import statements like `import fmt` creates a binding `fmt` that lets you access the package's functions.
- If you do `import math/rand`, it uses the last name in the path to create the binding, creating the `rand` binding in this case.
- It's preferred to group import statements into parentheses:
	```go
	import (
	    "fmt"
	    "math"
	)
	```

### Exports
A binding is exported if it starts with a capital letter, otherwise, it remains only accessible within its package. It's that simple.


## Variables
Variables are declared with `var` and can be done at the package-level or function-level.
```go
// Package-level variables.
var foo string

func main() {
	var bar int = 42
}
```
Types always come *after* the variable/parameter name, like [[software-engineering/programming-languages/TypeScript|TypeScript]]. **Why?** In short, with C-style type declaration, complex types quickly become unreadable, eg. `int (*foo)(int (*)(int, int), int)`. By specifying the type after the symbol name, you have significantly more readable complex types: `foo func(func(int, int) int, int) int` ([official blog](https://go.dev/blog/declaration-syntax)).

## Functions
Functions declarations look like this in Go. 
```go
func foo(a int) int {   // 
	return a + 42;
}
```


### Multiple Return Values
Unlike most languages, you can return multiple values without needing to wrap it in a data structure.
```go
func foo() (int, int) {
	return 42, 24
}

func main() {
	a, b := foo()    // a → 42, b → 24.
}
```
