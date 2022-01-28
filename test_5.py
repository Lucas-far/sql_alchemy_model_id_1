

"""
The pieces of code show an object which primary key is specified in "value", in a certain database.

In case key does not exist, the return is:
    A chave primária especificada não existe no banco
"""

if __name__ == '__main__':
    from utils import command_
    from model import User

    search_this_user_by_pk = User.query_from_table_by_pk(exec_=command_, value=4)

    print(type(search_this_user_by_pk))
    print(search_this_user_by_pk)
