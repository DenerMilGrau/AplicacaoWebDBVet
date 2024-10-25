from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///base_vet_analise_3.sqlite3')
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
    cpf = Column(Integer, nullable=False, index=True, unique=True)
    telefone_cliente = Column(String(20), nullable=False, index=True)
    profissao_cliente = Column(String(40), nullable=False, index=True)
    area_cliente = Column(String(40), nullable=False, index=True)
#   representacao da clasee
    def __repr__(self):
        return '<Cliente: {}  - {}>'.format(self.id_cliente, self.nome_cliente)
    #   salvar funções para executar mais tarde

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_cliente(self):
        dados_cliente = {
            'id_cliente': self.id_cliente,
            'nome_cliente': self.nome_cliente,
            'telefone_cliente': self.telefone_cliente,
            'profissao_cliente': self.profissao_cliente,
            'area_cliente': self.area_cliente,
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
    cliente = relationship('Cliente')

    def __repr__(self):
        return '<Animal: {} - {}>'.format(self.id_animal, self.nome_animal)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_animal(self):
        dados_animal = {
            'id_animal': self.id_animal,
            'nome_animal': self.nome_animal,
            'raca_animal': self.raca_animal,
            'ano_nasc_animal': self.ano_nasc_animal,
            'id_cliente1': self.id_cliente1,
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

    def serialize_categoria(self):
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
    id_vet1 = Column(Integer, ForeignKey('tab_veterinario.id_vet'))
    # id_cliente2 = Column(Integer, ForeignKey('tab_cliente.id_cliente'))
    id_animal1 = Column(Integer, ForeignKey('tab_animal.id_animal'))
    id_motivo1 = Column(Integer, ForeignKey('tab_motivo.id_motivo'))

    animal = relationship('Animal')
    # cliente = relationship('Cliente')
    veterinario = relationship('Veterinario')
    motivo = relationship('Motivo')

    def __repr__(self):
        return '<Consulta: {} - {}:{}>'.format(self.id_consulta, self.hora, self.minuto)
#

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_consulta(self):
        dados_consulta = {
            'id_consulta': self.id_consulta,
            'id_animal1': self.id_animal1,
            # 'id_cliente2': self.id_cliente2,
            'id_motivo1': self.id_motivo1,
            'id_vet1': self.id_vet1,
            'hora': self.hora,
            'minuto': self.minuto,
            'data': self.data,

        }
        return dados_consulta

class Veterinario(Base):
    __tablename__ = 'tab_veterinario'
    id_vet = Column(Integer, primary_key=True)
    nome_vet = Column(String(40), nullable=False, index=True)
    crmv = Column(Integer, nullable=False, index=True, unique=True)
    salario = Column(Float, nullable=False, index=True)
    valor_consulta = Column(Float, nullable=False, index=True)

#   representacao da clasee
    def __repr__(self):
        return '<Veterinário: {}  - {}>'.format(self.id_vet, self.nome_vet)
    #   salvar funções para executar mais tarde

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_veterinario(self):
        dados_vet = {
            'id_vet': self.id_vet,
            'nome_vet': self.nome_vet,
            'crmv': self.crmv,
            'salario': self.salario,
            'valor_consulta': self.valor_consulta,
        }
        return dados_vet

class Produto(Base):
    __tablename__ = 'tab_produto'
    id_produto = Column(Integer, primary_key=True)
    produto = Column(String(40), nullable=False, index=True)
    preco = Column(Float, nullable=False, index=True)

    id_categoria1 = Column(Integer, ForeignKey('tab_categoria.id_categoria'))

#   representacao da clasee
    def __repr__(self):
        return '<Produto: {} - {} {}>'.format(self.id_produto, self.produto, self.preco)
    #   salvar funções para executar mais tarde

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_produto(self):
        dados_produto = {
            'id_produto': self.id_produto,
            'produto': self.produto,
            'preco': self.preco,
        }
        return dados_produto


class Venda(Base):
    __tablename__ = 'tab_venda'
    id_venda = Column(Integer, primary_key=True)
    quantidade = Column(Integer, nullable=False)
    id_cliente3 = Column(Integer, ForeignKey('tab_cliente.id_cliente'))
    id_produto1 = Column(Integer, ForeignKey('tab_produto.id_produto'))
    data_venda = Column(Integer, nullable=False, index=True)

    Cliente = relationship('Cliente')
    Produto = relationship('Produto')
    def __repr__(self):
        return '<Venda: {} - {} {}>'.format(self.id_venda, self.data_venda, self.quantidade)
    #   salvar funções para executar mais tarde

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_venda(self):
        dados_venda = {
            'id_venda': self.id_venda,
            'quantidade': self.quantidade,
            'data': self.data_venda,

        }
        return dados_venda


class Motivo(Base):
    __tablename__ ='tab_motivo'
    id_motivo = Column(Integer, primary_key=True)
    motivo = Column(String(40), nullable=False, index=True)
    categoria_motivo = Column(String(40), nullable=False, index=True)
    valor_motivo = Column(Float, nullable=False, index=True)

    def __repr__(self):
        return '<Motivo: {} - {} >'.format(self.id_motivo, self.motivo)
    #   salvar funções para executar mais tarde

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_motivo(self):
        dados_motivo = {
            'id_motivo': self.id_motivo,
            'valor_motivo': self.valor_motivo,
            'categoria_motivo': self.categoria_motivo,
            'motivo': self.motivo

        }
        return dados_motivo
# cliente**, animal** vet** consulta* e produt**, categoria*, venda**, motivo


def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()