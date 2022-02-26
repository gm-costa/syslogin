from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class ConfigDao():

    @classmethod
    def criaEngine(cls):
        conn = models.Config.CONEXAO
        return create_engine(conn, echo=False)

    @classmethod
    def criaSession(cls, engine):
        Session = sessionmaker(bind=engine)
        return Session()

    @classmethod
    def criaTabela(cls, engine):
        try:
            models.Base.metadata.create_all(engine)
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


class UsuarioDao():

    @classmethod
    def salvar(cls, usuario: models.Usuario, engine):
        sessao = ConfigDao.criaSession(engine)
        try:
            sessao.add(usuario)
            sessao.commit()
        except:
            sessao.rollback()

    @classmethod
    def alterar(cls, usuario: models.Usuario, engine):
        sessao = ConfigDao.criaSession(engine)
        x = sessao.query(models.Usuario).filter(
            models.Usuario.id == usuario.id).all()

        if len(usuario.nome) > 0:
            x[0].nome = usuario.nome
        if len(usuario.email) > 0:
            x[0].email = usuario.email
        if len(usuario.senha) > 0:
            x[0].senha = usuario.senha
    
        try:
            sessao.commit()
        except:
            sessao.rollback()

    @classmethod
    def remover(cls, usuario: models.Usuario, sessao):
        try:
            sessao.delete(usuario)
            sessao.commit()
        except:
            sessao.rollback()

    @classmethod
    def listar(cls, engine):
        sessao = ConfigDao.criaSession(engine)
        return sessao.query(models.Usuario).all()
