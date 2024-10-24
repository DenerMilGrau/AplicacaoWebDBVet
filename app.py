from flask import Flask, render_template, request, redirect, url_for, flash
from models import Cliente, Animal, db_session, Produto, Veterinario, Categoria, Consulta, Venda
from sqlalchemy import select, join

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
    lista_animais = db_session.execute(lista_animais_sql).scalars().all()
    nome_cliente = Cliente.nome_cliente
    sobrenome_cliente = Cliente.sobrenome_cliente
    resultado=[]
    for animal in lista_animais:
        resultado.append(animal.serialize_animal())

    print(resultado)
    return render_template('animal.html', var_animal=resultado, nome_cliente=nome_cliente, sobrenome_cliente=sobrenome_cliente)


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


@app.route('/consulta')
def consultas_func():
    lista_consultas = select(Consulta).select_from(Consulta)
    lista_consultas = db_session.execute(lista_consultas).scalars()
    resultado = []
    for consulta in lista_consultas:
        resultado.append(consulta.serialize_consulta())

    print(resultado)
    return render_template('consulta.html', var_consulta=resultado)


if __name__ == '__main__':
    app.run(debug=True)