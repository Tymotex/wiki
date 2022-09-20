#include <iostream>

using namespace std;

class Foo {
public:
    explicit Foo(int a) {
        _a = a;
    }
private:
    int _a;
};

int main() {
    // Direct initialisation with ().
    Foo foo(1);
    
    // Copy initialisation with =.
    // If the constructor were not explicit, this would successfully compile.
    Foo bar = 1;   // error: conversion from 'int' to non-scalar type 'Foo' requested.
    return 0;
}
