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


@app.route('/consultas')
def consultas_func():
    lista_consultas_sql = (select(Consulta, Veterinario, Motivo, Animal, Cliente).join(Veterinario, Consulta.id_vet1 == Veterinario.id_vet).join(
        Animal, Consulta.id_animal1 == Animal.id_animal).join(Cliente, Animal.id_cliente1 == Cliente.id_cliente).join(
        Motivo, Consulta.id_motivo1 == Motivo.id_motivo))

    lista_consultas = db_session.execute(lista_consultas_sql).fetchall()
    print(lista_consultas)
    return render_template('consulta.html', var_consulta=lista_consultas)


@app.route('/consultas/<int:id_consulta>')
def consulta_detalhes_func(id_consulta):
    consulta_sql = (select(Consulta, Veterinario, Motivo, Animal, Cliente)
                    .where(Consulta.id_consulta == id_consulta)
                    .join(Veterinario, Consulta.id_vet1 == Veterinario.id_vet)
                    .join(Animal, Consulta.id_animal1 == Animal.id_animal)
                    .join(Cliente, Animal.id_cliente1 == Cliente.id_cliente)
                    .join(Motivo, Consulta.id_motivo1 == Motivo.id_motivo))

    consulta_detalhada = db_session.execute(consulta_sql).fetchone()
    return render_template('consulta-detalhes.html', consulta=consulta_detalhada)


@app.route('/produtos')
def produtos_func():
    lista_produtos = select(Produto).select_from(Produto)
    lista_produtos = db_session.execute(lista_produtos).scalars()
    resultado = []
    for produto in lista_produtos:
        resultado.append(produto.serialize_produto())
    return render_template('produto.html', var_produto=resultado)


@app.route('/veterinarios')
def veterinarios_func():
    lista_veterinarios = select(Veterinario).select_from(Veterinario)
    lista_veterinarios = db_session.execute(lista_veterinarios).scalars()
    resultado = []
    for veterinario in lista_veterinarios:
        resultado.append(veterinario.serialize_veterinario())
    return render_template('veterinario.html', var_veterinario=resultado)


@app.route('/categorias')
def categorias_func():
    lista_categorias = select(Categoria).select_from(Categoria)
    lista_categorias = db_session.execute(lista_categorias).scalars()
    resultado = []
    for categoria in lista_categorias:
        resultado.append(categoria.serialize_categoria())
    return render_template('categoria.html', var_categoria=resultado)


@app.route('/vendas')
def vendas_func():
    lista_vendas_sql = (select(Venda, Cliente, Produto, Categoria).join(Cliente, Venda.id_cliente3 == Cliente.id_cliente).join(
        Produto, Venda.id_produto1 == Produto.id_produto).join
                        (Categoria, Produto.id_categoria1 == Categoria.id_categoria))

    lista_vendas = db_session.execute(lista_vendas_sql).fetchall()

    return render_template('venda.html', var_venda=lista_vendas)


@app.route('/motivos')
def motivos_func():
    lista_motivos = select(Motivo)
    lista_motivos = db_session.execute(lista_motivos).scalars()
    resultado=[]
    for motivo in lista_motivos:
        resultado.append(motivo.serialize_motivo())
    dicio = {
        "motivo": "Motivo",
        "categoria_motivo": "Categoria motivo",
        "valor_motivo": "Valor motivo",
    }

    return render_template('motivo.html', var_motivo=resultado)


@app.route('/clientes/cadastro', methods=['GET', 'POST'])
def cadastro_clientes_func():
    if request.method == "POST":
        nome = request.form['form-nome-cliente']
        profissao = request.form['form-profissao-cliente']
        area = request.form['form-area-cliente']
        cpf = request.form['form-cpf']
        telefone = request.form['form-telefone-cliente']
        # preciso verificar se o cpf é unico para evitar um erro de integridade
        if not nome or not telefone or not cpf or not profissao or not area:
            flash('Todos os campos devem estar preenchidos!', 'error')
        else:
            if len(cpf) != 11:
                flash('O CPF deve ter 11 digitos!', 'error')
            else:
                if len(telefone) != 11:
                    flash('Um telefone deve ter 11 digitos', 'error')
                else:

                    cpf_ = str(cpf)
                    cpf_f = '{0}.{1}.{2}-{3}'.format(cpf_[:3], cpf_[3:6], cpf_[6:9], cpf_[9:])

                    cpf_cliente = select(Cliente).where(Cliente.cpf == cpf_)
                    cpf_cliente = db_session.execute(cpf_cliente).scalar()
                    if not cpf_cliente:
                        tel = str(telefone)
                        telefone = '({0}){1}-{2}'.format(tel[:2], tel[2:7], tel[7:])

                        form_add = Cliente(nome_cliente=nome, telefone_cliente=telefone, cpf=cpf_f,
                                           profissao_cliente=profissao, area_cliente=area)
                        form_add.save()
                        db_session.close()
                        flash('Cliente cadastrado com sucesso!', 'success')
                    else:
                        flash('CPF ja existe!', 'error')

    return render_template('/form/cadastro-cliente.html')


@app.route('/animais/cadastro', methods=['GET', 'POST'])
def cadastro_animais_func():
    if request.method == "POST":
        nome = request.form['form-nome-animal']
        raca = request.form['form-raca']
        ano_nasc = request.form['form-ano-nasc']
        if not nome or not raca or not ano_nasc:
            flash('Todos os campos precisam ser preenchidos', 'error')
        else:
            try:
                ano_nasc_int = int(ano_nasc)
                if ano_nasc_int < 2000 or ano_nasc_int > 2024:
                    flash('Informe os valores corretos!', 'error')
                else:
                    form_add = Animal(nome_animal=nome, raca_animal=raca, ano_nasc_animal=ano_nasc_int)
                    form_add.save()
                    db_session.close()
                    flash('Cliente cadastrado com sucesso!', 'success')

            except ValueError:
                flash('Informe os valores corretos!', 'error')
    return render_template('/form/cadastro-animal.html')


@app.route('/sobre-nos')
def sobre_nos_func():
    return render_template('sobre-nos.html')


if __name__ == '__main__':
    app.run(debug=True)