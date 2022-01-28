

"""
The pieces of code show an object which key is specified in "value", in a certain database.
By the name of the function, the search goes through a search related to "name"

In case key does not exist, the return is:
    A chave de nome especificada não existe no banco
"""

if __name__ == '__main__':
    from utils import command_
    from model import User

    search_by_name = User.query_from_table_by_name(exec_=command_, value='Carlos')

    print(type(search_by_name))
    print(search_by_name)
