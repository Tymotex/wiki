---
title: Rust
description: Rust
---
![[software-engineering/programming-languages/assets/rust-wallpaper.png|800]]
> "Rust's greatest ambition is to eliminate the trade-offs that programmers have accepted for decades by providing safety *and* productivity, speed *and* ergonomics." — *The Rust Programming Language*

Rust is a [[software-engineering/concepts/programming/Type System#Static Typing|statically typed]] low-level programming language that supports many [[software-engineering/concepts/programming/Programming Paradigm|programming paradigms]]. It's designed to have comparable performance to C/C++ while offering great developer experience and preventing pitfalls in low-level programming such as memory leaks, security vulnerabilities, etc.

When you install Rust, you also get the following CLIs:
- `rustup` — a Rust version manager.
- `rustc` — the [[software-engineering/concepts/programming/AOT|ahead-of-time]] Rust compiler, similar to `gcc` for C/C++. For bigger projects, you'd use `cargo` to compile and run the project, not `rustc`.
- `cargo` — the dependency manager *and* build tool.
- `rustfmt` — a formatter for enforcing code style.

## Core
Every Rust program must implement one `main` function as the entrypoint to the program.


### Functions
### Macros
You invoke macros the same way as invoking functions, but you append `!` to the macro name.
Eg. `println!("Hello world")` invokes the `println` macro.

### Memory Management
Rust does not use a garbage collector to implement memory safety like in most languages.

### Cargo
Rust projects using Cargo must go by a standard directory structure where all source code is kept in `src`.
```bash
cargo new <project_name>  # Creates a new directory, boilerplate and `Cargo.toml` file.
cargo build               # Compiles the project, dumping to output to a `target` directory.
    --release             #   → builds and optimised executable for production.
cargo run                 # Compiles and runs the project.

cargo check               # Sanity-checking that compilation works. Doesn't produce executables.
``` 

