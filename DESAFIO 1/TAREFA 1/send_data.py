import csv

from headers import dados
from models import *


# HACKATHON SANTO MAIO 2023
# DESAFIO 1, EXERCÍCIO 2
# CANDIDATO: TIAGO SOUZA PAIVA

# Propósito desse código é enviar os dados do arquivo .csv para o banco de dados.

calendar = dados['calendar']
customers = dados['customers']
categories = dados['categories']
subcategories = dados['subcategories']
products = dados['products']
returns = dados['returns']
sales_2015 = dados['sales_2015']
sales_2016 = dados['sales_2016']
sales_2017 = dados['sales_2017']
territories = dados['territories']


def envia_dados(dados):
    """Essa função deve abrir um arquivo .csv, e com auxilio de um laço enviar os dados para o banco de dados"""
    with open(dados, 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)
        for row in csv_data:
            # Esses if's estão aqui para enviar os dados que estão no laço para a Table correta.
            if dados == calendar:
                linha = Calendar(date=row[0])
                session.add(linha)
                session.commit()
            elif dados == categories:
                linha = Categories(
                    productcategorykey=row[0],
                    categoryname=row[1]
                )
                session.add(linha)
                session.commit()
            elif dados == customers:
                linha = Customers(
                    customerkey=row[0],
                    prefix=row[1],
                    firstname=row[2],
                    lastname=row[3],
                    birthdate=row[4],
                    maritalstatus=row[5],
                    gender=row[6],
                    emailaddress=row[7],
                    annualincome=row[8],
                    totalchildren=row[9],
                    educationlevel=row[10],
                    occupation=row[11]
                )
                session.add(linha)
                session.commit()
            elif dados == subcategories:
                linha = SubCategories(
                    productsubcategorykey=row[0],
                    subcategoryname=row[1],
                    productcategorykey=row[2]
                )
                session.add(linha)
                session.commit()
            elif dados == products:
                linha = Products(
                    productkey=row[0],
                    productsubcategorykey=row[1],
                    productsku=row[2],
                    productname=row[3],
                    modelname=row[4],
                    productdescription=row[5],
                    productcolor=row[6],
                    productsize=row[7],
                    productstyle=row[8],
                    productcost=row[9],
                    productprice=row[10]
                )
                session.add(linha)
                session.commit()
            elif dados == territories:
                linha = Territories(
                    salesterritorykey=row[0],
                    region=row[1],
                    country=row[2],
                    continent=row[3]
                )
                session.add(linha)
                session.commit()
            else:
                linha = Sales(
                    orderdate=row[0],
                    stockdate=row[1],
                    ordernumber=row[2],
                    productkey=row[3],
                    customerkey=row[4],
                    territorykey=row[5],
                    orderlineitem=row[6],
                    orderquantity=row[7],
                )
                session.add(linha)
                session.commit()


if __name__ == '__main__':
    envia_dados(territories)
    envia_dados(sales_2015)
    envia_dados(sales_2016)
    envia_dados(sales_2017)

