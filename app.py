from flask import Flask, render_template, request, redirect, url_for, flash
from models import Cliente, Animal, db_session, Produto, Veterinario, Categoria, Consulta, Venda, Motivo
from sqlalchemy import select


def dicionario_colunas_motivo():
    dicion = {
        "motivo": "Motivo",
        "categoria_motivo": "Categoria motivo",
        "valor_motivo": "Valor motivo",
        "id_motivo": "ID Motivo"
    }
    return dicion


def dicionario_colunas_consulta():
    dicion = {
        "id_consulta": "ID Consulta",
        "data": "Data",
        "id_motivo1": "ID Motivo",
        "id_cliente": "ID Cliente",
    }
    return dicion


def dicionario_colunas_venda():
    dicion = {
        "id_venda": "ID Venda",
        "data_venda": "Data",
        "id_produto1": "ID Produto",
        "id_cliente3": "ID Cliente",
        "id_categoria": "ID Categoria",
        "quantidade": "Quantidade",
    }
    return dicion


def dicionario_colunas_animal():
    dicion = {
        "id_animal": "ID Animal",
        "nome_animal": "Nome",
        "raca_animal": "Raça",
        "ano_nasc_animal": "Ano nasc. animal",
        "id_cliente1": "ID Cliente",
    }
    return dicion


def dicionario_colunas_categoria():
    dicion = {
        "id_categoria": "ID Categoria",
        "nome_categoria": "Nome",

    }
    return dicion


def dicionario_colunas_produto():
    dicion = {
        "id_produto": "ID Produto",
        "produto": "Produto",
        "preco": "Preço",
        "id_categoria": "ID Categoria",
        "nome_categoria": "Categoria",

    }
    return dicion


def dicionario_colunas_veterinario():
    dicion = {
        "id_vet": "ID Veterinário",
        "salario": "Salário",
        "nome_vet": "Nome",
        "crmv": "CRMV",
        "valor_consulta": "Valor Consulta"

    }
    return dicion


def dicionario_colunas_cliente():
    dicion = {
        "id_cliente": "ID Cliente",
        "nome_cliente": "Nome",
        "profissao_cliente": "Profissão cliente",
        "area_cliente": "Área de atuação",
        "cpf": "CPF"

    }
    return dicion


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def index():
    return redirect('home')


@app.route('/home', methods=['GET'])
def home():

    return render_template('dashboard.html')


@app.route('/clientes', methods=['GET', 'POST'])
def clientes_func():
    lista_clientes = select(Cliente).select_from(Cliente)
    lista_clientes = db_session.execute(lista_clientes).scalars()
    resultado = []
    print(lista_clientes)
    for cliente in lista_clientes:
        resultado.append(cliente.serialize_cliente())
    dicion = dicionario_colunas_cliente()
    numero_resultados = len(resultado)
    return render_template('cliente.html', var_cliente=resultado, numero_resultados=numero_resultados, class_=Cliente, dicio=dicion, pesquisa=False)


@app.route('/animais', methods=['GET', 'POST'])
def animais_func():
    lista_animais_sql = select(Animal, Cliente).join(Cliente, Animal.id_cliente1 == Cliente.id_cliente)
    lista_animais = db_session.execute(lista_animais_sql).fetchall()

    # resultado=[]
    # for animal in lista_animais:
    #     resultado.append(animal.serialize_animal())

    numero_resultados = len(lista_animais)
    dicion = dicionario_colunas_animal()
    return render_template('animal.html', var_animal=lista_animais, numero_resultados=numero_resultados, class_=Animal, dicio=dicion, pesquisa=False)


