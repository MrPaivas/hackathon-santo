CANDIDATO: TIAGO SOUZA PAIVA

TAREFA 1

A indeia inicial do projeto é desenvolver uma api rest para distibuição e controle de dados de banco de dados.

1. REQUIREMENTS
* O LINGUAGEM ESCOLHIDA FOI O PYTHON.
* O FRAME-WORK ESCOLHIDO FOI O FLASK
* O ORM ESCOLHIDO FOI SQLALCHEMY

2. ROTAS 
* ROTA '/products' USANDO O MÉTODO POST:

     Essa rota tem finalidade de criar um novo item no banco de dados. O utilizador deve fornecer um arquivo JSON
contendo os dados do novo produto.


* ROTA '/products' USANDO O MÉTODO GET:

    Essa rota retorna todos os itens do banco de dados de Produtos


* ROTA '/products/id' USANDO O MÉTODO GET:

    Essa rota retorna os dados de um produto específico fornecido pelo utilizador atravez da URL ({id}).


* ROTA '/products/id' USANDO O METODO PUT:

    Essa rota atualiza os dados de um produto específico fornecido pelo utilizador atravez da URL ({id}).


* ROTA '/products/id' USANDO O METODO DELETE:

    Essa rota deleta um produto específico fornecido pelo utilizador atravez da URL ({id}).

3.DADOS
*  TIPOS DE DADOS:
    
    É necessário ter atenção ao utilizar as rotas quanto aos tipos de dados. Segue abaixo um Modelo do banco de dados em 
    questão:
```class 
    Products(db.Model):
        __tablename__ = 'products'
        productkey = db.Column(db.Integer, primary_key=True)
        productsubcategorykey = db.Column(db.Integer, db.ForeignKey('subcategories.productsubcategorykey'))
        productsku = db.Column(db.String)
        productname = db.Column(db.String)
        modelname = db.Column(db.String)
        productdescription = db.Column(db.String)
        productcolor = db.Column(db.String)
        productsize = db.Column(db.String)
        productstyle = db.Column(db.String)
        productcost = db.Column(db.DECIMAL(precision=10, scale=2))
        productprice = db.Column(db.DECIMAL(precision=10, scale=2))```
