---
title: Regex
---

Regex pattern matching is supported in most modern programming languages, however they each might have their own 'flavour' of regex.

> Use [regex101](https://regex101.com/) to sanity check the correctness of your regex pattern.

| Metacharacter  | Description                                                                             |
| -------------- | --------------------------------------------------------------------------------------- |
| `.`            | Any character.                                                                          |
| `*`            | 0 or more times.                                                                        |
| `?`            | 0 or 1 time.                                                                            |
| `+`            | 1 or more times.                                                                        |
| `[a-zA-Z0-9]`  | Alphanumeric characters, lowercase and uppercase.                                       |
| `[^a-zA-Z0-9]`  | Anything apart from alphanumeric characters.                                       |
| hello\|world   | Matches `hello` or `world`.                                                             |
| hell(o\|w)orld | Matches `helloorld` or `hellworld`. We use parentheses for grouping among other things. |

| Character Class | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `\w`            | Any word, which is basically a shorthand for `[a-zA-Z_0-9]`. |
| `\W`            | Anything *not* a word.                                       |
| `\s`            | Any whitespace character (space, tabs, newlines, etc.)       |
| `\S`            | Anything *not* a whitespace.                                 |
