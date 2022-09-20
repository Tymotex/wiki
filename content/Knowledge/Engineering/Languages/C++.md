---
title: C++
---

> TODO: This file is a mess. Clean up.

![[Knowledge/Engineering/Languages/assets/cpp-wallpaper.png|800]]

C++ is a [[Knowledge/Engineering/Programming/Type System#Static Typing|statically-typed]], low-level programming language that supports [[Knowledge/Engineering/Programming/Object Oriented Programming|object-oriented programming]]. It's frequently used in any software system that requires resource efficiency such as operating systems, game engines, databases, compilers, etc.

C/C++'s high performance is attributed to how closely it's constructs and operations match the hardware.

The **[ISO C++ standard](https://isocpp.org/std/%20the-standard)** defines:
- Core language features — data types, loops, etc.
- Standard library components — `vector`, `map`, `string`, etc.

Also see [[Knowledge/Engineering/Languages/C++ Standard Library|C++ standard library]].

## Core
### Variable Initialisation
There are many ways to initialise a variable with a value.
1. **Copy initialisation**: using `=`. It implicitly calls a constructor.
2. **List initialisation**, also called **uniform initialisation**: using `{ }`.
3. **Direct initialisation**: using `( )`. Think of the parentheses as being used to *directly* invoke a specific constructor.
    ```cpp
    int b(1);     // Direct initialisation.
    int a{1};     // List initialisation.
    int c = 1;    // Copy initialisation.
    int d = {1};  // Copy/List initialisation.
    ```

> Prefer uniform initialisation over copy initialisation.

#### Details
- *List initialisation* does not allow *narrowing*. Try to use list initialisation `{ }` more often.
    ```cpp
    int i = 7.8;  // Gets floored to 7
    int i{7.8};   // Error: narrowing conversion from 'double' to 'int'
    ```
- `explicit` constructors are *not invokable* with copy initialisation.

### Auto
When specifying the data type of something as `auto`, C++ automatically infers the type.
- Use `auto` for concision, especially when long generic types are involved.
- It's fine to use [[Knowledge/Engineering/Languages/C++#Variables|copy initialisation]] if you use `auto` since type narrowing won't be a problem. E.g. `auto x = 1`.
- Always assume that `auto`, by itself, will make a copy of the RHS. Use `auto&` if copying is undesirable (such as when copying large vectors).

### Const
The `const` qualifier makes it impossible to assign a new value to a variable after it's initialised.


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
> Prefer typing function parameters as const references. This gives the caller confidence that what they pass in is not modified in any way.

#### Constexpr


#### Const Methods

The `const` qualifier *must* be placed after the parameter list.

### Static
- `static` variables. In functions, static variables let you share a value across all calls to that function.
    ```cpp
    void foo() {
    		static int a = 42;    // All calls to **foo** will see **a = 42**.
        ...                   // If **a** changes, then all calls to **foo** will see that change too
    }
    ```
    - Static variables are **generally considered bad** because they represent global state and are therefore much more difficult to reason about[*](https://stackoverflow.com/questions/7026507/why-are-static-variables-considered-evil#:~:text=Static%20variables%20are%20generally%20considered,assumptions%20of%20object%2Doriented%20programming.)
    - The static variables are stored in **the data segment of the memory**. The data segment is a part of the virtual address space of a program
        ![Program memory map|300](Knowledge/Engineering/Languages/assets/program-memory-map.png)

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

## If-Statements
In C++, you can declare variables inside `if` statements and follow it up with a condition: `if (init; condition) { ... }`.
```cpp
vector<int> vec = { 1, 2, 3 };

if (int size = vec.size()) {
    cout << "Vector size is not 0" << endl;
}
if (int size = vec.size(); n > 2) {
    cout << "Vector size is > 2" << endl;
}
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
The size of the array must be able to be determined during compile-time.

## Standard Library
See [[Knowledge/Engineering/Languages/C++ Standard Library|C++ Standard Library]].

---
# Old Notes

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

## Pointers and References

Pointers and references are really the same thing under the hood, however they have different semantics to the programmer. 

You can consider references as syntactic sugar for pointers whose main purpose is to help you write cleaner code (compared to if you were to use pointers for the same use case).

<aside>
ℹ️ Unlike other languages, in C++, arguments ***are always passed by value [by default](https://www.learncpp.com/cpp-tutorial/passing-arguments-by-value)*** *unless the function signature explicitly says it takes in a pointer or reference*. This means functions will **entirely copy** all the objects you pass in, unless you pass in a pointer/reference.

</aside>

**Important Note:**

<aside>
⚠️ `*` and `&` have different meanings depending on whether they appear in a type declaration (LHS) or whether they appear in an expression that is to be evaluated (RHS).

</aside>

In a *type* *declaration*:

- `*` defines a pointer type
    
    ```cpp
    int* arr;
    ```
    
- `&` defines a ***reference variable***
    
    ```cpp
    int i = 1;
    int& ref = i;
    ```
    

In an *expression*:

- **Dereference operator:** `*` is a unary operator that dereferences an address to get the contents at that address
    - Consider `*p`.
    Read this as “the **variable** stored at the address stored in `p`”
- **Address-of operator:** `&` is a unary operator that gets the address of a variable.
    - `&` expects an *lvalue.*
        
        ```cpp
        int i = 1;
        &i    // → Eg. 0x7FFEF2BA1884
        &&i   // → Illegal operation. &(0x7FFEF2BA1884) doesn't make sense.
        ```
        

### Pointers

Pointers are just memory addresses, often to the contents of an object allocated on the heap.

- Pointer arithmetic [TODO]
    
    Using ++ on a pointer will advance it to the next element
    
- `const` pointers
    
    `const` pointers are variables that can hold 1 memory address and then can never be changed again.
    
    ---
    
    The following is *not* a const pointer. It is a pointer to something that *is const*.
    
    ```cpp
    const int value = 42;
    const int anotherValue = 24;  // A pointer to an int constant. 
    
    const int *p = &value;        
    p = &anotherValue;            // You can assign myVar to an **address to any other const int**, 
    
    *p = 10;                      // but you cannot change the value you point to.
    ```
    
    ---
    
    The following *is a const* pointer.
    
    ```cpp
    int value = 42;
    int anotherValue = 24;
    
    int* const p = &value;       // p cannot be reassigned to any other memory address 
    p = &anotherValue            // Fails
    
    *p = 10;                     // This is fine because p points to an int, not a constant int
    ```
    
    If you have trouble understanding when a pointer is const or not, see the *clockwise spiral rule*.
    
- `nullptr`
    
    C++ requires that `NULL` is a constant that has value `0`. Unlike in C, `NULL` cannot be defined as `(void *)`
    
    - `nullptr` therefore exists to distinguish between 0 and an *actual null* for pointer types. People would otherwise mistakenly use `NULL` and not realise it is just 0
- Pointers vs. references (illustrated)
    
    **Pointers:**
    
    ```cpp
    int x = 2;
    int y = 3;
    int* p = &x;
    int* q = &y;
    p = q;          // p now contains the memory address to y
    ```
    
    ![Untitled](Knowledge/Engineering/Languages/assets/Untitled%204.png)
    
    **References:**
    
    ```cpp
    int x = 2;
    int y = 3;
    int& r = x;
    int& r2 = y;
    r = r2;            // Remember, you can think of references as aliases. This assignment is basically just `x = y`
    ```
    
    ![Untitled](Knowledge/Engineering/Languages/assets/Untitled%205.png)
    
- Arrays of elements vs. pointers [TODO]
    
    Remember, arrays are basically just pointers to the first element.
    
    ```cpp
    int myarray [20];
    int *mypointer;
    
    mypointer = myarray;     // This is valid
    myarray = mypointer;     // This is **invalid**. The main difference between arrays and pointers is that
                             // variables declared as arrays can't be assigned to anything whereas pointers can   
    ```
    

---

- [Stroustrup prefers](https://stackoverflow.com/questions/6990726/correct-way-of-declaring-pointer-variables-in-c-c/6990753) the pointer declaration style `int* p` in C++ and `int *p` in C

### References

You can think of a reference variable as an alias for another variable. They don’t occupy any memory themselves, once your program is compiled and running.

- References are useful as function parameters to avoid copying the entire argument
    
    ```cpp
    void sort(vector<int>& sequence);    // Inplace sort
    ```
    
- Const references are useful for when you don't want to modify an argument and **just want to read its contents**. It prevents the need to make a copy of that argument for the function's scope. This is really common practice:
    
    ```cpp
    void getAverage(const vector<int>& sequence);
    ```
    
- References must be initialised and can’t be reassigned afterwards

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
    
    - Doing this offers a marginal performance improvement because you avoid allocating a new stack frame that’s usually associated with making a function call
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
        
    - **RAII** — the technique of acquiring resources in the constructor and then freeing them in the destructor is called *RAII (Resource Acquisition is Initialisation)*. The idea is about coupling the use of a resource to the lifetime of an object
        - This also works well for mutexes where you can acquire the lock in the constructor and unlock in the destructor
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
    

## Namespaces

Namespaces ***define a scope for a set of names***. It's used to organise your project into logical groups and to prevent name collisions when you're using libraries, for example.

```cpp
**namespace UNSW** {
    **class Student** {
        public:
            string id;

            Student(string id) {
                this->id = id;
            }
    };
}

int main() {
    **UNSW::Student** me("z5258971");
    std::cout << me.id << "\n";
}
```

- To access a name in another namespace, use the *scope resolution operator* `::`
    - If specifying the namespace an identifier comes from is tedious, you can use `using` to bring in a specific identifier
        - Example
            
            ```cpp
            using std::cout;
            
            int main() {
                cout << "Hello world\n";
            }
            ```
            
- Any identifier you bring in that's not within a namespace will be in the *global namespace*

## Exception Handling [TODO]

- `try`-`catch`
    
    ```cpp
    try {
    		
    } catch(out_of_range& err) {
    
    } catch(...) {
    
    }
    ```
    
    - The last try block with condition `(...)` catches all exceptions that weren't matched by previous `catch` conditions
- `throw` [TODO]
- `noexcept` functions [TODO]
    
    Turns `throw` statements into `std::terminate()`
    

## Modules [TODO]

This looks like a C++20 feature, which isn't really out yet (at least not stably in Nov 2021).

# C++ Standard Libraries:

This section contains notes about some of the most useful things in the `std` namespace.

[C++ Standard Library headers](https://en.cppreference.com/w/cpp/header)

## Strings [TODO]

- String formatting with `**std::stringstream**` from `<sstream>`
    
    ```cpp
    std::stringstream fmt;
    fmt << "hello " << 10;
    std::string formatted_str << fmt.str();
    ```
    

str.find_first_of

std::string::npos

std::string_view vs std::string

- You can do `constexpr std::string_view s = "…"`, but not `constexpr std::string s = "…"`

## CType [TODO]

isspace

## I/O Stream

In computer science, a stream is an abstraction that represents a sequence of data that arrives over time (much like a conveyor belt delivering items). In C++, this stream abstraction is how we work with reading/writing characters coming from an input stream (eg. user input on the terminal or a file in read mode) or being written to an output stream (eg. the terminal or a file in write mode).

![Untitled](Knowledge/Engineering/Languages/assets/Untitled%206.png)

### **`ostream`**

An `ostream` serialises typed values as bytes and dumps them somewhere. 

- The ‘put to’ operator `<<` is used on objects of type `ostream`.
- `std::cout` and `std::err` are both objects of type `ostream`.

![Untitled](Knowledge/Engineering/Languages/assets/Untitled%207.png)

---

- You can chain the put-to operator `<<` because the result of an expression like `cout << “Hello”` is itself an `ostream`.
    
    ```cpp
    cout << "Hello, " << "world.\n";
    ```
    
- You can overload the << operator for your own classes. Example
    
    ```cpp
    class Person {
    public:
        Person(std::string name, int age) : name_(name), age_(age) {
        }
    
        std::string Serialise() const {
            return "(name: " + name_ + ")";
        }
    
    private:
        std::string name_;
        int age_;
    };
    
    ostream& operator<<(ostream& os, const Person& person) {
        os << person.Serialise();
        return os;
    }
    
    int main() {
        Person person("Andrew", 42);
        std::cout << person << std::endl;
        return 0;
    }
    ```
    

### `iomanip` [TODO]

### `istream`

An `istream` takes in bytes and converts it to typed values.

- The ‘get from’ operator `>>` is used as an input operator
- `std::cin` is the standard input stream

![Untitled](Knowledge/Engineering/Languages/assets/Untitled%208.png)

---

- **Formatted extraction:**
The type of the RHS of the ‘get from’ operator determines what input is accepted
    
    ```cpp
    int i;
    cin >> i;    // Expects an integer value to be supplied
    
    double j;
    cin >> j;    // Expects a floating point value to be supplied
    ```
    
    - You can chain the get-from operator `>>` just like for put-to `<<`.
        
        ```cpp
        cin >> i >> j;   // Expects an integer, and then a double
        ```
        
    - The user input can be space-separated, new-line-separated or tab-separated integers. There can be any number of ' ', '\n', '\t' characters between the integers
    - If what the user types in cannot be casted to the expected type, nothing happens. The program continues execution and the variable ends up being uninitialised
- **Unformatted line extraction with** `**std::getline**`
When you want to read an entire line up to and not including the newline character, you should use `getline` rather than directly read from `cin` (which always considers space characters ' ', '\n', '\t' to be terminating)
    
    ```cpp
    string msg;
    std::cin >> msg;
    
    // If the user types: **hello world**, then msg will only be "**hello**".
    // If you want to capture the entire line instead, use ***getline***
    std::**getline**(cin, msg);
    ```
    
- Common pitfall: when you do formatted execution followed by unformatted extraction, you’ll skip over the unformatted extraction. 
This is fixed with `std::cin.ignore()`
    
    [Source](https://stackoverflow.com/questions/21567291/why-does-stdgetline-skip-input-after-a-formatted-extraction)
    
    Suppose you have:
    
    ```cpp
    std::cin >> age;                     // You type: 10
    std::getline(std::cin, name);        // You type: Andrew
    ```
    
    You are actually typing “10\n” for the first input prompt. The “\n” unfortunately remains in the buffer when we get to the next `getline` call, which terminates immediately upon seeing the newline, thereby skipping input extract.
    
    To solve this, you need to call `std::cin.ignore()` to skip over the newline.
    
    ```
    std::cin >> age;
    std::cin.ignore();
    std::getline(std::cin, name);
    ```
    

## File Manipulation (`fstream`)

The `fstream.h` header defines `ifstream`, which you use to open a file in read mode, `ofstream`, which you use to open a file in write mode, and `fstream` which you can use to create, read and write to files. 

```cpp
// ═════ Opening a file for reading ═════
ifstream test_file("test.txt");
string line;
while (std::getline(test_file, line)) {
    cout << "Read line: " << line << endl;
}
test_file.close();

// ═════ Opening a file for writing (truncating) ═════
ofstream test_file("out.test.txt");
string line;
test_file << "Hello world\n";
test_file.close();

// ═════ Opening a file for writing (appending) ═════
ofstream test_file("out.test.txt", ios::app);
string line;
test_file << "Hello world\n";
test_file.close();
```

<aside>
ℹ️ Note that `ofstream` is a subclass of `ostream` and `ifstream` is a subclass of `istream`, meaning that you get to use `<<` to write and `>>` to read and work with them in the same way that you work with `cout` and `cin`.

</aside>

```cpp
// ifstream member methods:
in.eof();      // Returns true if EOF has been reached.
```

## String Streams (`sstream`)

String streams let you treat instances of `std::string` as stream objects, letting you work with them in the same way that you’d work with `cin`, `cout` of file streams.

```cpp
// You can use `**istringstream**` anywhere you use `**istream**`. You can use this to feed strings to something that expects input.
std::istringstream str_in("42 12 24");
int a, b, c;
str_in >> a >> b >> c;

// Similarly, `**ostringstream**` can substitute for `**ostream**` instances. You can use this to capture output into a string.
std::ostringstream str_out;
str_out << "Hello world";
std::string extracted = str_out.**str**();
```

## Filesystem

C++17 gives us the `std::filesystem` API which finally lets us basically do `ls` on directories and traverse the filesystem, create symbolic links, get file stats, etc.

```cpp
// Loops through all files in the given directory.
for (const std::filesystem::directory_entry& each_file : std::filesystem::directory_iterator("/usr/bin")) {
    cout << each_file.path() << endl;
}
```

## Smart Pointers [TODO]

## Tuple

```cpp
// Construct tuples with `std::make_tuple`   
**std::tuple<string, int>** person("Andrew", 42);

// Access tuple values with `std::get`. Tuples don't work with the subscript operator [] unfortunately. Reason: https://stackoverflow.com/questions/32606464/why-can-we-not-access-elements-of-a-tuple-by-index.
cout << **std::get<0>**(person) << endl;
cout << **std::get<1>**(person) << endl;

// You can also construct tuples with `std::make_tuple`. This is better
// when you want to pass a tuple r-value to a function because `make_tuple`
// can infer types. See: https://stackoverflow.com/questions/34180636/what-is-the-reason-for-stdmake-tuple
std::tuple<string, int> person = **std::make_tuple**("Andrew", 42);
```

## Multithreading

### Thread (`std::thread`)

<aside>
ℹ️ On Linux, you have to compile with the flag `-pthread` to link the POSIX thread library: `g++ -pthread -o term term.c`

</aside>

```cpp
void func() {
		...
}

int main() {
		// When you construct a thread, it starts running the given function in a separate thread immediately.
		std::thread my_worker(func);

		my_worker.join();      // A synchronous statement that blocks the current thread until `my_worker` has terminated.
		return 0;
}
```

- Simple full example
    
    ```cpp
    #include <iostream>
    #include <thread>
    
    using namespace std::literals::chrono_literals;   // Allows you to use time literals like `1s`, `1500ms`, etc.
    
    static bool finished = false;
    
    void DoWork() {
        while (!finished) {
            std::cout << "Working...\n";
            std::this_thread::sleep_for(1000ms);
        }
    }
    
    int main() {
        std::thread worker(DoWork);
    
        std::cin.get();
        std::cout << "Interrupted!\n";
        finished = true;
    
        worker.join();
        std::cout << "Worker thread has finished execution.\n";
        return 0;
    }
    ```
    

### Futures (`std::future`) [TODO]

### Async (`std::async`) [TODO]

### Mutex (`std::mutex`)

`std::mutex` is a very simple lockable object used to synchronise access to a resource shared by parallel threads.

```cpp
lock()
unlock()
```

- Race condition example and how to solve it with mutexes
    
    ```cpp
    #include <iostream>
    #include <thread>
    
    **static int count = 0;**    // This is a shared resource that parallel threads will try to read/write to
    
    void **IncrementCount**() {
        while (count < 100) {
            std::cout << "Thread with ID " << std::this_thread::get_id() 
                      << " sees count as " << count << "\n";
            count++; 
        }
        return;
    }
    
    int main() {
        **std::thread t1(IncrementCount);
        std::thread t2(IncrementCount);**
    
        **t1.join();
        t2.join();**
        return 0;
    }
    ```
    
    The following is the output of running the program. You can see the lines being printed are also jumbled because `cout` is also a ‘resource’ being accessed by both threads. We need to lock access to `count` and `cout`.
    
    ```cpp
    Thread with ID 140123004860160 sees count as 82
    Thread with ID 140123004860160 sees count as 83
    
    Thread with ID 140123013252864 sees count as 85
    Thread with ID Thread with ID 140123004860160 sees count as 14012301325286486 sees count as 
    Thread with ID 140123004860160 sees count as 87
    Thread with ID 140123004860160 sees count as 88
    86Thread with ID 
    Thread with ID 140123013252864 sees count as 90
    Thread with ID 140123013252864 sees count as 91
    ```
    
    **Solution:**
    
    ```cpp
    #include <iostream>
    #include <thread>
    #include <mutex>
    
    static int count = 0;
    **std::mutex count_mutex;**
    
    void IncrementCount() {
        while (count < 100) {
            **count_mutex.lock()**;
            std::cout << "Thread with ID " << std::this_thread::get_id() 
                      << " sees count as " << count << "\n";
            count++; 
            **count_mutex.unlock()**;
        }
        return;
    }
    
    int main() {
        std::thread t1(IncrementCount);
        std::thread t2(IncrementCount);
    
        t1.join();
        t2.join();
        return 0;
    }
    ```
    
    ```cpp
    Thread with ID 140367027558144 sees count as 82
    Thread with ID 140367027558144 sees count as 83
    Thread with ID 140367027558144 sees count as 84
    Thread with ID 140367027558144 sees count as 85
    Thread with ID 140367027558144 sees count as 86
    Thread with ID 140367027558144 sees count as 87
    Thread with ID 140367027558144 sees count as 88
    Thread with ID 140367027558144 sees count as 89
    Thread with ID 140367027558144 sees count as 90
    Thread with ID 140367027558144 sees count as 91
    ```
    

## Regex

Note: using raw string literals, $\texttt{R"(...)"}$, makes writing regex patterns easier because you won’t be confused about backslashes escaping things that you didn’t mean to escape.

```cpp
#include <regex>

**std::regex** pattern(R"()");
**std::smatch** matches;        // A container for storing std::string matches (capture groups). There are also other containers like std::cmatch for storing string literal matches. 
														// These are all instances of std::match_results and can be indexed with the subscript operator [].

// **═════ Functions ═════**
**std::regex_match**(haystack, pattern);            // Returns true if matched.

**std::regex_search**(haystack, matches, pattern);  // Returns true if matched. Populates the std::smatch object with capture group matches that you can extract.
		matches[i]                                  // Accesses the i-th match. Note: matches[1] accesses the first match, matches[2] accesses the second match, and so on.
```

## Chrono [TODO]

# C++ Data Structures & Algorithms:

This is a summary of the highly efficient general-purpose data structures and algorithms provided by the standard library. Refer to this section for interview preparation and learning competitive programming with C++.  

## Vector:

'Vector' is a misleading name. It should be called '[ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html)' or 'DynamicArray'. It is implemented with an array under the hood.

- To resize the underlying array, a larger memory block is allocated and all items in the original array are copied over to the new larger one. This is an $O(n)$ operation
- Vectors consume more memory than arrays, but offers methods for runtime resizing

```cpp
#include <vector>

// ***Initialisation***
vector<int> a = { 1, 2, 3 };    

// ***Main methods***
a.**insert**(posIter, b)           // **O(1)** - Inserts **b** at **posIter**   
a.**insert**(posIter, it1, it2)    //        Inserts elements from **it1** to **it2** at **posIter**

a.**erase**(posIter)               // Deletes item at **posIter**
a.**erase**(startIter, endIter)    // Deletes all elements in range from inclusive **startIter** to exclusive **endIter**

a.**push_back**(b)                 // **O(1)** - Append
a.**pop_back**()                   // **O(1)** - Pop from end

a.**front**()                      // **O(1)** - Peek front
a.**back**()                       // **O(1)** - Peek back

a**[**i**]**                           // **O(1)** - Access item at an index (the same way you would for arrays)
a.**at**(i)                        //        Alternative to []. It throws an exception for out of bounds access

// ***Iterators***
a.**begin**()               // Iterator starting from first element (index 0)
a.**end**()                 // Iterator starting from last element

a.**rbegin**()              // Reversed
a.**rend**()                

a.**cbegin**()              // Read-only iterator
a.**cend**()                

// ***Properties***
a.**size**()
a.**empty**()
a.**max_size**()
a.**capacity**()

```

- Slicing and splicing
    
    ```cpp
    
    // ***Slicing***
    template<typename T>
    vector<T> **slice**(vector<T> vec, int start, int end) {     
    		// Returns a new vector from inclusive start to exclusive end
        auto first = vec.cbegin() + start; 
        auto last = vec.cbegin() + end;
        vector<T> sliced(first, last);
        return sliced;
    }
    
    // ***Splicing***
    vector<int> a = { 1, 2, 3};
    vector<int> b = { 4, 5 };
    a.insert(a.begin() + 1, b.begin(), b.end());     // a is now { 1, **4**, **5**, 2, 3 }
    a.erase(a.begin() + 2, a.begin() + 3);           // a is now { 1, 4, 2, 3 } 
    ```
    

## Set:

### `set`

Stores elements in ***sorted order*** without duplicates. For most use cases, you probably want to use `unordered_set` instead, which has more favourable time complexities.

```cpp
**set<T> s**;

s.**insert**(T elem)      // **O(logn)** - Inserts element
s.**find**(T elem)        // **O(logn)** - Gets an element
                      //           Returns an iterator which points to the value if it was found, otherwise it points to **s.end()** 
s.**size**()              // **O(1)**    - Cardinality
```

- The underlying implementation uses a balanced tree

### `unordered_set`

Same 

```cpp
unordered_set<T> s;

// **CRUD:**
s.insert(T elem)      // O(1) 
s.find(T elem)        // O(1)
s.erase()

// **Properties:**
s.size()              // O(1)
s.empty()
```

- Uses a hash table as the underlying data structure

## Map:

### `map`

```cpp
map<string, int> m;

// ***Main operations***
m.insert(pair)      // Takes in **std::pair<keyT, valT>**
m[key] = val        // More straightforward way to add key-value pairs
m.erase(key)        // Deletes key-value pair by key. Doesn't fail if the key doesn't exist

// ***Iterators***
m.begin()
m.end()
// ... and all the other ones available to classes like **std::vector**

// ***Properties***
m.size()
m.max_size()
m.empty()
```

- Usage example
    
    ```cpp
    // ***Adding key-value pairs***
    map<string, int> frequencies;
    frequencies["Hello"] = 4;
    frequencies["World"] = 3;
    int val = frequencies["World"];
    
    // ***Iterating through key-value pairs***
    for (auto it = frequencies.begin(); it != frequencies.end(); ++it) {
        cout << it->first << " : " << it->second << endl;
    }
    ```
    

---

- There are [multiple ways](https://stackoverflow.com/questions/17172080/insert-vs-emplace-vs-operator-in-c-map) to insert key-value pairs into a map, eg. `insert()`, `[ ]` operator, `emplace()`, etc.

### `unordered_map`

The interface is very similar to `std::map`, however it offers a few more lower-level methods like `bucket_count()`, `load_factor()`, etc.

```cpp

```

## Strings:

The set of methods available to the `std::string` class is similar to the methods available to `std::vector`, plus a few more special string manipulation methods and operator support like `+`, `<<`, `>>`. 

```cpp

// ***Main operations***
s1 + s2              // Concatentation
s1.append(s2)        // Alternative to + operator

// TODO: https://www.cplusplus.com/reference/string/string/compare/
s1.compare(s2)
s1.compare(s2, pos

s.substr(startPos, runLen)   // Returns the substring from inclusive **startPos** onwards for **runLen** characters

//TODO: more string ops https://www.cplusplus.com/reference/string/string/
s.find
s.find_first_of
s.find_first_not_of
s.find_last_of
s.find_last_not_of
>
// ***Others***
s.copy()

char c;
std::isdigit(c)    // Returns true if the string consists of a valid digit.
std::isalnum(c)
std::isspace(c)
```

**Raw Strings:**

There are raw string literals just like in Python where everything inside the string is treated as raw characters, not special characters. This means you won’t have to escape any special characters with backslash and they’ll all lose their meaning. This is especially useful when defining strings containing regex patterns which contain a bunch of backslashes.

The format for defining a raw string literal is: $\texttt{R"(...)"}$. 

```cpp
std::string my_raw_str = R"(my raw string)";   // → "my raw string"
```

### LeetCode Encountered Things: [temporary]

A collection of string operations and functions that I found helpful in LeetCoding.

- You can iterate through strings with the range-based for loop:
    
    ```cpp
    std::string message = "Hello, world";
    for (char& c : message) {
    	  ...
    }
    ```
    
- Functions
    
    ```cpp
    islower(char c)
    isupper(char c)
    ```
    

## Arrays:

```cpp
// ***Initialisation***
int nums[3];
int nums[3] = { 1, 2, 3 };     // [1, 2, 3]
int nums[]  = { 1, 2, 3 };     // [1, 2, 3]
int nums[3] = { 1 };           // [1, 0, 0]
int nums[3] = {  };            // [0, 0, 0]

// TODO: ***Utility functions***
std::fill_n(nums, 3, -1);

```

- To get the size of an array, you’d need to do $\texttt{sizeof(arr) / sizeof(arr[0])}$. It is almost always recommended to use `std::vector` over regular arrays[*](https://stackoverflow.com/questions/2037736/how-to-find-the-size-of-an-int).

### Matrices:

## Priority Queue:

```cpp
#include <**priority_queue**>

```

## Stack & Queue:

### std::stack:

```cpp
#include <**stack**>

stack<int> s;

// ***Main methods***
s.**push**(item);      
s.**top**()          // Reads the top element
s.**pop**()          // Removes the top element. *Doesn't actually return anything*
s.**empty**()
s.**size**()
```

### std::queue:

```cpp
#include <**queue**>

queue<int> q;

// ***Main methods***
q.**push**()   
q.**front**()          // Reads the next element
q.**back**()           // Reads the last element
q.**pop**()            // Removes the top element. Doesn't actually return anything
q.**empty**()
q.**size**()
```

### std::deque:

```cpp
#include <**deque**>

```


### Smart Pointers [TODO]

Smart pointers — wraps a naked pointer. Preferred over naked pointers, mainly because it handles the deletion of objects that would cause a memory leak otherwise.
    - Smart pointers are 'smart' because they enforce ownership semantics.
        - Objects owned by a `unique_ptr` will have `delete` invoked on them when the `unique_ptr` goes out of scope
        - Smart pointers are preferred in C++ just because they offer better memory management
Naked pointers, also called *dumb pointers*, are regular C-style pointers.
        
```cpp
int* p;   // A naked pointer
```

- Use `#include <memory>`
- Makes it so that you never have to call `new` or `delete` in your code
- C++ code should prefer smart pointers (most commonly `std::unique_ptr`) instead of raw pointers when dynamically allocating objects. The `delete` operator is used on the allocated object in `std::unique_ptr`’s destructor
- `std::unique_ptr` — the simplest smart pointer. When it goes out of scope, the object gets deleted. They’re called unique because they cannot be copied — because if you were to have two pointers to the same memory address, then if delete is called on one pointer, then the other pointer would be pointing to invalid memory.
    - If you only have one reference to an object and you want it to be freed once out of scope, then use unique_ptr
    - There’s also stuff like `std::make_unique` that is apparently a [replacement for the new operator when initialiser std::unique_ptr?](https://stackoverflow.com/questions/37514509/advantages-of-using-stdmake-unique-over-new-operator)
        - It is recommended to use the 'make_unique/make_shared' function **to create smart pointers**
- `std::shared_ptr`
    - Unlike `std::unique_ptr`, shared_ptr lets you have multiple references to the same object. You can assign a `std::shared_ptr` to another variable that is type `std::shared_ptr`
    - Uses reference counting. When you assign std::shared_ptr to a variable of type std::shared_ptr, it’ll increment the count
    - You **have to** use `std::make_shared` to instantiate shared_ptr. It is important to do this because shared_ptr needs to manage bookkeeping around the counting of references. If you were to use new, then you’ve created a separate instance that won’t be counted as a reference.
- `std::weak_ptr`
    - When you assign `std::shared_ptr` to a variable of type `std::weak_ptr`, it won’t increment the underlying references count managed by the shared_ptr.
- [Return smart pointers by value](https://www.internalpointers.com/post/move-smart-pointers-and-out-functions-modern-c#:~:text=Return%20smart%20pointers%20from%20functions)

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
    

### Separate Compilation

C++ supports separate compilation to decouple parts of a project and minimise compilation time.

- Example — using header files to separate the users of an interface and the implementation for that interface
    
    ![Untitled](Knowledge/Engineering/Languages/assets/Untitled%209.png)
    
    ```cpp
    // **Vector.h — the header file defining the Vector class and its properties and methods (but without implementation)**
    
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
    // **Vector.cpp — the implementation for Vector.h**
    
    #include "Vector.h"
    
    Vector::Vector(int s) :elements{new double[s]}, capacity{s} {}   // Implementing the constructor outside of the class definition
    
    double& Vector::operator[[]] {
        return elements[i];
    }
    
    int Vector::size() {
        return capacity;
    }
    ```
    
    ```cpp
    // **user.cpp — the user of Vector.h who has know idea about how it's implemented**
    
    #include <iostream>
    #include "Vector.h"
    
    using namespace std;
    
    int main() { 
        Vector v(10);
        cout << "Vector size: " << v.size() << endl;
    }
    ```
    

### L-Values and R-Values:

*Lvalues*, or locator values, are memory locations that identifies an object. Lvalues are typically just variables.

*Rvalues* are values stored at some memory address. They’re different from lvalues in that they cannot have a value assigned to it, which means it can’t even be the LHS part of an assignment.

```cpp
int i = 10;    // i is an lvalue, 10 is an rvalue
2 = i;         // **Error**: **expression must be a modifiable lvalue**
```

- Rvalues are important because they **enable move semantics** in C++.
    - There are many instances in C++ code where it’s not necessary to copy a value or object from one place to another. Eg. when passing arguments into a function or saving the returned value on the caller’s side.
    Implementing move semantics, where appropriate, is great for performance
- **Lvalue references:**
An lvalue reference uses a single ampersand `&`, eg. `string&`
- **Rvalue references:**
An rvalue reference uses double ampersand `&&`, eg. `string&&`.
    
    You’d use it to receive rvalues in functions, like literals and temporary objects. Doing this means you can avoid unnecessarily copying a value that is a ‘throwaway’ on the caller’s side.
    
    - You can define a *move constructor* and *move assignment operator* that take in an rvalue reference instead of the default const l-value reference.
        - It’ll behave the same way, but it won’t guarantee the source to be unchanged

---

**Practical Notes:**

- Const l-value reference types as a function parameter let the caller pass both an l-value or r-value equivalently
- Example showing l-value, r-value and const l-value references
    
    ```cpp
    void **GreetLvalue**(string &name) {    // Takes in an l-value reference which forces the caller to pass in variables.
      cout << name << endl;
    }
    
    void **GreetRvalue**(string &&name) {   // Takes in an r-value reference which forces the caller to pass in literals 
      cout << name << endl;             // or temporary objects.
    }
    
    void **Greet**(const string &name) {    // Const references let the caller pass both lvalues and rvalues alike
      cout << name << endl;             // **Note**: `**const string &**` will create a temporary variable behind the
    }                                   // scenes and then assign it to `name`. This is why you can pass both
    																		// lvalues and rvalues to a **const l-value reference** like this.
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
