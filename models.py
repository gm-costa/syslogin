import email
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Config():
    CONEXAO = "mysql+pymysql://aluno:aluno@localhost:3306/db_login"


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    senha = Column(String(64), nullable=False)

    def __repr__(self):
        return f'Usuario(id={self.id}, nome={self.nome}, e-mail={self.email}, senha={self.senha})'
