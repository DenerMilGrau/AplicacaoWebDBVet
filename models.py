from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///banco_vet.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))
#   bases declarativas permite q classes python representem tabelas
# sem precisar configurar a relação entre elas
Base = declarative_base()
Base.query = db_session.query_property()
#   pessoas q tem atividades


class Cliente(Base):
    __tablename__ = 'tab_cliente'
    id_cliente = Column(Integer, primary_key=True)
    nome_cliente = Column(String(40), nullable=False, index=True)
    sobrenome_cliente = Column(String(40), nullable=False, index=True)
    cpf = Column(Integer, nullable=False, index=True, unique=True)

#   representacao da clasee
    def __repr__(self):
        return '<Cliente: {}  - {} {}>'.format(self.id_cliente ,self.nome_cliente, self.sobrenome_cliente)
    #   salvar funções para executar mais tarde

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_cliente = {
            'id_cliente': self.id_cliente,
            'nome_cliente': self.nome_cliente,
            'sobrenome_cliente': self.sobrenome_cliente,
            'cpf': self.cpf,
        }
        return dados_cliente


class Animal(Base):
    # adicionar caracteristicas as colunas
    __tablename__ = 'tab_animal'
    id_animal = Column(Integer, primary_key=True)
    nome_animal = Column(String(40), nullable=False, index=True)
    raca_animal = Column(String(40), nullable=False, index=True)
    ano_nasc_animal = Column(Integer, nullable=False)
    id_cliente1 = Column(Integer, ForeignKey('tab_cliente.id_cliente'))
    Cliente = relationship('Cliente')

    def __repr__(self):
        return '<Animal: {} - {}>'.format( self.id_animal, self.nome_animal)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_animal = {
            'id_animal': self.id_animal,
            'nome_animal': self.nome_animal,
            'raca_animal': self.raca_animal,
            'ano_nasc_animal': self.ano_nasc_animal,

        }
        return dados_animal


class Categoria(Base):
    # adicionar caracteristicas as colunas
    __tablename__ = 'tab_categoria'
    id_categoria = Column(Integer, primary_key=True, index=True)
    nome_categoria = Column(String(40), nullable=False, index=True)

    def __repr__(self):
        return '<Categoria: {} - {}>'.format(self.id_categoria, self.nome_categoria)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_categoria = {
            'id_categoria': self.id_categoria,
            'nome_categoria': self.nome_categoria,
        }
        return dados_categoria


class Consulta(Base):
    # adicionar caracteristicas as colunas
    __tablename__ = 'tab_consulta'
    id_consulta = Column(Integer, primary_key=True)
    hora = Column(Integer, nullable=False)
    minuto = Column(Integer, nullable=False)
    data = Column(Integer, nullable=False, index=True)
    ano_nasc_animal = Column(Integer, nullable=False)
    id_motivo1 = Column(Integer, ForeignKey('tab_motivo.id_motivo'))
    id_cliente2 = Column(Integer, ForeignKey('tab_cliente.id_cliente'))
    id_animal1 = Column(Integer, ForeignKey('tab_animal.id_animal'))

    Animal = relationship('Animal')
    Motivo = relationship('Motivo')
    Cliente = relationship('Pessoa')

    def __repr__(self):
        return '<Consulta: {} - {}>'.format(self.id_animal, self.nome_animal)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_animal = {
            'id_animal': self.id_animal,
            'nome_animal': self.nome_animal,
            'raca_animal': self.raca_animal,
            'ano_nasc_animal': self.ano_nasc_animal,

        }
        return dados_animal


def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()