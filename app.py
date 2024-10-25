from flask import Flask, render_template, request, redirect, url_for, flash
from models import Cliente, Animal, db_session, Produto, Veterinario, Categoria, Consulta, Venda, Motivo
from sqlalchemy import select

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def index():
    return redirect('home')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/clientes')
def clientes_func():
    lista_clientes = select(Cliente).select_from(Cliente)
    lista_clientes = db_session.execute(lista_clientes).scalars()
    resultado = []
    print(lista_clientes)
    for cliente in lista_clientes:
        resultado.append(cliente.serialize_cliente())
    return render_template('cliente.html', var_cliente=resultado)


@app.route('/animais')
def animais_func():
    lista_animais_sql = select(Animal, Cliente).join(Cliente, Animal.id_cliente1 == Cliente.id_cliente)
    lista_animais = db_session.execute(lista_animais_sql).fetchall()

    # resultado=[]
    # for animal in lista_animais:
    #     resultado.append(animal.serialize_animal())

    print(lista_animais)
    return render_template('animal.html', var_animal=lista_animais)


@app.route('/consulta')
def consultas_func():
    lista_consultas_sql = (select(Consulta, Veterinario, Motivo, Animal, Cliente).join(Veterinario, Consulta.id_vet1 == Veterinario.id_vet).join(
        Animal, Consulta.id_animal1 == Animal.id_animal).join(Cliente, Animal.id_cliente1 == Cliente.id_cliente).join(
        Motivo, Consulta.id_motivo1 == Motivo.id_motivo))

    lista_consultas = db_session.execute(lista_consultas_sql).fetchall()
    print(lista_consultas)
    return render_template('consulta.html', var_consulta=lista_consultas)


@app.route('/produto')
def produtos_func():
    lista_produtos = select(Produto).select_from(Produto)
    lista_produtos = db_session.execute(lista_produtos).scalars()
    resultado = []
    for produto in lista_produtos:
        resultado.append(produto.serialize_produto())
    return render_template('produto.html', var_produto=resultado)


@app.route('/veterinario')
def veterinarios_func():
    lista_veterinarios = select(Veterinario).select_from(Veterinario)
    lista_veterinarios = db_session.execute(lista_veterinarios).scalars()
    resultado = []
    for veterinario in lista_veterinarios:
        resultado.append(veterinario.serialize_veterinario())
    return render_template('veterinario.html', var_veterinario=resultado)


@app.route('/categoria')
def categorias_func():
    lista_categorias = select(Categoria).select_from(Categoria)
    lista_categorias = db_session.execute(lista_categorias).scalars()
    resultado = []
    for categoria in lista_categorias:
        resultado.append(categoria.serialize_categoria())
    return render_template('categoria.html', var_categoria=resultado)


@app.route('/venda')
def vendas_func():
    lista_vendas_sql = (select(Venda, Cliente, Produto, Categoria).join(Cliente, Venda.id_cliente3 == Cliente.id_cliente).join(
        Produto, Venda.id_produto1 == Produto.id_produto).join
                        (Categoria, Produto.id_categoria1 == Categoria.id_categoria))

    lista_vendas = db_session.execute(lista_vendas_sql).fetchall()

    return render_template('venda.html', var_venda=lista_vendas)


@app.route('/motivo')
def motivos_func():
    lista_motivos = select(Motivo)
    lista_motivos = db_session.execute(lista_motivos).scalars()
    resultado=[]
    for motivo in lista_motivos:
        resultado.append(motivo.serialize_motivo())

    return render_template('motivo.html', var_motivo=resultado)


if __name__ == '__main__':
    app.run(debug=True)