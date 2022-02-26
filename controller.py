from dao import *
from models import Usuario
from hashlib import sha256


def calcula_hash(texto):
    return sha256(texto.encode()).hexdigest()


class ConfigController():

    def cria_engine():
        try:
            return ConfigDao.criaEngine()
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def cria_tabela(engine):
        try:
            return ConfigDao.criaTabela(engine)
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


class UsuarioController():

    def cadastrar_usuario(self, nome, email, senha, engine):
        try:
            hash_senha = calcula_hash(senha)
            usuario = Usuario(nome=nome, email=email, senha=hash_senha)
            UsuarioDao.salvar(usuario, engine)
            return 1
        except:
            return 2

    def alterar_usuario(self, id, nome, email, senha, engine):
        try:
            hash_senha = senha
            if len(senha) > 0:
                hash_senha = calcula_hash(senha)
            usuario = Usuario(id=id, nome=nome, email=email, senha=hash_senha)
            UsuarioDao.alterar(usuario, engine)
            return 1
        except:
            return 2

    def remover_usuario(self, id, engine):
        try:
            sessao = ConfigDao.criaSession(engine)
            x = sessao.query(Usuario).filter(Usuario.id == id).one()
            UsuarioDao.remover(x, sessao)
            return 1
        except:
            return 2

    @staticmethod
    def listar_usuarios(engine):
        return UsuarioDao.listar(engine)

    def existe_usuario(self, id, engine):
        sessao = ConfigDao.criaSession(engine)
        return len(sessao.query(Usuario).filter(Usuario.id == id).all()) > 0

    @staticmethod
    def logar(engine, email, senha):
        hash_senha = calcula_hash(senha)
        sessao = ConfigDao.criaSession(engine)
        try:
            usuario = sessao.query(Usuario).filter(Usuario.email == email).filter(Usuario.senha == hash_senha).one()
            return 1, usuario.nome
        except:
            return 2, None