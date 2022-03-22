/*
** EPITECH PROJECT, 2022
** pp.hpp
** File description:
** pp.hpp
*/

#ifndef __pp_hpp_
#define __pp_hpp_

// g++ -o core *.cpp -Wpedantic -pedantic-errors -Wextra -Wall -W -ldl // a taper dans le core.

#include <iostream>
#include <fstream>
#include <sstream>
#include <exception>
#include <functional>
#include <thread>
#include <dlfcn.h>
#include <stack>

class IStack {
    public:
        virtual ~IStack() = 0;
        virtual void push(double value) = 0;
        virtual double pop() = 0;
        virtual double top() const = 0;
        virtual void add() = 0;
        virtual void sub() = 0;
        virtual void mul() = 0;
        virtual void div() = 0;
};


class pp
{
    private:
        IStack *_pp;
        std::string _nameLib;

        void *stackHandle;

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
        pp(const std::string &name = "");
        ~pp();
        void openLib();
        int testLib();

        static void   *Dlsym(void *handle, const char *symbol);
        static void   *Dlopen(const char *filename, int flag);
        static int    Dlclose(void *handle);
};



#endif /* !__pp_hpp_ */
