/*
** EPITECH PROJECT, 2022
** main.cpp
** File description:
** main
*/

#include "pp.hpp"

pp::pp(const std::string &name)
{
    this->_nameLib = name;
}

pp::~pp()
{
    // _pp ? delete(_pp) : (void)0;
    // this->Dlclose(stackHandle);
}

void *pp::Dlsym(void *handle, const char *symbol)
{
  return (dlsym(handle, symbol));
}

void *pp::Dlopen(const char *filename, int flag)
{
  return (dlopen(filename, flag));
}

int pp::Dlclose(void *handle)
{
  return (dlclose(handle));
}


void pp::openLib()
{
    IStack *(*create_stack)();

    this->stackHandle = this->Dlopen(this->_nameLib.c_str(), RTLD_LOCAL | RTLD_LAZY);
    if (!this->stackHandle)
        throw pp::Error("Error: '" + this->_nameLib + "': Cannot open");
    create_stack = reinterpret_cast<IStack* (*)()>(Dlsym(this->stackHandle, "createStack"));
    if (!create_stack)
        throw pp::Error("Error: '" + this->_nameLib + "': Cannot load library symbol");
    this->_pp = create_stack();
    std::cout << "la creation s'est bien passée . . .\n\n\n";
}

int pp::testLib()
{
    this->_pp->push(42.21);
    this->_pp->push(84.42);
    this->_pp->push(21.12);
    this->_pp->add();
    this->_pp->div();
    try {
        this->_pp->mul();
    }
    catch ( const std :: exception & e ) {
        std :: cout << e . what () << std :: endl ;
    }
    std :: cout << this->_pp->top () << std :: endl ;
    return 0;
}

int main(int ac, char **av)
{
    std::string ss;

    if (ac != 2) return 84;
    ss = av[1];
    pp p(ss);
    p.openLib();
    if (p.testLib()) return 84;
    return 0;
}