from flask import Flask, request, jsonify

from models import *


# HACKATHON SANTO MAIO 2023
# DESAFIO 2, TAREFA 1
# CANDIDATO: TIAGO SOUZA PAIVA


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:@localhost/adventureworks"
db.init_app(app)


@app.route('/products', methods=['POST'])
def create():
    """Rota para criar um novo Produto"""
    novo_produto = request.get_json()
    sub_cat_key = SubCategories.query.get(novo_produto['productsubcategorykey'])

    if sub_cat_key is None: # Testa se o novo produto possui um código existente
        return jsonify({'error': 'ProductSubCategoryKey inválido'})

    try:
        dados_produto = Products(
            productkey=novo_produto['productkey'],
            productsubcategorykey=novo_produto['productsubcategorykey'],
            productsku=novo_produto['productsku'],
            productname=novo_produto['productname'],
            modelname=novo_produto['modelname'],
            productdescription=novo_produto['productdescription'],
            productcolor=novo_produto['productcolor'],
            productsize=novo_produto['productsize'],
            productstyle=novo_produto['productstyle'],
            productcost=novo_produto['productcost'],
            productprice=novo_produto['productprice']
        )
        db.session.add(dados_produto)
        db.session.commit()
        return jsonify({'message': 'Dados enviados para o banco de dados com sucesso'})

    # Se Cair no exept provavelmente é por um productKey ja cadastrado, ou por tantar botar valor string em Interger
    except:
        return jsonify({'error': 'ProductKey já cadastrado ou tipo de dado incorreto!'})


@app.route('/products', methods=['GET'])
def read():
    """Rota para mostrar todos os produtos da table Products"""
    todos_produtos = Products.query.all()
    busca = []
    for produto in todos_produtos:
        resposta = {
            "productkey": produto.productkey,
            "productsubcategorykey": produto.productsubcategorykey,
            "productsku": produto.productsku,
            "productname": produto.productname,
            "modelname": produto.modelname,
            "productdescription": produto.productdescription,
            "productcolor": produto.productcolor,
            "productsize": produto.productsize,
            "productstyle": produto.productstyle,
            "productcost": produto.productcost,
            "productprice": produto.productprice
        }
        busca.append(resposta)
    return jsonify(busca)


@app.route('/products/<int:id>', methods=['GET'])
def read_id(id):
    """Rota de pesquisa de produtos por ID"""
    produto = Products.query.get(id)
    if produto:
        data = {
            "productkey": produto.productkey,
            "productsubcategorykey": produto.productsubcategorykey,
            "productsku": produto.productsku,
            "productname": produto.productname,
            "modelname": produto.modelname,
            "productdescription": produto.productdescription,
            "productcolor": produto.productcolor,
            "productsize": produto.productsize,
            "productstyle": produto.productstyle,
            "productcost": produto.productcost,
            "productprice": produto.productprice
        }
        return jsonify(data)
    else:
        return jsonify({"message": "Produto não encontrado"})


@app.route('/products/<int:id>', methods=['PUT'])
def update(id):
    """Rotas para Atualizar dados de um produto"""
    produto = Products.query.get(id)

    # checa de o id é valido
    if not produto:
        return jsonify({"message": "Produto não encontrado"})

    # Essas Variaveis aqui representão os valores novos
    productsubcategorykey = request.json.get('productsubcategorykey')
    productsku = request.json.get('productsku')
    productname = request.json.get('productname')
    modelname = request.json.get('modelname')
    productdescription = request.json.get('productdescription')
    productcolor = request.json.get('preto e branco')
    productsize = request.json.get('productsize')
    productstyle = request.json.get('productstyle')
    productcost = request.json.get('productcost')
    productprice = request.json.get('productprice')

    sub_cat_key = SubCategories.query.get(productsubcategorykey)

    # Testa se a atualização do produto possui um código ProductSubCategoryKey existente
    if productsubcategorykey:
        if sub_cat_key is None:
            return jsonify({'error': 'ProductSubCategoryKey inválido'})

    # esse monte de if é para checar item por item se existe algum valor novo a ser atualizado

    if productsubcategorykey:
        produto.productsubcategorykey = productsubcategorykey
    if productsku:
        produto.productsku = productsku
    if productname:
        produto.productname = productname
    if modelname:
        produto.modelname = modelname
    if productdescription:
        produto.productdescription = productdescription
    if productcolor:
        produto.productcolor = productcolor
    if productsize:
        produto.productsize = productsize
    if productstyle:
        produto.productstyle = productstyle
    if productcost:
        produto.productcost = productcost
    if productprice:
        produto.productprice = productprice
    db.session.commit()
    return jsonify({"message": "Produto atualizado com sucesso"})


@app.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    """Rota para deletar um produto"""
    drop_item = Products.query.get(id)
    if drop_item is None:
        return jsonify({"message": "Produto não encontrado"})

    db.session.delete(drop_item)
    db.session.commit()
    return jsonify({"message": "Produto excluído com sucesso"})


if __name__ == '__main__':
    app.run()