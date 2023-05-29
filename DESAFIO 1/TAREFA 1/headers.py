import csv


# FINALIDADE DESSE CÓDIGO É MOSTRAR TODOS OS VALORES DOS CABEÇARIOS DOS ARQUIVOS
# PARA FACILITAR CRIAÇÃO DO BANCO DE DADOS
dados = {
    'calendar': './data/AdventureWorks_Calendar.csv',
    'customers': './data/AdventureWorks_Customers.csv',
    'categories': './data/AdventureWorks_Product_Categories.csv',
    'subcategories': './data/AdventureWorks_Product_Subcategories.csv',
    'products': './data/AdventureWorks_Products.csv',
    'returns': './data/AdventureWorks_Returns.csv',
    'sales_2015': './data/AdventureWorks_Sales_2015.csv',
    'sales_2016': './data/AdventureWorks_Sales_2016.csv',
    'sales_2017': './data/AdventureWorks_Sales_2017.csv',
    'territories': './data/AdventureWorks_Territories.csv'
}

def mostra_cabecalho():
    """ Função para mostrar os cabeçalhos do arquivo csv"""
    for key, valor in dados.items():
        with open(valor) as data:
            reader = csv.reader(data)
            header_row = next(reader)
            print(key)
            for index, column_header in enumerate(header_row):
                print(index, column_header)
