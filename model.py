

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):

    # ------------------------------------------- MÉTODOS DE CRIAÇÃO (única) -------------------------------------------
    @staticmethod
    def create_database_file(database_name):
        import sqlalchemy
        engine_ = sqlalchemy.create_engine(f"sqlite:///{database_name}", echo=False)
        return engine_

    @staticmethod
    def create_table(engine):
        Base.metadata.create_all(engine)

    @staticmethod
    def create_database_cursor(engine):
        from sqlalchemy.orm import sessionmaker
        session_bind = sessionmaker(bind=engine)
        session = session_bind()
        return session

    # -------------------- MÉTODOS DE INSERÇÃO (adição de objeto ao banco, na ordem: um p/ vários) --------------------
    @staticmethod
    def insert_object(exec_, object_):
        exec_.add(object_)
        exec_.commit()

    @staticmethod
    def insert_object_many(exec_, users_tuple):
        exec_.add_all(users_tuple)
        exec_.commit()

    # ----------------- MÉTODO DE CONSULTA (consultar todos os objetos da tabela desta classe modelo) -----------------
    @staticmethod
    def query_table_global_content(exec_):
        for content in exec_.query(User).order_by(User.id_):
            print({'id_': content.id_, 'name_': content.name_})

    # ----------------------- MÉTODO DE ARMAZENAMENTO (guardar objetos do banco em uma variável) -----------------------
    @staticmethod
    def store_table_content(exec_):
        box = []
        for content in exec_.query(User).order_by(User.id_):
            box.append({'id_': content.id_, 'name_': content.name_})
        return box

    # -------------------- MÉTODO DE CONSULTA DE SELEÇÃO (cada função é uma consulta de uma coluna) --------------------
    @staticmethod
    def query_from_table_by_pk(exec_, value):

        this_msg_error = 'A chave primária especificada não existe no banco'

        try:
            query_user = exec_.query(User).filter_by(id_=value).first()
            query_user_as_dict = {'id_': query_user.id_, 'name_': query_user.name_}
            # query_user_as_dict = query_user.__dict__
            # del query_user_as_dict['_sa_instance_state']
            return query_user_as_dict
        except AttributeError:
            return this_msg_error

    @staticmethod
    def query_from_table_by_name(exec_, value):

        this_msg_error = 'A chave de nome especificada não existe no banco'

        try:
            query_user = exec_.query(User).filter_by(name_=value).first()
            query_user_as_dict = {'id_': query_user.id_, 'name_': query_user.name_}
            # query_user_as_dict = query_user.__dict__
            # del query_user_as_dict['_sa_instance_state']
            return query_user_as_dict
        except AttributeError:
            return this_msg_error

    # -------------- MÉTODO DE REFATORAÇÃO (identificar e editar dado específico de um objeto da tabela) --------------
    @staticmethod
    def from_table_edit_object_by_name(exec_, target_value, new_value):
        """
        :param exec_        || cursor which executes commands
        :param target_value || the key value which tells how the object will be found
        :param new_value:   || the key value which updates a new value for the object

        ------- NOTE -------
        The target column in the syntax is "name_", because it is easier to find by text, and it only has 2 fields
        """

        # O campo alvo deste método é: name_ (O modelo possui somente dois campos)
        exec_.query(User).filter(User.name_ == target_value).update({'name_': new_value})
        exec_.commit()

    # -------------- MÉTODO DE REFATORAÇÃO (identificar e deletar dado específico de um objeto da tabela) --------------
    @staticmethod
    def from_table_delete_object_by_name(exec_, target_value):
        """
        :param exec_        || cursor which executes commands
        :param target_value || the key value which tells how the object will be found

        ------- NOTE -------
        The target column in the syntax is "name_", because it is easier to find by text, and it only has 2 fields
        """
        exec_.query(User).filter(User.name_ == target_value).delete()
        exec_.commit()

    @staticmethod
    def type_database(exec_):
        return type(exec_.query(User).order_by(User.id_))

    __tablename__ = 'user'

    id_ = Column(Integer, primary_key=True, autoincrement=True)
    name_ = Column(String(70))


if __name__ == '__main__':

    instance_ = User.create_database_file(database_name='a.db')
    command_ = User.create_database_cursor(engine=instance_)
    User.create_table(engine=instance_)

    # Codes related to the functions are found at: [ utils.py ] and [ test_1.py ] until [ test_8.py ]
