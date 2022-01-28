

"""
The pieces of code show the table with its whole content, as dictionaries, so far
"""

if __name__ == '__main__':
    from utils import command_
    from model import User

    User.query_table_global_content(exec_=command_)
