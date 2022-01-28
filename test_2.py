

"""
The pieces of code must create a new object to the database "sqlalchemy_test.db"
In the database file, look for the strings specified in "name_" to take the proof
"""


if __name__ == '__main__':
    from utils import command_
    from model import User

    User.insert_object_many(exec_=command_, users_tuple=(User(name_='Bento'),
                                                         User(name_='Carlos')))
