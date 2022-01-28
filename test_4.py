

"""
The pieces of code show the table with its whole content, as dictionaries, so far, placed into a variable
"""

if __name__ == '__main__':
    from utils import command_
    from model import User

    database_stored = User.store_table_content(exec_=command_)

    print(type(database_stored))
    print(database_stored)
