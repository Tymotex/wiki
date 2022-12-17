---
title: C++
---

![[Knowledge/Engineering/Languages/assets/cpp-wallpaper.png|800]]

C++ is a [[Knowledge/Engineering/Programming/Type System#Static Typing|statically-typed]], low-level programming language that supports [[Knowledge/Engineering/Programming/Object Oriented Programming|object-oriented programming]]. It's frequently used in any software system that requires resource efficiency such as operating systems, game engines, databases, compilers, etc.

C/C++'s high performance is attributed to how closely it's constructs and operations match the hardware.

The **[ISO C++ standard](https://isocpp.org/std/%20the-standard)** defines:
- Core language features — data types, loops, etc.
- Standard library components — `vector`, `map`, `string`, etc.

Also see [[Knowledge/Engineering/Languages/C++ Standard Library|C++ standard library]].

# Basics
## Copy, List and Direct Initialisation
There are a few ways to initialise a variable with a value.
1. **Copy initialisation**: using `=`. It implicitly calls a constructor.
2. **List initialisation**, also called **uniform initialisation**: using `{ }`.
3. **Direct initialisation**: using `( )`. Think of the parentheses as being used to *directly* invoke a specific constructor.

> Prefer uniform initialisation over copy initialisation.

    ```cpp
    int b(1);     // Direct initialisation.
    int a{1};     // List initialisation.
    int c = 1;    // Copy initialisation.
    int d = {1};  // Copy/List initialisation.
    ```
- *List initialisation* does not allow *narrowing*. Try to use list initialisation `{ }` more often.
    ```cpp
    int i = 7.8;  // Gets floored to 7
    int i{7.8};   // Error: narrowing conversion from 'double' to 'int'
    ```
- `explicit` constructors are *not invokable* with copy initialisation.

#### Designated Initialisers
C++20 introduces a new way to initialise the members of a class/struct:
```cpp
struct Human {
  string name;
  int age;
};

int main() {
  Human andrew{ .name = "Andrew", .age = 42 };
  Human linus{ .name{"Linus"} };               // You can also use list initialisation on the members.

  Human ada{ .age = 36, .name = "Ada" };       // Error. You must initialise the fields in the same order as they're declared in the struct/class.
  return 0;
}
```

## Pointers and References
Pointers and references are really the same thing under the hood, however they have different semantics to the programmer. You can consider references as syntactic sugar for pointers whose main purpose is to help you write cleaner code, compared to if you were to use pointers for the same use case.

>  Unlike other languages, in C++, arguments ***are always passed by value [by default](https://www.learncpp.com/cpp-tutorial/passing-arguments-by-value)*** *unless the function signature explicitly says it takes in a pointer or reference*. This means functions will **entirely copy** all the objects you pass in, unless you pass in a pointer/reference.

>  `*` and `&` have different meanings depending on whether they appear in a type declaration (LHS) or whether they appear in an expression that is to be evaluated (RHS).

In a *type* *declaration*:
- `*` defines a **pointer type**. `int* arr;`
- `&` defines a **reference variable**.
    ```cpp
    int i = 1;
    int& ref = i;
    ```

In an *expression*:
- `*` is the unary **dereference** **operator** that dereferences an address to evaluate to the contents at that address.
- `&` is the unary **address-of operator** that evaluates to the address of a variable. `&` always expects an [[Knowledge/Engineering/Languages/C++#L-Values and R-Values|lvalue]].
    ```cpp
    int i = 1;
    &i         // → Eg. 0x7FFEF2BA1884
    &&i        // → Illegal operation. &(0x7FFEF2BA1884) doesn't make sense.
    ```

### Pointers
Pointers are just memory addresses, often to the contents of an object allocated on the heap.
```cpp
int x = 2;
int y = 3;
int* p = &x;
int* q = &y;
p = q;          // p now contains the memory address of y.
```
![illustration of pointers|590](Knowledge/Engineering/Languages/assets/pointers-illustrated.png)

- `nullptr`. C++ requires that `NULL` is a constant that has value `0`. Unlike in C, `NULL` cannot be defined as `(void *)`
    - `nullptr` therefore exists to distinguish between 0 and an *actual null* for pointer types. People would otherwise mistakenly use `NULL` and not realise it is just 0
- **Note**: [Stroustrup prefers](https://stackoverflow.com/questions/6990726/correct-way-of-declaring-pointer-variables-in-c-c/6990753) the pointer declaration style `int* p` in C++ and `int *p` in C.

### References
You can think of a reference variable as an alias for another variable. They don’t occupy any memory themselves, once your program is compiled and running.
```cpp
int x = 2;
int y = 3;
int& r = x;
int& r2 = y;
r = r2;      // Remember, you can think of references as aliases. This assignment is basically just `x = y`
```
![illustration of references|600](Knowledge/Engineering/Languages/assets/references-illustrated.png)

- References are useful as function parameters to avoid copying the entire argument. **In C++, pass-by-value is the default**, although *copy elision* can happen which nullifies the performance impact of making a copy of an object.
    ```cpp
    void sort(vector<int>& sequence);    // Will sort the given sequence, in-place.
    ```
- Const references are useful for when you don't want to modify an argument and **just want to read its contents**. It prevents the need to make a copy of that argument for the function's scope. This is really common practice:
    ```cpp
    void getAverage(const vector<int>& sequence);
    ```
- References must be initialised and can’t be reassigned afterwards.
- When you return a reference, you are '*granting the caller access to something that isn't local to the function*'. It is an error to return a reference to a local variable.

## Type Qualifiers: auto, const, constexpr, static
### Auto
When specifying the data type of something as `auto`, C++ automatically infers the type.
- Use `auto` for concision, especially when long generic types are involved.
- It's fine to use [[Knowledge/Engineering/Languages/C++#Variables|copy initialisation]] if you use `auto` since type narrowing won't be a problem. E.g. `auto x = 1`.
- Always assume that `auto`, by itself, will make a copy of the RHS. Use `auto&` if copying is undesirable (such as when copying large vectors).

### Const
The `const` qualifier makes it 'impossible' to assign a new value to a variable after it's initialised. There is 0 negative performance impact of enforcing `const` since it's all done at compile-time. Using const can actually allow the compiler to make optimisations.

> Prefer making things const by default. See [const correctness](https://isocpp.org/wiki/faq/const-correctness) for a pitch on why.

- `const` and `constexpr`— immutable variables. Declaring and initialising a `const` variable will make the compiler guarantee that its value is never modified, ever.
    ```cpp
    const int i = 1;      
    const auto j {2};      // You can put **const** before pretty much any variable declaration
    
    // With **const**, you can assign it a value that is determined during runtime.
    // With **constexpr**, you can only assign it values known at compile-time
    constexpr int x = 8; 
    constexpr int x = cube(2);    // Error, *unless cube is defined as a [**constexpr function**](https://www.ibm.com/docs/es/xl-c-and-cpp-aix/16.1?topic=functions-constexpr-c11)*
    ```

#### Const Pointers
```cpp
const int *p;               // A pointer to an immutable int.
const int * const q = ...;  // An immutable pointer to an immutable int. It must be initialised with a memory address.
int * const r = ...;        // An immutable pointer to an int. It must be initisalised with a memory address.
```
If this is hard to read, see the [[Knowledge/Engineering/Languages/C++#Clockwise Spiral Rule|clockwise-spiral rule]].

#### Const References
Typing a variable as a const reference makes it a read-only alias. It's especially helpful for function parameters.
> Prefer typing function parameters as const references. This gives the caller confidence that what they pass in is not modified in any way.

If you don't want a function to modify a caller's argument, you have these options:
```cpp
void foo1(const std::string& s);   // Preferred approach.
void foo2(const std::string* s);   // A pointer to a const also works.
void foo3(std::string s);          // Since pass-by-value is the default, `s` is an independent copy of what the caller passed in.

// If you want a parameter to be modifiable:
void bar1(std::string& s);         // This might modify the caller's string directly.
void bar1(std::string* s);         // So can this.
```

You can't have 100% certainty that what you pass as a const reference is unchanged. See [this example from isocpp](https://isocpp.org/wiki/faq/const-correctness#return-const-ref-from-const-memfn):

#### Const Methods
Const methods can only read `this` and never mutate anything about it. To specify a const method, the `const` qualifier *must* be placed after the parameter list.
```cpp
class Foo {
public:
    void inspect() const;
};
```

> What about making methods **return const values**, eg. `const Foo bar();`? [It's *mostly* pointless](https://stackoverflow.com/questions/8716330/purpose-of-returning-by-const-value). However, it is *not* pointless if you're returning a pointer or reference to something that is const.

### Constexpr
The `constexpr` type specifier is like `const`, except the RHS value must be able to be determined at compile-time. 
```cpp
const int a = some_val;
constexpr int b = 42;
```

#### Constexpr Functions
Constexpr functions are those than *can* be executed at compile-time, meaning all its state and behaviour is determinable at compile-time.

### Static
#### Static Variables
Inside functions, static variables let you share a value across all calls to that function.
```cpp
void foo() {
    static int a = 42;    // All calls to **foo** will see **a = 42**.
    ...                   // If **a** changes, then all calls to **foo** will see that change too
}
```
> Static function variables are **generally considered bad** because they represent global state and are therefore much more difficult to reason about[\*](https://stackoverflow.com/questions/7026507/why-are-static-variables-considered-evil#:~:text=Static%20variables%20are%20generally%20considered,assumptions%20of%20object%2Doriented%20programming.).

### Clockwise-Spiral Rule
[Clockwise-Spiral Rule](http://c-faq.com/decl/spiral.anderson.html) is a trick for reading variable types.
1. Start at the variable name.
2. Follow an outwards clockwise spiral from that variable name to build up a sentence.

**Example**:
![clockwise-spiral rule example|400](Knowledge/Engineering/Languages/assets/clockwise-spiral.png)
Starting at the name `fp`:
1. `fp` is a pointer.
2. `fp` is a pointer to a function (that takes in an `int` and a `float` pointer).
3. `fp` is a pointer to a function (that takes in an `int` and a `float` pointer) that returns a pointer.
4. `fp` is a pointer to a function (that takes in an `int` and a `float` pointer) that returns a pointer to a char.

More examples:
```cpp
int *myVar;                     // pointer to an int.
int const *myVar;               // pointer to a const int.
int * const myVar = ...;        // const pointer to an int.
int const * const myVar = ...;  // const pointer to a const int.
```

## IO
`<<` — the **'put to'** operator. In `arg1 << arg2`, the `<<` operator takes the second argument and writes it into the first.
```cpp
cout << "Meaning of life: " << 42 << "\n";
```

`>>` — the **'get from'** operator. In `arg1 >> arg2`, the `>>` operator gets a value from `arg1` and assigns it to `arg2`.
```cpp
int a, b;
cin >> a >> b;
```

`std::endl` is a newline that flushes the output buffer, which means it is less performant than `"\n"`.
```cpp
cout << "Hello" << endl;             // Adds a "\n" and flushes the output buffer.
cout << "Hello" << "\n";             // Adds a "\n".
cout << "Hello" << "\n" << flush;    // Adds a "\n" and flushes the output buffer.
```

See [[Knowledge/Engineering/Languages/C++ Standard Library#IO|C++ Standard Library IO]] for more complex IO operations.

## Arrays
The many ways of initialising arrays:
```cpp
int arr[4];                    // [?, ?, ?, ?] – array is full of garbage values, often zeroes.
int arr[4] = {  };             // [0, 0, 0, 0] – all elements set to 0.
int arr[4] = { 1, 2, 3, 4 };   // [1, 2, 3, 4].
int arr[4] = { 1 };            // [1, 0, 0, 0] – the rest of array is zeroed.

int arr[] = { 1, 2, 3, 4 };    // Array size can be omitted if it can be inferred from RHS.
int arr[] { 1, 2, 3, 4 };      // You can use uniform initialisation instead of copy initialisation.
```
The size of the array must be able to be determined at compile-time.

### Pointers vs. Arrays
What's the difference between `int* array` and `int array[]`? They both can be used to access a sequence of data and are mostly interchangeable.

The main difference is in **runtime allocation and resizing**: `int* array` is far more flexible, allowing allocation/deallocation and resizing during runtime, whereas `int array[]` cannot be resized after declaration.

> In general, *prefer using declaring **true array-types** with `[]` over pointers-type arrays with `*`*. It's less error-prone (because you don't have to worry about dynamic allocation and remembering to free allocated memory) and more readable.

## L-Values and R-Values
An **lvalue** is a memory location that identifies an object. **Variables are lvalues**.
> In C: an *lvalue* is an expression that can appear on the LHS ***or*** RHS of an assignment.

An **rvalue** is a value stored at some memory address. Rvalues are different from lvalues in that **they cannot have a value assigned to it**, which means it can’t ever be on the LHS part of an assignment. **Literals are typically rvalues**.
> In C: an *rvalue* is an expression that can only appear on the RHS of an assignment.
```cpp
int i = 10;    // i is an lvalue, 10 is an rvalue.
int j = i * 2  // i * 2 is an rvalue.
2 = i;         // error: expression must be a modifiable lvalue.
```

- Rvalues are important because they **enable move semantics** in C++. There are many instances in C++ code where it’s not necessary to copy a value or object from one place to another. E.g. when passing arguments into a function or when saving the returned value on the caller’s side. Implementing move semantics, where appropriate, is great for performance because it prevents expensive copies.

### L-value and R-value References
An **lvalue reference** uses a single ampersand `&`, eg. `string& s = "..."`
- Const lvalue reference types (eg. `const string& s`) as a function parameter allow the caller to **pass both an l-value or r-value, equivalently**.

An **rvalue reference** uses double ampersand `&&`, eg. `string&& s`. You’d use this to receive rvalues in functions, like literals and temporary objects. Doing this means you can avoid unnecessarily copying a value that is a ‘throwaway’ on the caller’s side.
- You can define a *move constructor* and *move assignment operator* that take in an rvalue reference instead of a const lvalue reference. It’ll behave the same way, but it won’t guarantee the source to be unchanged.

```cpp
// Takes in an l-value reference which forces the caller to pass in variables.
void **GreetLvalue**(string &name) {    
  cout << name << endl;
}

// Takes in an r-value reference which forces the caller to pass in literals 
// or temporary objects.
void **GreetRvalue**(string &&name) {   
  cout << name << endl;             
}

// Const references let the caller pass both lvalues and rvalues alike
void **Greet**(const string &name) {    
  cout << name << endl;             // Note: `const string &` will create a temporary variable behind the
}                                   // scenes and then assign it to `name`. This is why you can pass both
                                    // lvalues and rvalues to a const l-value reference like this.
int main() {
  string myName = "Tim";
  GreetLvalue(myName);     // ✓
  GreetLvalue("Andrew");   // Error: cannot bind **non-const lvalue reference**

  GreetRvalue(myName);     // Error: cannot bind **rvalue reference**
  GreetRvalue("Andrew");   // ✓

  Greet(myName);           // ✓
  Greet("Andrew");         // ✓
}
```

## Modularity
### Separate Compilation
C++ supports *separate compilation*, where code in one file only sees the declarations for the types and functions it uses, not the implementation. This decouples the smaller units comprising a project and minimises compilation time since each unit can be compiled only if they change.

We take advantage of separate compilation by listing out declarations in a header file. Example:
![[Knowledge/Engineering/Languages/assets/vector-header-cpp.png|500]]
```cpp
// Vector.h — the header file defining the Vector class and its properties and methods (but without implementation)
class Vector {
    public:
        Vector(int size);
        double& operator[[]];
        int size();
    private:
        double* elements;
        int capacity;
};
```

```cpp
// Vector.cpp — the implementation for Vector.h
#include "Vector.h"

// Implementing the constructor and methods outside of the class definition.
Vector::Vector(int s) :elements{new double[s]}, capacity{s} {}   

double& Vector::operator[[]] { return elements[i]; }
int Vector::size() { return capacity; }
```

```cpp
// user.cpp — the user of Vector.h, who has know idea about how it's implemented.
//            It only knows about the declarations inside Vector.h

#include <iostream>
#include "Vector.h"

using namespace std;

int main() { 
    Vector v(10);
    cout << "Vector size: " << v.size() << endl;
}
```
### Namespaces
Namespaces ***define a scope for a set of names***. It's used to organise your project into logical groups and to prevent name collisions when you're using libraries, for example.
```cpp
namespace UNSW {
    class Student {
        public:
            string id;

            Student(string id) {
                this->id = id;
            }
    };
}

int main() {
    UNSW::Student me("z5258971");
    std::cout << me.id << "\n";
}
```

Use `using` to avoid using a fully qualified name every time. 
```cpp
using std::cout;

int main() {
    cout << "Hello world\n";
    return 0;
}
```
            
Any identifier you declare that's *not within* a namespace will be implicitly part of the *global namespace*. Globally scoped identifiers are accessible with `::` without specifying a name.
```cpp
int num = 42;

namespace Foo {
    int num = 24;

    void bar() {
        std::cout << num;     // 24. Picks the closer `Foo::num` over `::num`.
        std::cout << ::num;   // 42.
    }
}
```

## Error Handling
C++ provides the familiar `try` and `catch`  blocks for error handling. Note that when an exception is thrown, the destructor for the object that threw the exception is called, enabling [[Knowledge/Engineering/Languages/C++#RAII|RAII]].
```cpp
try {
        
} catch(out_of_range& err) {

} catch(...) {
    // All exceptions are caught here when you use `...`

    throw;  // Use `throw` on its own to re-throw the exception.
}
```

### Custom Exceptions
Just inherit from `std::exception`, implement the `const char* what() const throw()` method, and a constructor that takes in a `string` error message.
```cpp
class MyException : public std::exception {
public:
  MyException(const string &message) : message_(message) {}
  const char *what() const throw() { return message_.c_str(); }

private:
  string message_;
};
```

### noexcept
Use `noexcept` at the end of a function signature to declare that it will never throw an exception. If it does in fact throw an exception, it will just directly `std::terminate()`.
```cpp
void something_bad() noexcept;
```

Why use it?
- The compiler generates slightly more optimal code since it can assume it doesn't have to support try-catch control flow.
- For documentation for other developers.

## Classes

#### RAII
The technique of acquiring resources in the constructor and then freeing them in the destructor is called *RAII (Resource Acquisition is Initialisation)*. The idea is about coupling the use of a resource to the lifetime of an object so that when it goes out of scope, or when it throws an exception, the resources it held are guaranteed to be released. Always design classes with RAII in mind.
- This works well for mutexes where you can acquire the lock in the constructor and unlock in the destructor.

### Move Constructor [TODO]
Suppose you have a function that returns a large object (e.g. a big matrix). Since you can't return a reference to a local variable, and it is a bad idea to resort to the C-style returning of a pointer to a `new` object that the caller has to memory-manage, the best option is to use a move constructor.

# Quirks
Random C++ details you encounter infrequently but which are still good to know.
- **Structured binding**: you can unpack values in C++ like how you destructure objects in JavaScript.
    
- **Copy elision**: by default, when you pass an object to a function, that object is copied over (pass-by-value). When it doesn't affect program behaviour, the compiler can move the object rather than making a full copy of it. This compiler optimisation can also happen when returning an object, throwing an exception, etc.
    ```cpp
    string foo() {
      string str = "Hello, world!";
      return str;  // copy elision occurs here
    }
    
    int main() {
      string s = foo();
    }
    ```
- **if-statement with initialiser**: in C++17, you can declare variables inside `if` statements and follow it up with a condition: `if (init; condition) { ... }`.
    ```cpp
    vector<int> vec = { 1, 2, 3 };
    
    if (int size = vec.size())
        cout << "Vector size is not 0" << endl;
    if (int size = vec.size(); size > 2)
        cout << "Vector size is > 2" << endl;
    ```
- **`noexcept(false)`**: it's possible to use `noexcept(false)` in function signatures to say that 'this function throws no exceptions (but it actually might, lol)'. Just avoid using it.
- **`noexcept(true)`** and `noexcept` are completely equivalent. 
- **`throw()`**: in older C++, you can put `throw()` at the end of a function signature to say that the function never throws exceptions, for example: `void something_bad() throw()`. It's been deprecated by `noexcept` in C++11, which is preferred over `throw()`, so you'd do: `void something_bad() noexcept` instead.

---
# Old Notes

> TODO: This is a huge mess that I'll slowly clean up...

### Others:
- `new` operator — for instantiating classes and creating arrays.
    The `new` operator denotes a request for memory allocation on the heap. If the request can be granted, then it'll evaluate to the memory address of the newly allocated memory and then the constructor will be called.
    An object allocated for on the heap will need to be explicitly freed with C++'s `delete` keyword.
    ```cpp
    class Human {
        public:
            Human() {
                cout << "Constructor has been called" << endl;
            }
    };
    
    int main() {
    		// **Creating an object** whose memory will be allocated on the heap
        Human* me = new Human();
        delete me;
    
    		// Creating an array whose memory will be allocated on the heap
    		int* A = new int[3];
    		delete A;
    
    		int B[3];             // This array will have its memory allocated on the stack, so no **delete** operation is necessary
    		
    }
    ```
    - Being allocated on the heap means that it is independent of the scope that it was created in and that it'll persist until it is explictly destroyed or until the program ends
    - You should [always prefer stack allocations](https://stackoverflow.com/questions/333443/c-object-instantiation) rather than heap allocations
        - This helps avoid memory leaks because when the variable is allocated for in the stack, its *destructor* is automatically called when leaving its scope
    - The user of your class should never have to use `new` and `delete` in their consuming code
    - If you need to allocate a resource like a file handle, socket, etc. it should be wrapped in a class where the constructor acquires the resources, then the destructor frees the resources (guranteeing resource release)
        - This is the basic idea behind [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization) — *resource allocation is initialisation*
    - Avoid using `malloc` like you would in C
- `delete` operator — for deallocating objects and arrays allocated on the heap.

    There's two delete operators, `delete` and `delete[]`.
    - `delete` — for individual objects. It calls the destructor of that single object
    - `delete[]` — for arrays. It calls the destructor on each object
    
    ```cpp
    public:
        string* courses;
        string* zId;
    
        Student() {
            courses = new string[3];
            zId = new string("z5258971");
        }
    
        ~Student() {
            **delete[] courses**;       // Deleting an array
            **delete zId**;             // Deleting an individual string
        }
    };
    ```
- `::` *scope resolution operator* — for unambiguously referencing a name [TODO]


## Functions

- Overloading
    
    For functions with the same name, the appropriate function is called depending on which signature matches the call.
    
    ```cpp
    void print(int);
    void print(string);
    
    void print(int i) {
        cout << i << "\n";
    }
    
    void print(string s) {
        cout << s << "\n";
    }
    
    int main() {
        print(1);
        print("Tim Zhang");
    }
    ```
    
- Default parameter values
    
    ```cpp
    void func(int value = 10) {
    		std::cout << value << endl;
    }
    ```
    
- *Pass-by-value* vs. *pass-by-reference* for function parameters
    
    ```cpp
    void func(vector<int> vec, vector<int>& refVec) {
    		vec[1] = 99;         // Only modifies the copied **vec** and does not affect anything on the caller's side
    		refVec[1] = 42;      // Directly modifies the original vector passed in
    }
    ```
    
    - It's preferred to pass larger values by reference to avoid copying them into the function
        - If a function is only ever expected to read a vector's values, for instance, then it's common to declare it with `const vector<int>&`
- `auto` return type
    
    You can also use `auto` in function return types
    
    ```cpp
    auto add(int a, int b) {
        return a + b;
    }
    ```
    
    - It can be convenient for lambdas and functions that return generic types
- `inline` functions
    
    You can prefix a function or method signature with the inline keyword. This makes it so the compiler places a copy of the code in that function at each point where the function is called at compile time, meaning that the code is basically copied into the calling function.
    
    - Doing this offers a marginal performance improvement because you avoid allocating a new [[Knowledge/Engineering/Operating Systems/Stack Frame|stack frame]] that’s usually associated with making a function call
        - This performance improvement is done at the cost of a marginally bigger executable size
        - [Why not make everything inline?](https://softwareengineering.stackexchange.com/questions/254688/why-dont-compilers-inline-everything)
    - You should mainly consider using inline on functions that are very small but called several times in a program
    
    ```cpp
    **inline** void Func() {
        cout << "Hello world" << endl;
    }
    ```
    

---

- *Hoisting* does not exist in C++ or C

### Functors (Function Objects):

*Functors*, or *function objects*, are instances of a regular class that **implements the function call operator method**, `operator()`, which means that they can called as if they were functions themselves.

- Example
    
    ```cpp
    class **DrinkingLaw** {
    public:
        DrinkingLaw(int requiredAge) : requiredAge(requiredAge) {}
    
        **bool** **operator()(int age)** {         // Implementing this method is what makes this class a functor
            return age >= requiredAge;
        }
    private:
        int requiredAge;
    };
    
    int main() {
        DrinkingLaw canDrink(18);
        cout << "I can drink: " << (canDrink(20) ? "Yup" : "Nope") << endl;
    }
    ```
    

**Functors vs functions/methods:**

- Functors can contain state, since they’re just instances of a class
    - Useful in cases where you want to calculate a running value of some kind
- Functors are way more customisable since you get them by calling the constructor, where you could pass in different arguments to get a functor that behaves differently

### Lambda Functions (Anonymous Functors):

You can think of lambda functions as syntactic sugar for *inline*, *anonymous functors*. 

```cpp
[_] (params) -> RetType    // You can omit the return type if it can be implicitly inferred
{
		// Function body
}
```

- You can use the capture clause (the `[]` of the expression) to access variables from the outer scope
    - `[&foo, bar]` — capture foo by reference and bar by value
    - `[&]` — capture all variables by reference
        - `[&, foo]` — capture all variables by reference apart from `foo`
    - `[=]` — capture all variables by value
        - [=, &foo] — capture all variables by value apart from `foo`

Lambda functions are great for concise, localised customisation of *predicate functions* (which are functions which given inputs, returns true/false). 

A classic use of lambda functions is passing it as the comparator function to `std::sort` to define the the ordering of the sorted collection.

```cpp
std::sort(c.begin(), c.end(), **[[]] {**
    **return a.key < b.key;
}**);
```

## Classes

A class has a set of public or private *members*, which can be variables, functions or subtypes.

```cpp
**class Human** {
**public:**
    int age;
    string name;
		static string scientific_name;
		
		// **Default constructor**
		**Human**() { ... }

    **Human**(int age, string name) { ... }
};

// Static class variables must be initialised outside the class definition:
string Human::scientific_name = "homo sapiens";

int main() {
		// **Allocating the object on the heap**
    Human* me1 = new Human(20, "Tim");
    delete me1;

		// **Allocating the object on the stack** (meaning there's not need to call delete)
		Human me2(20, "Tim");
		Human me3{20, "Tim"};     // An equivalent way of instantiating a class
		Human me4;                // Implicitly calls the default constructor	
}
```

### Instantiating Classes: [TODO]

```cpp
void func() {
    // Allocated on the stack 
    Foo f1;              // Implicitly calls the default constructor Foo()
    Foo f2 = Foo(1);     // Copy initialisation
		Foo f3 = 1;          // TODO:
		Foo f4(1);           // Direct initialisation
		Foo f5{1};           // List initialisation      (Generally preferred, unless **auto** is used)
		Foo f6 = {1};        // TODO:

		Foo f7();            // You'd think this is calling the default constructor, but it's not. See '[most vexing parse](https://en.wikipedia.org/wiki/Most_vexing_parse)'

    // Allocated on the heap (avoid when posssible)
    Foo* f8 = new Foo();
    delete f8;
}
```

**General Guidelines for Choosing the Initialisation Method[*](https://stackoverflow.com/questions/9976927/when-to-use-the-brace-enclosed-initializer):**

- Use `=` if the (single) value you are initialising with is intended to be the *exact value* of the object
    - Prefer using `=` when assigning to `auto` variables
    - Prefer when initialising variables with primitive types (eg. int, bool, float, etc.)
- Use `{ }` if the values you are initialising with are a list of values to be *stored in the object* (like the elements of a vector/array, or real/imaginary part of a complex number)
    - Prefer using { } in the majority of cases because it can be used in every context and is less error-prone than the alternatives
- Use `( )` if the values you are initialising with are *not* values to be stored, but *describe* the intended value/state of the object, use parentheses
    - Essentially, if the intent is to call a particular constructor, then use parentheses `( )`
    - Eg. good example with `vector`
        
        ```cpp
        vector<int> **v(10)**;          // Empty vector of 10 elements
        cout << v.size() << endl;   // Prints **10**
        
        vector<int> **u{1, 2, 3}**;     // Vector with elements 1, 2, 3
        cout << u.size() << endl;   // Prints **3**
        ```
        

[There are MANY reasons to use brace initialization, but you should be aware that **the `initializer_list<>` constructor is preferred to the other constructors**, the exception being the default-constructor. This leads to problems with constructors and templates where the type `T` constructor can be either an initializer list or a plain old ctor.](https://stackoverflow.com/questions/18222926/why-is-list-initialization-using-curly-braces-better-than-the-alternatives)

```cpp
struct Foo {
    Foo() {}
    Foo(std::initializer_list<Foo>) { std::cout << "initializer list" << std::endl; }
    Foo(const Foo&) { std::cout << "copy ctor" << std::endl; }
};

int main() {
    Foo a;
    Foo b(a); // copy ctor
    Foo c{a}; // copy ctor (init. list element) + initializer list!!!
}

```

Assuming you don't encounter such classes there is little reason not to use the intializer list.

- Ways to construct an object
    ```cpp
    Foo f;            // Just calls Foo's default constructor, **Foo()**. In Java/C#, this would be an uninitialised object, but in C++ it has implicitly called the default constructor
    Foo f = Foo(1);    // **Copy initialisation**:   calls Foo(), *then the **copy constructor***
    Foo f = Foo(1);		// Direct initialisation							
    Foo f();           // **Direct initialisation**: calls Foo()
    ^WARNING This doesn't do what you think it does. This is actually interpreted as a function prototype. What you want is just **Foo f;** which just invokes the default constructor 
    ```

                       
                       
### OOP:

- ***Operator overloading*** — lets you define what operators like `++`, `[ ]`, `()`, etc. do when used on an instance of your class.
    
    The compiler converts something like `a != b` to a function call `operator!=(a, b)`
    
    - Example
        
        ```cpp
        class Human {
            public:
                Human(int age, string name) {
                    this->age = age;
                    this->name = name;
                }
        
                // Defines the subscript operator []'s behaviour. Returns a reference to the age property, regardless of the index (which is pretty dumb)
        				// Eg. **me[123]** will evalute to **this->age**
                int& **operator[]**(int i) { return this->age; }
        				
        				// Defines the *prefix* incrementor operator ++'s behaviour. It just increases the age
                void **operator++**() { this->age++; }
        
            private:
                int age;
                string name;
        };
        
        int main() {
            Human me(20, "Tim");
            ++me;
            cout << me[42] << endl;     // Prints 21
        }
        ```
        
- ***Destructors***
    
    A method that's called when the object goes out of scope. It's main purpose is to ensure memory allocated resources on the heap are freed to prevent memory leaks.
    
    - Example
        
        You define a destructor the same way you define a constructor, except you prefix the classname with `~`
        
        ```cpp
        
        ```
        
- **Virtual methods** — a function that has an implementation but which may be redefined later by a class deriving from this one
    - ***Pure virtual method*** — where a function ***must*** be defined by a class deriving from this one
        
        ```cpp
        class Foo {
        public:
        		virtual void Bar() **= 0**;
        }
        ```
        
    - ***Abstract class*** — a class that has at least 1 *pure virtual method*. It cannot be instantiated
        - C++ doesn't have an `abstract` keyword like Java. To make a class abstract, you just define 1 pure virtual method
    - ***Concrete class*** — a class that has no *pure virtual functions* and can be directly instantiated
    - `override` keyword — is an *optional* qualifier that tells programmers that a method is meant to provide a definition for a virtual method from a base class
    - Any class with virtual functions should always provide a virtual *destructor*
- **Inheritance [TODO]**
- Polymorphism [TODO]
    
    I think you can only access polymorphic objects through pointers and references
    

---

### Misc:

- `const` methods
    
    <aside>
    💡 Methods that don't modify object state should be declared `const`. See this [const-correctness article](http://www.gotw.ca/gotw/006.htm)
    
    </aside>
    
    When you add the `const` keyword to a method the `this` pointer will essentially become a pointer to `*const` object*, and you cannot therefore change any member data (unless you use `mutable` for class fields).
    
    Declaring a method with `const` will cause a compiler error to be raised for when that method attempts to change a class variable.
    
    ```cpp
    class Student {
    public:
      ...
      **void myConstFunction() const** {       
        this->name = "Overriden";         // Compiler error!
      }
    
    private:
      string name;
    };
    ```
    
    You can add the `mutable` keyword to allow exceptions for what class variables can be modified by const member functions.
    
    ```cpp
    class Student {
    public:
    	...
      Student(string name) {
        cout << "Constructor" << endl;
        this->name = name;
      }
    
      **void myConstFunction() const** { 
        this->name = "Overriden";       // This is now fine ✓
      }
    
    private:
      **mutable** string name;              // Permit `name` to be mutated by const member functions 
    };
    ```
    
- `const` objects
    
    An object declared with `const` means that mutating its fields is not allowed. You can't set class variables directly and you can't call methods that set class variables either.
    
    ```cpp
    class Student {
    public:
        string name;
    
        Student() {
            this->name = "Andrew";
        }
    
        void setName(string name) {
            this->name = name;
        }
    };
    
    int main() {
        Student s1;
        s1.name = "Taylor";     // ✓
    
        **const Student s2**;        
        s2.name = "Taylor";     // ✘ not fine because this modifies a class variable
        s2.setName("Taylor");   // ✘ not fine because this modifies a class variable
    }
    ```
    
- `final` methods
    
    Postfixing a method signature with the `final` keyword will make it so that it cannot be implemented by a deriving class.
    
    - [Why final exists](https://stackoverflow.com/questions/8824587/what-is-the-purpose-of-the-final-keyword-in-c11-for-functions)
    
    ```cpp
    class **BaseFoo** {
    public:
        virtual void Info() = 0;
    };
    
    class **Foo** : public **BaseFoo** {
    public:
        void Info() override final {}
    };
    
    class **DerivingFoo** : public **Foo** {
    public:
        void Info() override {}            // **Error**: cannot override **final** funtion
    };
    ```
    
- `explicit` methods
    
    You can put explicit in front of constructors or methods to prevent implicit type conversions from other types to your class.
    
    - It’s good practice to make constructors explicit by default, unless an implicit conversion makes sense semantically. [Source](https://stackoverflow.com/questions/3716453/is-it-a-good-practice-to-make-constructor-explicit)
    
    ```cpp
    class MyVector {
    public:
      **MyVector(int num)** {
        size = num;
      }
    
      void Show() {
        cout << "Size: " << size << endl;
      }
    
    private:
      int size;
    };
    
    int main() {
      MyVector v = 2;      // Without an **explicit** constructor, this actually calls **MyVector(2)**. 
    											 // When you define **`explicit MyVector(int num)`**, this call would cause an error.
      v.print();
    }
    ```
    
- Access modifiers — `public`, `private`, `protected`
    
    `public` — members are visible and usable anywhere in the program
    
    `private` — members are visible and usable only within the class itself and to *friend classes*
    
    `protected` — like *private,* but derived classes are also allowed to access the members
    
- ***Member initialiser list** —* for 'properly' initialising class variables in the constructor [TODO]
    
    <aside>
    ⚠️ This is not to be confused with **list initialisation**!
    
    </aside>
    
    ```cpp
    // **Member initialiser list**
    Foo(int num)**: bar(num)** {};
    
    // **Simple assignment**
    Foo(int num) {
    		bar = num;
    }
    ```
    
    There is a significant difference between initialising a class variable with member initialiser list and simple assignment in the constructor body
    
    - Member initialiser list — the constructor for each member will be called and initialised in one operation
    - Simple assignment in the body
        - There is the additional overhead of creation *and* assignment when you do this
        - You can't initialise `const` class variables this way
    
    ---
    
    - Class members are initialised in the **order that they are declared in the class**, not the order they appear in the actual member initialiser list
        - It's good practice to keep the order of class variable declarations and the order they appear in member initialiser lists the same
    
- `friend` — granting full internal access to other classes and functions
    
    A class can declare who their *friends* are in their body. Friends are then able to access everything within that class, including private members.
    
    - You can only declare who’s allowed to access you, not who you can have access to. Eg. in real life, you can’t grant yourself access to someone else’s privates, but you can grant others access to yours 😏
    - You can declare other classes or standalone functions as your friends
    - Example
        
        ```cpp
        class Baby {
        public:
            Baby(const string& name) {}
        private:
            **friend class Mother;**        // Makes it so that methods of **Mother** will be able to see everything in **Baby**
            string name;
        };
        
        class Mother {
        public:
            Mother(const string& babyName) : baby(babyName) {}
        
            void RenameBaby(const string& newName) {
                **baby.name = newName;**    // This is only possible because of `**friend class Mother**`
            }
        private:
            Baby baby;
        };
        
        int main() {
            Mother mum("Andrew");
            mum.RenameBaby("Andy");
        }
        ```
        
    
    **Use cases:**
    
    - When you want to write white-box unit tests, then you can declare the unit test class as a friend. It’s good for unit testing private methods
        - It’s [debatable](https://stackoverflow.com/questions/4171310/what-is-wrong-with-making-a-unit-test-a-friend-of-the-class-it-is-testing/4171331#4171331) whether it’s good practice to test private methods. Testing a public method will indirectly test a private method anyway
- Class prototypes
    
    Class prototypes: just like function prototypes, you can declare all your classes upfront and then use them wherever you want throughout the code:
    
    ```cpp
    // Declare my classes
    class A;
    class B;
    class C;
    
    // Define my classes (any order will do)
    class A { ... };
    class B { ... };
    class C { ... };
    ```
    
    - Remeber, *hoisting* does not exist in C++
- *Deleted* *functions* (`= delete`)
    
    Just like how you can use `= 0` to declare a function to be a pure virtual function, you can use `= delete` to declare a function to be a *delete function*.
    
    A *delete function* is one that has been explicitly disabled. It’s useful for disabling certain operators from being usable on your class, for example. Any attempts to call a deleted function raises a compile-time error.
    
    ```cpp
    class Foo {
    		Bar(const Foo &) **= delete**;
    }
    ```
    

---

- In general, prefer allocating on the stack rather than the heap, unless you need the object to persist after the function terminates
    - When allocating on the heap, you have to explicitly call `delete` on that object to prevent memory leaks. Making the caller responsible for remembering to call `delete` themselves is bad practice
        - Every `new` must have a corresponding `delete`, just like how every `malloc(...)` must have a corresponding `free(...)` in C
        - With stack-allocated objects, the destructor is automatically called when the scope ends
    - Allocating on the heap is less performant than allocating on the stack
        - **The stack is faster** because the access pattern makes it trivial to allocate and deallocate memory from it (a pointer/integer is simply incremented or decremented), while the heap has much more complex bookkeeping involved in an allocation or free[*](https://stackoverflow.com/questions/24057331/is-accessing-data-in-the-heap-faster-than-from-the-stack)
    - Very large objects should still be on the heap to prevent stack overflow (the heap is larger than the stack)
- Note: In Java/C#, you can’t allocate objects on the stack, they’d all be allocated on the heap. You could use a `struct` instead

## Enums

In addition to structs and classes, you can also use enums to declare new data types. Enums are used to represent small sets of integer values in a readable way.

There are two kinds of enums in C++, *plain enums* and *enum classes* (which are preferred over plain enums because of their type safety).

- **Plain Enum:**
Declared with just `enum`. The enum's values can be implicitly converted to integers
    
    ```cpp
    **enum Mood** { happy, sad, nihilistic };
    
    int main() {
    		Mood currMood = Mood::happy;  
    		int val = currMood;           // No error, the **Mood** value is implicitly converted to an integer type
    }
    ```
    
- **Enum Classes:**
When you declare an enum with `enum class`, it is strongly typed such that you won't be able to assign an enum value to an integer variable or to another enum type. It reduces the number of 'surprises' which is why it's preferred
    
    ```cpp
    **enum class Mood** { happy, sad, nihilistic };
    
    int main() {
    		Mood currMood = Mood::happy;  
    		int val = currMood;            // Error, **Mood::happy** is not an **int**
    }
    ```
    

## Modules [TODO]

This looks like a C++20 feature, which isn't really out yet (at least not stably in Nov 2021).



### Using [TODO]
`using` keyword — what are all the uses of it?
- question: are there performance impacts to this?
- Can be used for type aliasing instead of typedef
    - It’s generally more preferred to use `using` over C-style `typedef`. It also supports a little more extra functionality that is not available with `typedef` [Source](https://stackoverflow.com/questions/10747810/what-is-the-difference-between-typedef-and-using-in-c11)
- Can be used to inherit constructors:
    
    ```cpp
    class D : public C {
     public:
      using C::C;  // inherit all constructors from C
      void NewMethod();
    };
    ```
    
- Is using namespace std; bad practice?
    - It's bad because it pollutes your namespace with lots of new identifiers that could collide with whatever identifiers you try to bring in. Your code could be silently calling the wrong function for instance
    - using namespace should never be used in header files because it forces the consumer of the header file to also bring in all those identifiers into their namespaces
    - You can always do `using std::cout` so that you don't have to always type `std::cout`
- [Translation units](https://stackoverflow.com/questions/1106149/what-is-a-translation-unit-in-c) (basically just a c or cpp file *after* it's finished including all of the header files)

### Exception Handling [TODO]
- Exception handling
    - And the built-in exception types that C++ defines in [stdexcept](https://en.cppreference.com/w/cpp/header/stdexcept)

### Asserts [TODO]
- `assert` and `static_assert` (runtime vs compile time assertions)

### Casts [TODO]
- static_cast and const_cast and dynamic_cast and regular C-style casting

### Initializer List [TODO]
- `std::initializer_list<T>` — seems like it allows an object to be initialised using curly brace syntax and has
    
    NOT TO BE CONFUSED WITH ‘Member initialiser lists’ used in constructors to initialise its fields.
    
    Apparently, an instance of std::initializer_list<...> is automatically constructed when:
    
    1. {} is used to construct a new object: `Person person{"Tim", "Zhang"}`
        - Note: I think it’s a bit confusing. From experimentation, this will call the constructor of signature `Person(std::initializer_list<string> l) {...}` if it exists. Else it will look for `Person(string firstName, string lastName) { ... }`.
    2. {} is used on the RHS of an assignment.
        - Note: I think this will look for the = operator (assignment) overload method that takes in an instance of `std::initializer_list` and call that.
    3. {} is bound to auto. Eg.
        
        ```cpp
        for (auto i : { 2, 5, 7 }) {
            cout << i << endl;
        }
        ```
        
    
    Note: `std::initializer_list` is an iterable.
    
    For some reason, you cannot subscript an instance of std::initializer_list like you would a vector or array ([SO discussion](https://stackoverflow.com/questions/17787394/why-doesnt-stdinitializer-list-provide-a-subscript-operator)). It seems that it’s just not a desired enough use case?
    
    [**Notes from cplusplus.com](https://www.cplusplus.com/reference/initializer_list/initializer_list/):**
    
    The compiler automatically converts { ... } to objects of type std::initializer_list. For example: 
    
    ```cpp
    auto il = { 10, 20, 30 };  // the type of il is an initializer_list
    ```
    
    Constructors taking only one argument of this type are a special kind of constructor, called *initializer-list constructor*. Initializer-list constructors take precedence over other constructors when the initializer-list constructor syntax is used:
    
    ```cpp
    struct myclass {
    	  myclass (int,int);
    	  myclass (initializer_list<int>);
    	  /* definitions ... */
    };
    
    myclass foo {10,20};  // calls initializer_list ctor
    myclass bar (10,20);  // calls first constructor
    ```
    
- constructor initialiser list (member initialiser list) — the list of stuff that follows the colon : in a constructor implementation.
    - Call base class constructors here
    - Initialise member variables before the constructor body executes (const members MUST be initialised this way, you can’t set them in the body)

### Extern [TODO]
- `extern` keyword
    - [Good explanation](https://stackoverflow.com/questions/10422034/when-to-use-extern-in-c)
    - `extern int x;` tells the compiler that an object of type `int` called `x` exists *somewhere*. It's not the compilers job to know where it exists, it just needs to know the type and name so it knows how to use it. Once all of the source files have been compiled, the linker will resolve all of the references of `x` to the one definition that it finds in one of the compiled source files. For it to work, the definition of the `x` variable needs to have what's called “external linkage”, which basically means that it needs to be declared outside of a function (at what's usually called “the file scope”) and without the `static` keyword.

### Volatile [TODO]
- `volatile` keyword

### Decltype [TODO]
- `decltype` keyword

### Templates
- Templates
    - They’re quite similar to generics in managed languages like Java or C#, but they’re much more powerful. A template is basically you getting the compiler to write code for you, based on a couple rules.
        - You can kind of think of template functions as things that are created on demand — kind of like a code generator. If there are no calls to it, then it actually doesn’t exist after compilation. You could leave syntax errors inside template functions that aren’t called and the compiler just ignores them entirely (but this is compiler-dependent)!
        - Some companies literally ban the use of templates in their source code. It’s because overusing templates can make the code very unreadable. There’s a delicate tradeoff between having to do manual, repetitive coding and accessing the powerful abstracted-away code-generation magic that templates offer
        - *Metaprogramming* is basically about when a program has knowledge of itself and can manipulate itself.
            - C#’s reflection feature is a form of metaprogramming (where it can examine its own static types)
            - C++ gives us template metaprogramming, where the templates you program are used by the compiler to generate more source code.




    
- Copy elision — the compiler is ‘*allowed*’ to *elide* copies where results are “as if” copies were made. Ie. the compiler can decide to skip the copy/move construction of an object. Return value optimisation (RVO) is one such instance.
    - Note: in English/linguistics, to *elide* means to merge and therefore omit something in language. Eg. dunno == don’t know, kinda == kind of, etc
    - It’s an optimisation technique implemented by most C++ compilers to prevent extraneous copy operations. It is because of copy elision that return-by-value and pass-by-value usually remain quite performant in C++ (assuming the certain criteria to allow for it are met).
    - Calls to the copy or move constructors can be entirely skipped!
- Wtf can curly braces be used for?
    - Defining anonymous scope blocks
        - Yep, wrote notes on this
    - Initialising arrays and vectors, and possibly other objects?
        - Yep. It’s generally preferred. You wrote notes on this
    - Constructor initialiser lists
        
        ```cpp
        Vector::Vector(int s) :elements{new double[s]}, capacity{s} { ...constructor body... }
        
        // ^
        // According to https://stackoverflow.com/questions/36212837/member-initializer-list-notation-curly-braces-vs-parentheses
        // this is pretty much equivalent to:
        Vector::Vector(int s) :elements(new double[s]), capacity(s) { ...constructor body... }
        
        // Google's style guide's section on constructor initialiser lists shows examples with parentheses instead of curly braces 
        // Scott Meyer in 'Effective Modern C++': There’s no consensus that either approach is better than the other, so my advice is to pick one and apply it consistently.
        ```
        
- Delegating constructors
    - You can call other constructors from a constructor in the initialiser list. Doing this however means you can’t use a member initialiser list
    - You cannot call constructors from the body of another constructor ☹️
    - Often, you’d have to resort to defining a SharedInit() method

Constructors and assignments for copy or move semantics:

```cpp
class X {
public:
		X(Sometype);            // 'Ordinary constructor' for creating an object
		X();                    // Default constructor
		X(const X &);           // Copy constructor. Takes in a const l-value reference
		X(X &&);                // Move constructor. Takes in an r-value reference

		X& operator=(const X&); // Copy assignment
		X& operator=(X&&);      // Move assignment
		
		~X();                   
		...
};
```

- Switch-case statements in C++ are a bit different. They’re like this? (They have curly braces around the cases)
    
    ```cpp
    switch (tag) {
        case 1: { 
            // ...
            break;
        }
        case 2: {  
            // ...
            break;
        }
        case 3: {  
            // ...
            break;
        }
    }
    ```
    
- Iterators
    - It’s up to the implementation to define what iteration means. It’s kind of like operator overloading, you could make the ++ operator do literally anything.
        - To support range-based for loops, your class has to implement the `begin()` and `end()` methods and make them return an iterator
        
        ```cpp
        std::vector<int> values = {1, 2, 3};
        
        // Equivalently
        for (std::vector<int>::iterator it = values.begin(); it != values.end(); it++) {
        		cout << *it << endl;
        }
        
        // Syntactic sugar for the above
        for (int value : values) {
        		cout << value << endl;
        }
        ```
        
        - end() isn’t the last element, it’s one beyond the last element, meaning it’s an invalid iterator
        - Should you always use range-based for loops?
            - In general yes, but with exceptions. Eg. you should not use it when you are erasing values, inserting something into the middle of something, etc., basically anytime you need to manipulate the position of the iterator, you’d have to fall back to the ugly for loop.
    - Looping with indexes vs iterators
        - Indexes work for arrays, vectors, etc. but for other data structures like sets, you have no choice but to use iterators .
    - const_iterator is for read-only iteration — making sure you don’t mutate the collection.
    - When mutating a container, you must keep in mind that changing the container has an impact on existing iterators that point at elements in the container.
        
        ```cpp
        // BUGGY CODE, DO NOT USE
        for (auto it = c.begin(); it != c.end(); ++it) {
        	  if (BadValue(*it)) {
        		    c.erase(it);
        	  }
        }
        ```
        
        - Although this seems simple enough, there is a fatal flaw: erasing an element in an associative container invalidates all iterators that point to that element. Thus, in the above `for`loops continuation step, the iterator `it` will be invalid whenever `c.erase(it)` was just invoked, resulting in undefined behaviour. To remedy this issue, we can leverage the post-increment operator like so:
        
        ```cpp
        for (auto it = c.begin(); it != c.end(); ) {
          if (BadValue(*it)) {
            c.erase(it++);
          } else {
            ++it;
          }
        }
        ```
        
        - This time, our loop behaves as expected. While `it` is incremented before calling `erase`, the post-increment operator returns the previous (unincremented) value, which is then passed to `erase`. For `vector`s, `deque`s, and `list`s, we can leverage the fact that `erase` returns an iterator that points at the next value in the container and write:
        
        ```cpp
        for (vector<int>::iterator it = c.begin(); it != c.end(); ) {
        	  if (BadValue(*it)) {
        		    it = c.erase(it);
        	  } else {
        		    ++it;
        	  }
        }
        ```
        
- `#include` tells the preprocessor to copy the contents of the included file and directly paste it into the current file, that’s literally all that happens.
    - `#include <path>`
        - With `<>`, the preprocessor searches for the thing to include in directories defined by the compiler. You would use <> often for including standard library headers
        - On Linux, you can find all the libraries stored on the path `/usr/include/c++/<version_num>`
    - `#include “path”`
        - With `“”`, the preprocessor searches first in the same directory as the file first, and then searches through the same directories that `#include <path>` would search through
- Header guards are used inside header files to ensure that the contents of the file are not copied and pasted more than once to any single file. They have the form:
    
    ```cpp
    #ifndef YOUR_HEADER_NAME_H
    #define YOUR_HEADER_NAME_H
    
    ...
    
    #endif
    ```
    
- The entire purpose of namespaces is to avoid naming conflicts (and as a logical container for classes, further namespaces, etc.)
- About std::swap:
    - Often, `std::swap(T& a, T& b)` is horribly inefficient because it could involve copies or moves three times
- Constexpr methods — declared with the `constexpr` qualifier
    - Constexpr methods are also implicitly `inline` methods
    - Can be used to initialise constants at compile time
- What is external linkage? [https://stackoverflow.com/questions/1358400/what-is-external-linkage-and-internal-linkage#:~:text=External linkage refers to things,units (or object files)](https://stackoverflow.com/questions/1358400/what-is-external-linkage-and-internal-linkage#:~:text=External%20linkage%20refers%20to%20things,units%20(or%20object%20files)).
    - Linkage has to do with how many instances (or copies) of a named object there are in a program. it is usually best for a constant with one name to refer to a single object within the program.
    - When you write a .cc file, the compiler generates a translation unit from it. This is basically the source file, plus all the headers that you #included.
        - Internal linkage refers to everything **only in scope of a translation unit**
        - External linkage refers to things that exist beyond a particular translation unit. Ie. accessible through the whole program, which is the combination of al translation units
- You can do namespace aliases to shorten namespaces. Never do this in header files
    
    ```cpp
    namespace testing = ::my::testing::framework;
    ```
    
- TODO: Copy over the stuff in the cheatsheet that are missing in this set of notes
    - Eg. bitsets, `<algorithm>` functions, etc.
- Still can’t fully understand `const`.
    - I think I’m really confused with combinations of qualifiers: static, const, constexpr in a class definition and outside of it, and whether you can initialise the member/variable when declared or if it must be defined in the .cc file.
    Could list out all possibilities.
- regular array literal vs using std::array
- [https://www.google.com/search?q=references+as+members&oq=references+as+members&aqs=chrome..69i57.4024j0j7&sourceid=chrome&ie=UTF-8](https://www.google.com/search?q=references+as+members&oq=references+as+members&aqs=chrome..69i57.4024j0j7&sourceid=chrome&ie=UTF-8)

## **Templates:**

- Templates vs. generics [TODO]
    
    Templates are massively different from generics like in Java.
    
    In Java, generics are mainly syntactic sugar that help programmers avoid boilerplate casting code.
    
    Some main differences that developers should know:
    
    - Java doesn’t let you pass primitive types like `int` as type parameters... yup. You can’t do this
        
        ```cpp
        ArrayList<int> myList = new ArrayList<int>();
        ```
        

[CppCon talk](https://www.youtube.com/watch?v=LMP_sxOaz6g&ab_channel=CppCon) 

### Function Templates:

Suppose you’re writing multiple overloads for a method, and each overload does essentially the same thing but just takes in different types.

```cpp
void **swap**(int& i, int& j) {
		int tmp = i;
		i = j;
		j = tmp;
}

void **swap**(string& s1, string& s2) {
		string tmp = s1;
		s1 = s2;
		s2 = tmp;
}
...
```

Clearly there’s a lot of duplicated code in each overload, and this approach would not scale well in practice. A solution to this is to use ***function templates*** to define a generalised algorithm and let the compiler generate all the overloads for you on compilation.

- Strictly speaking, a function template is not really a function. It’s a generalisation of an algorithm that is used as a tool by the compiler for generating similar but distinct functions.
    - The act of generating a function from a function template by the compiler is called ***template instantiation***

```cpp
**template <typename T>**      // Start of T's scope
****void swap(T& a, T& b) { 
		T tmp = a;
		a = b;
		b = tmp;
}                          // End of T's scope
```

`T` is a ***type argument***. Its scope is limited to the function body.

- Using `class` instead of `typename`
    
    You can also use the `class` keyword instead of `typename`. The behaviour is exactly the same in template definitions... there’s historical reasons why they’re interchangeable. 
    
    ```cpp
    template <typename T>  is the same as  template <class T>
    ```
    
    They both have *very* different meanings in different contexts though.
    

![Untitled](Knowledge/Engineering/Languages/assets/Untitled.png)

When you invoke `**swap<int>(i, j)**`, the compiler will *instantiate* a function with signature `**void swap<int>(int& a, int& b)**` for you by plugging in the types into the template function you defined. Template instantiation is done on-demand when you compile.

- The compiler is smart enough to avoid instantiating duplicate functions

### Class Templates:

Much like how a function template is a generalisation of an algorithm, a class template is a generalisation of a type, *but it’s not an actual type*.

```cpp
template <typename T>
class MyContainer {
public:
		MyContainer(T n);
}

// In member implementations *done outside of the class*, you must fully qualify with the prefix `MyContainer<T>::`.
// Anything following :: will adopt the class' scope, meaning that specifying <T> becomes optional again. 
template <typename T>
MyContainer<T>::MyContainer(T n) {

}
```

- Note: when in the scope of the class body, you can use `MyContainer` and `MyContainer<T>` interchangeably. Essentially, you can consider `<T>` optional inside the class body. However, when outside the class, you have to fully qualify the name with `MyContainer<T>::`
    - Once you specify `MyContainer<T>::`, you can imagine that you’re basically re-entering the class scope, and then everything you could access within the class become available again.
        
        ![Untitled](Knowledge/Engineering/Languages/assets/Untitled%201.png)
        

 

**Container Class Templates:**

A container is an object that contains other objects. Examples include arrays, linked lists, etc.

The standard C++ library provides various container class templates like:

- `list<T>`
- `vector<T>`
- `set<T>`

TODO: should learn more about move semantics. Specifically copy and move constructors as well as std::move


# C++ Appendix:

All the notes under this section are meant to be topics or details you don’t need to care much about to program effectively with C++ but which are important background information.

### How C++ Compilation Works:

Compilation of C++ programs follow 3 steps:

1. **Preprocessing** 
    
    Preprocessor directives like `#include`, `#define`, `#if`, etc. transforms the code before any compilation happens. At the end of this step, a pure C++ file is produced.
    
2. **Compilation**
    
    The compiler (eg. g++, the GNU C++ compiler) takes in pure C++ source code and produces an object file. This step doesn’t produce anyting that the user can actually run — it just produces the machine language instructions.
    
3. **Linking**
    
    Takes object files and produces a library or executable file that your OS can use.
    
### Curly Braces in C++:

This section exists because I keep seeing curly braces appearing in different contexts and having totally different semantics.

- Defining ***scope blocks***
    
    ```cpp
    //***CODE****
    {
    	  // A smaller scope containing some statements
    }
    //****MORE CODE****
    ```
    
    - Doing this within a function is useful when you want a destructor to be called as soon as possible. Eg. often when dealing with mutexes, you’d want to acquire and release a lock as soon as possible.
- 

### Union:

A `union` is data structure like a `class` or `struct`, except all its members share the same memory address, meaning it can only hold 1 value for one member at a time. The implication is that a union can only hold **one value at a time**, and its total allocated memory is equal to $\texttt{max(sizeof each member)}$.

- It’s mainly used when you really need to conserve memory
- They’re largely useless in C++ and more useful in C

```cpp
union Numeric {
    short  sVal;
    int    iVal;
    double dVal;
};

int main() {
    cout << "Unions" << endl;

    Numeric num = { 42 };
    cout << num.sVal << endl;    // Prints **42**
    cout << num.iVal << endl;    // Prints **42**
    cout << num.dVal << endl;    // Interprets the bits of 42 using floating point representation (IEEE 754)
}
```

### Struct:

- **Structs vs. Classes:** There are very few differences between a `struct` and a `class` in C++.
    
    
    | Struct | Class |
    | --- | --- |
    | Members are public by default | Members are private by default |
    | Are value types | Are reference types |
- **Structs in C vs. C++**
    
    
    | C | C++ |
    | --- | --- |
    | Can only have fields | Can have methods and fields |
    | No class features | Has constructors, inheritance, private/protected/public members, literally everything you expect in a class |
- You should use structs when you need a plain-old-data structure that doesn’t require any class-like features[*](https://stackoverflow.com/questions/54585/when-should-you-use-a-class-vs-a-struct-in-c)

### Structured Binding:

**Structured binding** is syntactic sugar for declaring variables initialised with items/fields of a data structure.

- JavaScript calls this ***destructuring***, Python calls this *unpacking*, C# calls this *deconstructing*
- Unfortunately, you have to specify as many identifiers as there are things to unpack

**Use Cases:**

- Array destructuring
    
    ```cpp
    int arr[3] = { 1, 2, 3 };
    auto [a, b, c] = arr;
    ```
    
- Ranged for-loop
    
    ```cpp
    map<string, int> m;
    m.insert(pair<string, int>("Hello", 42));
    m.insert(pair<string, int>("World", 24));
    
    for (**const auto& [key, val]** : m) {
        cout << "Key: " << key << ", val: " << val << endl;
    }
    ```
    
- Class/struct destructuring
    
    ```cpp
    Foo f(42, 24);
    auto [u, v] = f;
    ```
    
- Tuple destructuring
    
    ```cpp
    tuple<int, bool, double> tup(1, false, 3.14);
    auto [x, y, z] = tup;
    ```
    

Continue at 5.2 in Tour of C++

# C++ Primer:

- Any variable with the following properties will be placed into *static memory*:
    - Declared with `static`
    - Has namespace scope
    
    ![Untitled](Knowledge/Engineering/Languages/assets/Untitled%2010.png)
    
- Variable with *static storage duration* have their address and size known at compile time. They’ll live for as long as the program lifetime.
- There is a `thread_local` keyword in C++. When a variable is declared with `thread_local`, it is brought into existence when the thread starts and deallocated when the thread ends. In that sense, the thread sees it as a *static storage duration* variable.
    
    ```cpp
    thread_local int myInt = ...;
    ```
    

Continue at ‘RAII (The "Resource Acquisition Is Initialization" Idiom)’

# C++ Style

### Style Guide

[Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)

Note: there are many decisions in the Google C++ style guide that many people protest against, for example, the lack of exceptions. It generally has good style rules otherwise.

### Soruce Code Documentation

The advice here is sourced from [Google’s C++ style guide](https://google.github.io/styleguide/cppguide.html).

**File Comments**

File comments are preferred but not always necessary. Function and class documentation, on the other hand, must be present with exceptions only for trivial cases.

- Start with licence boilerplate, then broadly describe what abstractions are introduced by the file.
- Don’t duplicate comments across a class’ `.h` and `.cc` file.

[Example](https://github.com/google/googletest/blob/main/googletest/src/gtest-all.cc)

```cpp
// Copyright 2008, Google Inc.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted
// ... and so on
// 
// Google C++ Testing and Mocking Framework (Google Test)
//
// Sometimes it's desirable to build Google Test by compiling a single file.
// This file serves this purpose.
```

**Variable comments**

Generally not required if the name is sufficiently descriptive. Often for class variables, more context is needed to explain the purpose of the variable.

```cpp
private:
	 // Used to bounds-check table accesses. -1 means
	 // that we don't yet know how many entries the table has.
	 int num_total_entries_;
```

**TODO comments**

```cpp
// TODO(kl@gmail.com): Use a "*" here for concatenation operator.
// TODO(Zeke) change this to use relations.
// TODO(bug 12345): remove the "Last visitors" feature.
```

**Function comments**

Always write a comment to explain what the function/method accomplishes unless it is trivial. This includes private functions.

- Start with a verb. Eg. “Opens a file...” or “Returns an iterator for...”
- Which arguments can be `nullptr` and what that would mean.
- Performance implications of how the function is used.

```cpp
// Returns an iterator for this table, positioned at the first entry
// lexically greater than or equal to `start_word`. If there is no
// such entry, returns a null pointer. The client must not use the
// iterator after the underlying GargantuanTable has been destroyed.
//
// This method is equivalent to:
//    std::unique_ptr<Iterator> iter = table->NewIterator();
//    iter->Seek(start_word);
//    return iter;
std::unique_ptr<Iterator> GetIterator(absl::string_view start_word) const;
```

**Class comments**

Always write a comment to explain what the class’ purpose is and when to correctly use it. Always do this in the `.h` file, leaving comments about implementation detail to the implementing `.cc` file.

- Good place to provide a code snippet illustrating a simple use case.
- About documenting the `.h` header file vs. documenting the `.cc` source file
    - Document how to use the function in the header file, or more accurately close to the declaration
    - Document how the function works (if it's not obvious from the code) in the source file, or more accurately, close to the definition
    
    [Source](https://softwareengineering.stackexchange.com/questions/84071/is-it-better-to-document-functions-in-the-header-file-or-the-source-file).
    

```cpp
// Iterates over the contents of a GargantuanTable.
// 
// Example:
//    std::unique_ptr<GargantuanTableIterator> iter = table->NewIterator();
//    for (iter->Seek("foo"); !iter->done(); iter->Next()) {
//        process(iter->key(), iter->value());
//    }
class GargantuanTableIterator {
	  ...
};
```

# Abseil:

Basically Google’s standard library

[https://abseil.io/](https://abseil.io/)

[[Knowledge/Engineering/Languages/C++ Cheatsheet]]

# Flashcards
- What is separate compilation?
    - A division of a larger project into smaller units that interact with each other through header files. One unit only knows about another unit through their header files. The big benefit of structuring projects this way is to allow for compilation to be done independently on these units, meaning that if one unit changes while others have not, then only that one unit is to be compiled.
- What are the differences between copy, list and direct initialisation?
    - They're the 3 ways initialisation of a new variable is done in C++. Copy initialisation is done with `=`, list initialisation is done with `{}`, and direct initialisation is done with `()`. Copy initialisation invokes the . Direct initialisation is directly invoking the constructor, hence the use of `()`.
- What is the difference between `const` and `constexpr`?
- What happens when an identifier is declared outside of a namespace?
    - That identifier becomes globally scoped, i.e. part of the global namespace. It can be referenced directly or with `::` to explicitly say it's from the global namespace.
- Explain RAII and what problem it aims to solve.
    - *Resource allocation is initialisation* means that any resources (things like file handles, database handles, etc.) required by a class should be acquired in the constructor and then released in the destructor. Think of it as "scope-bound resource management". The point here is that when a class throws an exception or goes out of scope, the destructor is called, guaranteeing no resources to be held after the object's lifetime.
- What are designated initialisers in C++? How do you use them?
- How do you define a custom exception in C++?
    - Write a new class that inherits from `std::exception` and implement the `const char* what() const throw()` method and implement a constructor that takes in an error message. 
- Explain copy elision.
- What problem does a move constructor solve — when would you use one?

