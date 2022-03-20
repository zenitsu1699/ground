##
## EPITECH PROJECT, 2021
## evalxpr
## File description:
## makefile
##

SRC	=	groundhog.py
NAME =	groundhog

all:
	ln -s $(SRC) $(NAME)
	chmod +x $(NAME)

clean:
	rm -f *~

fclean: clean
	rm -f $(NAME)

re: fclean all