@app.route('/consultas', methods=['GET', 'POST'])
def consultas_func():
    lista_consultas_sql = (select(Consulta, Veterinario, Motivo, Animal, Cliente).join(Veterinario, Consulta.id_vet1 == Veterinario.id_vet).join(
        Animal, Consulta.id_animal1 == Animal.id_animal).join(Cliente, Animal.id_cliente1 == Cliente.id_cliente).join(
        Motivo, Consulta.id_motivo1 == Motivo.id_motivo))


    resultado = db_session.execute(lista_consultas_sql).fetchall()
    numero_resultados = len(resultado)
    dicion = dicionario_colunas_consulta()
    return render_template('consulta.html', var_consulta=resultado, dicio=dicion, class_=Consulta, pesquisa=False, numero_resultados=numero_resultados)


@app.route('/consultas/<int:id_consulta>', methods=['GET'])
def consulta_detalhes_func(id_consulta):

    var_consulta = request.args.get('var_consulta')
    print(f'detalhes:{var_consulta}')
    consulta_sql = (select(Consulta, Veterinario, Motivo, Animal, Cliente)
                    .where(Consulta.id_consulta == id_consulta)
                    .join(Veterinario, Consulta.id_vet1 == Veterinario.id_vet)
                    .join(Animal, Consulta.id_animal1 == Animal.id_animal)
                    .join(Cliente, Animal.id_cliente1 == Cliente.id_cliente)
                    .join(Motivo, Consulta.id_motivo1 == Motivo.id_motivo))

    consulta_detalhada = db_session.execute(consulta_sql).fetchone()

    return render_template('consulta-detalhes.html', consulta=consulta_detalhada, var_consulta=var_consulta)


@app.route('/produtos', methods=['GET', 'POST'])
def produtos_func():
    lista_produtos = select(Produto, Categoria).join(Categoria, Produto.id_categoria1 == Categoria.id_categoria)
    lista_produtos = db_session.execute(lista_produtos).fetchall()
    numero_resultados = len(lista_produtos)
    dicion = dicionario_colunas_produto()
    return render_template('produto.html', var_produto=lista_produtos, class_=Produto, dicio=dicion, pesquisa=False, numero_resultados=numero_resultados)


@app.route('/veterinarios', methods=['GET', 'POST'])
def veterinarios_func():
    lista_veterinarios = select(Veterinario).select_from(Veterinario)
    lista_veterinarios = db_session.execute(lista_veterinarios).scalars()
    resultado = []
    for veterinario in lista_veterinarios:
        resultado.append(veterinario.serialize_veterinario())
    numero_resultados = len(resultado)
    dicion = dicionario_colunas_veterinario()
    return render_template('veterinario.html', var_veterinario=resultado, class_=Veterinario, numero_resultados=numero_resultados, pesquisa=False, dicio=dicion)


@app.route('/categorias', methods=['GET', 'POST'])
def categorias_func():
    lista_categorias = select(Categoria).select_from(Categoria)
    lista_categorias = db_session.execute(lista_categorias).scalars()
    resultado = []
    for categoria in lista_categorias:
        resultado.append(categoria.serialize_categoria())
    numero_resultados = len(resultado)
    dicion = dicionario_colunas_categoria()
    return render_template('categoria.html', var_categoria=resultado, class_=Categoria, pesquisa=False, numero_resultados=numero_resultados, dicio=dicion)


@app.route('/vendas', methods=['GET', 'POST'])
def vendas_func():
    lista_vendas_sql = (select(Venda, Cliente, Produto, Categoria).join(Cliente, Venda.id_cliente3 == Cliente.id_cliente).join(
        Produto, Venda.id_produto1 == Produto.id_produto).join
                        (Categoria, Produto.id_categoria1 == Categoria.id_categoria))

    lista_vendas = db_session.execute(lista_vendas_sql).fetchall()

    dicion = dicionario_colunas_venda()
    numero_vendas = len(lista_vendas)

    return render_template('venda.html', var_venda=lista_vendas, dicio=dicion, class_=Venda, pesquisa=False, numero_resultados=numero_vendas)


