/*
** EPITECH PROJECT, 2022
** Stack.hpp
** File description:
** Stack.hpp
*/

#ifndef __Stack_hpp_
#define __Stack_hpp_

#include "../core/pp.hpp"

#include <iostream>
#include <fstream>
#include <sstream>
#include <exception>
#include <functional>
#include <stack>


// class MyException : public std::exception
// {
//     private:
//         std::string _msg;

//     public:
//         MyException(const std::string &msg) noexcept
//             : _msg(msg)
//             {}
//     public:
//         const char *what() const noexcept override { return _msg.data(); }
// };


// g++ -o shared_lib.so *.cpp -Wpedantic -pedantic-errors -Wextra -Wall -W -fPIC -shared // a taper dans le lib dir

class Stack : public IStack {
    private:
        std::stack<double> _stack;

    public:
        class Error : public std::exception
        {
            private:
                std::string _msg;

            public:
                Error(const std::string &msg) noexcept
                    : _msg(msg)
                    {}
            public:
                const char *what() const noexcept override { return _msg.data(); }
        };
        Stack();
        ~Stack();
        void push(double value);
        double pop();
        double top() const;
        void add();
        void sub();
        void mul();
        void div();
};

#endif /* !__Stack_hpp_ */
