

"""
------- FUNCTION -------
from_table_delete_object_by_name

------- GOAL -------
The piece of code will delete an object which column has the value specified in "target_value"

------- PROCEDURES -------
If the object does not exist:
    nothing will be deleted
Else:
    the object specified will be dropped out the table database
"""

if __name__ == '__main__':
    from utils import command_
    from model import User

    User.query_table_global_content(exec_=command_)  # before deletion
    print('\n')
    User.from_table_delete_object_by_name(exec_=command_, target_value='Carlos')
    print('\n')
    User.query_table_global_content(exec_=command_)  # after deletion
