

"""
------- FUNCTION -------
insert_object()

------- GOAL -------
The pieces of code must add a new object to a certain database, based on the object instance of a class related to it

------- PROCEDURE -------
The demonstration is made with an input, but the main code lies at the hash comment
"""


def algorithm_create_object():
    from utils import command_
    from model import User
    input_text = 'Digite um nome a ser adicionado ao banco de dados (ex: Joao): '
    this_input = input(input_text)
    print(f'Objeto {this_input} foi adicionado ao banco')

    # MAIN
    new_user = User(name_=this_input)
    User.insert_object(exec_=command_, object_=new_user)


if __name__ == '__main__':
    algorithm_create_object()