@app.route('/motivos', methods=['GET', 'POST'])
def motivos_func():
    lista_motivos = select(Motivo)
    lista_motivos = db_session.execute(lista_motivos).scalars()
    resultado=[]
    for motivo in lista_motivos:
        resultado.append(motivo.serialize_motivo())
    dicion = dicionario_colunas_motivo()
    numero_resultados= len(resultado)
    return render_template('motivo.html', var_motivo=resultado, dicio=dicion, class_=Motivo, numero_resultados=numero_resultados, pesquisa=False)


dicionario_classes = {
    "<class 'models.Motivo'>": Motivo,
    "<class 'models.Consulta'>": Consulta,
    "<class 'models.Venda'>": Venda,
    "<class 'models.Animal'>": Animal,
    "<class 'models.Categoria'>": Categoria,
    "<class 'models.Produto'>": Produto,
    "<class 'models.Veterinario'>": Veterinario,
    "<class 'models.Cliente'>": Cliente

}


@app.route('/pesquisar_/<class_>', methods=['GET', 'POST'])
def pesquisar_func(class_):

    if request.method == 'POST':
        campo = request.form['campo']
        print(f'campo : {campo}')
        classe = dicionario_classes[class_]
        print(f'class : {classe}')
        termo_pesquisa = request.form.get('form-pesquisa')
        print(f'termo : {termo_pesquisa}')
        if not campo or not termo_pesquisa:
            flash('Por favor, selecione um campo e insira um termo de pesquisa.')
            # return redirect(url_for('motivos_func'))

        if classe == Consulta:
            if campo == 'id_cliente':
                classe = Cliente

            if campo in ['id_consulta', 'id_motivo1', 'id_animal1', 'id_vet1', 'id_cliente']:
                lista_consultas_sql = (select(Consulta, Veterinario, Motivo, Animal, Cliente)
                                       .join(Veterinario, Consulta.id_vet1 == Veterinario.id_vet)
                                       .join(Animal, Consulta.id_animal1 == Animal.id_animal)
                                       .join(Cliente, Animal.id_cliente1 == Cliente.id_cliente)
                                       .join(Motivo, Consulta.id_motivo1 == Motivo.id_motivo)).where(getattr(classe, campo) == termo_pesquisa)
            elif campo not in ['id_consulta', 'id_motivo1', 'id_animal1', 'id_vet1', 'id_cliente']:
                lista_consultas_sql = (select(Consulta, Veterinario, Motivo, Animal, Cliente)
                                       .join(Veterinario, Consulta.id_vet1 == Veterinario.id_vet)
                                       .join(Animal, Consulta.id_animal1 == Animal.id_animal)
                                       .join(Cliente, Animal.id_cliente1 == Cliente.id_cliente)
                                       .join(Motivo, Consulta.id_motivo1 == Motivo.id_motivo)).where(
                    getattr(classe, campo).like(f'%{termo_pesquisa}%'))

            resultado = db_session.execute(lista_consultas_sql).fetchall()
            numero_resultados = len(resultado)
            dicion = dicionario_colunas_consulta()
            print('\n\n\n\n######### PESQUISA ########## \n\n\n\n')

            return render_template('consulta.html', var_consulta=resultado, dicio=dicion, class_=class_, pesquisa=True, numero_resultados=numero_resultados)

