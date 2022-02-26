from abc import abstractmethod
from dao import *
from models import Config, Usuario
from hashlib import sha256


def calcula_hash(texto):
    return sha256(texto.encode()).hexdigest()


class ConfigController():

    def cria_engine():
        try:
            return ConfigDao.criaEngine()
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def cria_session(engine):
        try:
            return ConfigDao.criaSession(engine)
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def cria_tabela(engine):
        try:
            return ConfigDao.criaTabela(engine)
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


class UsuarioController():

    def cadastrar_usuario(self, nome, email, senha, session):
        try:
            hash_senha = calcula_hash(senha)
            usuario = Usuario(nome=nome, email=email, senha=hash_senha)
            UsuarioDao.salvar(usuario, session)
            return 1
        except:
            return 2

    def alterar_usuario(self, id, nome, email, senha, session):
        try:
            hash_senha = senha
            if len(senha) > 0:
                hash_senha = calcula_hash(senha)
            usuario = Usuario(id=id, nome=nome, email=email, senha=hash_senha)
            UsuarioDao.alterar(usuario, session)
            return 1
        except:
            return 2

    def remover_usuario(self, id, session):
        try:
            x = session.query(Usuario).filter(Usuario.id == id).one()
            UsuarioDao.remover(x[0], session)
            return 1
        except:
            return 2

    @staticmethod
    def listar_usuarios(session):
        return UsuarioDao.listar(session)

    def existe_usuario(self, id, session):
        return len(session.query(Usuario).filter(Usuario.id == id).all()) > 0
