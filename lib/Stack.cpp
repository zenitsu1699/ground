/*
** EPITECH PROJECT, 2022
** Stack.cpp
** File description:
** Stack.cpp
*/

#include "Stack.hpp"

Stack::Stack()
{
}

Stack::~Stack()
{
}

void Stack::push(double value)
{
    this->_stack.push(value);
}

double Stack::pop()
{
    if (!this->_stack.top())
        throw Stack::Error("Empty stack");
    double ss = this->_stack.top();

    this->_stack.pop();
    return ss;
}

double Stack::top() const
{
    if (!this->_stack.top())
        throw Stack::Error("Empty stack");
    return this->_stack.top();
}

void Stack::add()
{
    double a = 0;
    double b = 0;

    if (this->_stack.size() < 2)
        throw Stack::Error("Not enough operands");
    a = this->pop();
    b = this->pop();
    this->_stack.push(a + b);
}

void Stack::div()
{
    double a = 0;
    double b = 0;

    if (this->_stack.size() < 2)
        throw Stack::Error("Not enough operands");
    a = this->pop();
    b = this->pop();
    this->_stack.push(a / b);
}

void Stack::sub()
{
    double a = 0;
    double b = 0;

    if (this->_stack.size() < 2)
        throw Stack::Error("Not enough operands");
    a = this->pop();
    b = this->pop();
    this->_stack.push(a - b);
}

void Stack::mul()
{
    double a = 0;
    double b = 0;

    if (this->_stack.size() < 2)
        throw Stack::Error("Not enough operands");
    a = this->pop();
    b = this->pop();
    this->_stack.push(a * b);
}

extern "C"
{
    Stack *createStack(void)
    {
        return (new Stack());
    }

    void deleteStack(Stack *tmp)
    {
        if (tmp) {
            delete(tmp);
            tmp = NULL; }
    }
}