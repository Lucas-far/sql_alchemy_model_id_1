

"""
The pieces of code executed must create a database passed on parameter "database_name"
"""

from model import User

instance_ = User.create_database_file(database_name='test.db')
command_ = User.create_database_cursor(engine=instance_)
User.create_table(engine=instance_)
