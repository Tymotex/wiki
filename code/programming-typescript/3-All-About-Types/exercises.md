1. 
    a) `number`
    b) `string`
    c) `'pineapples'`
    d) `boolean[]`
    e) `{type: string}`
    f) `(number | boolean)[]`
    g) `[3]`
    h) ~~`null`~~ `any`
2. 
    a) Because `4` is not a member of the type `3`.
    b) Because `j` was inferred to be of type `number[]` which cannot accept `string` items.
    c) Nothing is assignable to type `never` apart from `never` itself.
    d) Anything can be assigned to an `unknown` typed variable, however you must run type-checks (with `typeof`, for example) before being able to use the `unknown` value.


