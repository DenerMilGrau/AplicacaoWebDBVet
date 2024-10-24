from models import Cliente, Animal, Consulta, Produto, Veterinario, Categoria, db_session
from sqlalchemy import select

global escolha_tabela
global dicionario
# global cpf_
# inserir dados na tabela


def inserir_cliente():
    while True:
        try:
            cpf_ = input('CPF: ')
            if len(cpf_) != 11 or '-' in cpf_:
                print('Deve ter ocorrido algum erro de digitação.'
                'Por favor verifique se foi digitado corretamente')
            else:
                cpf_int = int(cpf_)
                break

        except ValueError:
            print('Erro de valor')

    cliente = Cliente(nome_cliente=str(input('Nome: ')),
                    sobrenome_cliente=str(input('Sobrenome: ')),
                    cpf=cpf_int)

    print(cliente)
    cliente.save()


def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).all()
    print(var_cliente)


if __name__ == '__main__':
    consultar_cliente()
    # executa


def atualizar_cliente():
    # selecionar a pessoa a ser alterada
    var_cliente = select(Cliente).where(str(input('Nome: ')) == Cliente.nome_cliente)
    var_cliente = db_session.execute(var_cliente).scalar()
    # nome adicionado
    var_cliente.nome_cliente = str(input('Novo nome: '))
    var_cliente.save()


def deletar_cliente():
    pessoa_deletar = input('Quem você deseja deletar? : ')
    var_pessoa = select(Cliente).where(pessoa_deletar == Cliente.nome_cliente)
    var_pessoa = db_session.execute(var_pessoa).scalar()
    var_pessoa.delete()


# **************************************************************************************
# **************************************************************************************

def inserir_consulta():
    consulta = Consulta(data=int(input('Data: ')),
                        motivo=str(input('motivo: ')),
                        hora=int(input('Hora: ')),
                        minuto=int(input('minuto: ')))
    print(consulta)
    consulta.save()


def consultar_consulta():
    var_consulta = select(Consulta)
    var_consulta = db_session.execute(var_consulta).all()
    print(var_consulta)

if __name__ == '__main__':
    consultar_consulta()

def atualizar_consulta():
    var_consulta = select(Consulta).where(int(input('ID Consulta: ')) == Consulta.id_consulta)
    var_consulta = db_session.execute(var_consulta).scalar()
    var_consulta.motivo = str(input('Novo motivo: '))
    var_consulta.save()


def deletar_consulta():
    consulta_deletar = input('ID da consulta a deletar: ')
    var_consulta = select(Consulta).where(consulta_deletar == Consulta.id_consulta)
    var_consulta = db_session.execute(var_consulta).scalar()
    var_consulta.delete()


#######################################################################
#######################################################################

def inserir_animal():
    animal = Animal(nome_animal=str(input('Nome: ')),
                    raca_animal=str(input('raca: ')),
                    ano_nasc_animal=int(input('ano nasc: ')))
    print(animal)
    animal.save()


def consultar_animal():
    var_animal = select(Animal)
    var_animal = db_session.execute(var_animal).all()
    print(var_animal)

if __name__ == '__main__':
    consultar_animal()
def atualizar_animal():
    var_animal = select(Animal).where(str(input('Nome do animal: ')) == Animal.nome_animal)
    var_animal = db_session.execute(var_animal).scalar()
    var_animal.nome = str(input('Novo nome: '))
    var_animal.save()


def deletar_animal():
    animal_deletar = input('Nome do animal a deletar: ')
    var_animal = select(Animal).where(animal_deletar == Animal.nome_animal)
    var_animal = db_session.execute(var_animal).scalar()
    var_animal.delete()

#####################################################
#####################################################

def inserir_veterinario():
    veterinario = Veterinario(nome_vet=str(input('Nome: ')),
                              crmv=int(input('CRM: ')),
                              salario=float(input('Salario: ')),
                              valor_consulta=float(input('Valor da consulta: ')),
                              sobrenome_vet=str(input('Sobrenome: ')))
    print(veterinario)
    veterinario.save()


def consultar_veterinario():
    var_veterinario = select(Veterinario)
    var_veterinario = db_session.execute(var_veterinario).all()
    print(var_veterinario)

if __name__ == '__main__':
    consultar_veterinario()
def atualizar_veterinario():
    var_veterinario = select(Veterinario).where(str(input('Nome: ')) == Veterinario.nome_vet)
    var_veterinario = db_session.execute(var_veterinario).scalar()
    var_veterinario.nome = str(input('Novo nome: '))
    var_veterinario.save()