# se aplica com tabelas q n recebem FK como motivo, categoria, cliente e veterinario, mudando apenas o dicionario

        elif classe in [Motivo, Categoria, Veterinario, Cliente]:
            if 'id' not in campo:
                consulta = select(classe).where(getattr(classe, campo).like(f"%{termo_pesquisa}%"))
                lista_resultados = db_session.execute(consulta).scalars()
            else:
                consulta = select(classe).where(getattr(classe, campo) == termo_pesquisa)
            lista_resultados = db_session.execute(consulta).scalars()
            resultado = []
            if classe == Motivo:
                for result in lista_resultados:
                    resultado.append(result.serialize_motivo())
                dicion = dicionario_colunas_motivo()
                numero_resultados = len(resultado)
                return render_template('motivo.html', var_motivo=resultado, dicio=dicion, class_=class_, numero_resultados=numero_resultados, pesquisa=True)
            elif classe == Categoria:
                for result in lista_resultados:
                    resultado.append(result.serialize_categoria())
                dicion = dicionario_colunas_categoria()
                numero_resultados = len(resultado)
                return render_template('categoria.html', var_categoria=resultado, dicio=dicion, class_=class_, numero_resultados=numero_resultados, pesquisa=True)
            elif classe == Veterinario:
                for result in lista_resultados:
                    resultado.append(result.serialize_veterinario())
                dicion = dicionario_colunas_veterinario()
                numero_resultados = len(resultado)
                return render_template('veterinario.html', var_veterinario=resultado, dicio=dicion, class_=class_, numero_resultados=numero_resultados, pesquisa=True)
            elif classe == Cliente:
                for result in lista_resultados:
                    resultado.append(result.serialize_cliente())
                dicion = dicionario_colunas_cliente()
                numero_resultados = len(resultado)
                return render_template('cliente.html', var_cliente=resultado, dicio=dicion, class_=class_, numero_resultados=numero_resultados, pesquisa=True)

        elif classe == Venda:
            print(f'campo:{campo}')
            if 'categoria' in campo:
                classe = Categoria

            if 'id' not in campo:
                print('geral')
                consulta = select(Venda, Cliente, Produto, Categoria).join(Produto, Venda.id_produto1 == Produto.id_produto).join(
                    Cliente, Venda.id_cliente3 == Cliente.id_cliente).join(Categoria, Produto.id_categoria1 == Categoria.id_categoria).where(
                getattr(classe, campo).like(f"%{termo_pesquisa}%")
                )
            else:

                print('exata')
                consulta = select(Venda, Cliente, Produto, Categoria).join(Produto, Venda.id_produto1 == Produto.id_produto).join(
                    Cliente, Venda.id_cliente3 == Cliente.id_cliente).join(Categoria, Produto.id_categoria1 == Categoria.id_categoria).where(
                    getattr(classe, campo) == termo_pesquisa)

            resultado = db_session.execute(consulta).fetchall()
            numero_resultados = len(resultado)
            dicion = dicionario_colunas_venda()
            return render_template('venda.html', var_venda=resultado, dicio=dicion, class_=class_, pesquisa=True, numero_resultados=numero_resultados)
        elif classe == Animal:
            if 'id' not in campo:
                consulta = select(Animal, Cliente).join(
                    Cliente, Animal.id_cliente1 == Cliente.id_cliente).where(
                getattr(classe, campo).like(f"%{termo_pesquisa}%")
                )
            else:
                consulta = select(Animal, Cliente).join(
                    Cliente, Animal.id_cliente1 == Cliente.id_cliente).where(
                    getattr(classe, campo) == termo_pesquisa)

            resultado = db_session.execute(consulta).fetchall()
            numero_resultados= len(resultado)
            dicion = dicionario_colunas_animal()
            return render_template('animal.html', var_animal=resultado, dicio=dicion, class_=class_, pesquisa=True, numero_resultados=numero_resultados)

        elif classe == Produto:
            if 'categoria' in campo:
                classe = Categoria
            if 'id' not in campo:
                consulta = select(Produto, Categoria).join(
                    Categoria, Produto.id_categoria1 == Categoria.id_categoria).where(
                getattr(classe, campo).like(f"%{termo_pesquisa}%")
                )
            else:
                consulta = select(Produto, Categoria).join(
                    Categoria, Produto.id_categoria1 == Categoria.id_categoria).where(
                    getattr(classe, campo) == termo_pesquisa)

            resultado = db_session.execute(consulta).fetchall()
            numero_resultados= len(resultado)
            dicion = dicionario_colunas_produto()
            return render_template('produto.html', var_produto=resultado, dicio=dicion, class_=class_, pesquisa=True, numero_resultados=numero_resultados)


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