

"""
The piece of code will change an object with column of value specified in "target_value" by the value at "new_value"

If the value in "target_value" does not exist:
    nothing changes

Else:
    "new_value" will rewrite "target_value"
"""

if __name__ == '__main__':
    from utils import command_
    from model import User

    User.from_table_edit_object_by_name(exec_=command_,
                                        target_value='Antonio',
                                        new_value='Alberto')