def deletar_veterinario():
    veterinario_deletar = input('Nome do veterinário a deletar: ')
    var_veterinario = select(Veterinario).where(veterinario_deletar == Veterinario.nome_vet)
    var_veterinario = db_session.execute(var_veterinario).scalar()
    var_veterinario.delete()

#########################################################
#########################################################

def inserir_produto():
    produto = Produto(produto=str(input('Nome do produto: ')),
                      preco=float(input('Preço: ')))
    print(produto)
    produto.save()


def consultar_produto():
    var_produto = select(Produto)
    var_produto = db_session.execute(var_produto).all()
    print(var_produto)

if __name__ == '__main__':
    consultar_produto()

def atualizar_produto():
    var_produto = select(Produto).where(str(input('Nome do produto: ')) == Produto.produto)
    var_produto = db_session.execute(var_produto).scalar()
    var_produto.nome = str(input('Novo nome: '))
    var_produto.save()


def deletar_produto():
    produto_deletar = input('Nome do produto a deletar: ')
    var_produto = select(Produto).where(produto_deletar == Produto.produto)
    var_produto = db_session.execute(var_produto).scalar()
    var_produto.delete()

#########################################################
#########################################################

def inserir_categoria():
    categoria = Categoria(nome_categoria=str(input('Nome da categoria: ')))
    print(categoria)
    categoria.save()


def consultar_categoria():
    var_categoria = select(Categoria)
    var_categoria = db_session.execute(var_categoria).all()
    print(var_categoria)

if __name__ == '__main__':
    consultar_categoria()

def atualizar_categoria():
    var_categoria = select(Categoria).where(str(input('Nome da categoria: ')) == Categoria.nome_categoria)
    var_categoria = db_session.execute(var_categoria).scalar()
    var_categoria.nome = str(input('Novo nome: '))
    var_categoria.save()


def deletar_categoria():
    categoria_deletar = input('Nome da categoria a deletar: ')
    var_categoria = select(Categoria).where(categoria_deletar == Categoria.nome_categoria)
    var_categoria = db_session.execute(var_categoria).scalar()
    var_categoria.delete()

#################################

def chamar_func(dicio, chave_func):
    func = dicio[chave_func]
    return func()

clientes = {
    '1': inserir_cliente,
    '2': consultar_cliente,
    '3': atualizar_cliente,
    '4': deletar_cliente
}
consultas = {
    '1': inserir_consulta,
    '2': consultar_consulta,
    '3': atualizar_consulta,
    '4': deletar_consulta
}
produtos = {
    '1': inserir_produto,
    '2': consultar_produto,
    '3': atualizar_produto,
    '4': deletar_produto
}
categorias = {
    '1': inserir_categoria,
    '2': consultar_categoria,
    '3': atualizar_categoria,
    '4': deletar_categoria
}
animais = {
    '1': inserir_animal,
    '2': consultar_animal,
    '3': atualizar_animal,
    '4': deletar_animal
}

veterinarios = {
    '1': inserir_veterinario,
    '2': consultar_veterinario,
    '3': atualizar_veterinario,
    '4': deletar_veterinario
}

if __name__ == '__main__':
    while True:

        print('Menu\n1- Cliente\n2-Veterinario\n3-Animal\n4-Produtos\n5-Categorias\n6-Consulta\n0-Sair')
        escolha = input('>> ')
        while escolha not in ['1', '2', '3', '4', '5', '6', '0']:
            print('\nEscolha inválida\n')
            print('Menu\n1- Cliente\n2-Veterinario\n3-Animal\n4-Produtos\n5-Categorias\n6-Consulta')
            escolha = input('>> ')

        if escolha == '1':
            dicionario = clientes
        elif escolha == '2':
            dicionario = veterinarios
        elif escolha == '3':
            dicionario = animais
        elif escolha == '4':
            dicionario = produtos
        elif escolha == '5':
            dicionario = categorias
        elif escolha == '6':
            dicionario = consultas
        elif escolha == '0':
            break

        print('Menu Funções\n1-Inserir\n2-Consultar\n3-Atualizar\n4-Deletar')
        escolha_func = input('>> ')
        while escolha_func not in ['1', '2', '3', '4']:
            print('\nEscolha inválida\n')
            print('Menu Funções\n1-Inserir\n2-Consultar\n3-Atualizar\n4-Deletar')
            escolha_func = input('>> ')
        chamar_func(dicionario, escolha_func)

