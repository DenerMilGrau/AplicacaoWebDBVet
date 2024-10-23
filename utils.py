from models import Cliente, Animal, Consulta, Produto, Veterinario, Categoria, db_session
from sqlalchemy import select

global escolha_tabela
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

    pessoa = Cliente(nome_cliente=str(input('Nome: ')),
                    sobrenome_cliente=str(input('Sobrenome: ')),
                    cpf=cpf_int)

    print(pessoa)
    pessoa.save()


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
    var_cliente.nome = str(input('Novo nome: '))
    var_cliente.save()


def deletar_cliente():
    pessoa_deletar = input('Quem você deseja deletar? : ')
    var_pessoa = select(Cliente).where(pessoa_deletar == Cliente.nome_cliente)
    var_pessoa = db_session.execute(var_pessoa).scalar()
    var_pessoa.delete()


# **************************************************************************************
# **************************************************************************************

def inserir_consulta():
    consulta = Consulta(data_consulta=int(input('Data: ')),
                        descricao=str(input('Descrição: ')),
                        id_cliente=int(input('ID Cliente: ')),
                        id_animal=int(input('ID Animal: ')))
    print(consulta)
    consulta.save()


def consultar_consulta():
    var_consulta = select(Consulta)
    var_consulta = db_session.execute(var_consulta).all()
    print(var_consulta)

if __name__ == '__main__':
    inserir_consulta()

def atualizar_consulta():
    var_consulta = select(Consulta).where(int(input('ID Consulta: ')) == Consulta.id_consulta)
    var_consulta = db_session.execute(var_consulta).scalar()
    var_consulta.descricao = str(input('Nova descrição: '))
    var_consulta.save()


def deletar_consulta():
    consulta_deletar = input('ID da consulta a deletar: ')
    var_consulta = select(Consulta).where(consulta_deletar == Consulta.id_consulta)
    var_consulta = db_session.execute(var_consulta).scalar()
    var_consulta.delete()


#######################################################################
#######################################################################
if __name__ == '__main__':

    while True:

        print('Menu\n1- Inserir\n2-Consultar\n3-Atualizar\n4-Deletar\n5- Sair')
        escolha = input('>> ')
        if escolha != '5':
            escolha_tabela = input('Escolha uma tabela de dados?\n1-pessoa\n2-atividade\n>> ')
            while escolha_tabela not in ['1', '2']:
                print('Digite "1" ou "2" para continuar')
                escolha_tabela = input('Escolha uma tabela de dados?\n1-pessoa\n2-atividade\n>> ')

        if escolha == '1':
            print('inserir')
            if escolha_tabela == '1':
                print('inserir pessoa')
                inserir_pessoa()
            else:
                inserir_atividade()
        elif escolha == '2':
            if escolha_tabela == '1':
                consultar_pessoa()
            elif escolha_tabela == '2':
                consultar_atividade()
        elif escolha == '3':
            if escolha_tabela == '1':
                atualizar_pessoa()
            elif escolha_tabela == '2':
                atualizar_atividade()
        elif escolha == '4':
            if escolha_tabela == '1':
                deletar_pessoa()
            elif escolha_tabela == '2':
                deletar_atividade()
        elif escolha == '5':
            break
        else:
            print('\ndigite um numero de 1 a 5')