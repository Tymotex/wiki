---
title: Go
description: Go
---

Go is a [[software-engineering/concepts/programming/Programming Paradigm|statically-typed]] *compiled* language inspired by C in design, but aims to provide memory safety, ease of usage, and the high performance of close-to-metal languages like C++ and Rust, which Go is often compared to. The main observation being that Go makes design decisions that more readily trade speed for ease of usage.

Notably, Go is credited for improving the developer experience in writing [[software-engineering/concepts/programming/Concurrency|concurrent]] code through [[software-engineering/programming-languages/Go#Goroutines|Goroutines]]. It's also credited with very fast compilation/build times, which is one reason why Go is prevalent in [[software-engineering/DevOps|DevOps]].

Go is general-purpose, but it's typically used for building:
- Backend servers in combination with a framework like Gin.
- Complex scripts and CLIs, especially as an [[software-engineering/Site Reliability Engineering|SRE]]. For one-off scripts, [[software-engineering/programming-languages/Python|Python]] is quicker to write, but for long-lived scripts used frequently, Go might be better.
- Data-intensive algorithms.

## Core Things to Know

 `go mod init <module_name>`.


## Goroutines
TODO.
