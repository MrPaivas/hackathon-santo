from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import sessionmaker, declarative_base

# String de conexão com o banco de dados
connection_string = "mysql+mysqlconnector://root:@localhost/adventureworks"
engine_db = create_engine(connection_string)

Base = declarative_base()


class Calendar(Base):
    __tablename__ = 'calendar'

    date = Column(String, primary_key=True)


class Categories(Base):
    __tablename__ = 'categories'

    productcategorykey = Column(Integer, primary_key=True)
    categoryname = Column(String)


class SubCategories(Base):
    __tablename__ = 'subcategories'

    productsubcategorykey = Column(Integer, primary_key=True)
    subcategoryname = Column(String)
    productcategorykey = Column(Integer, ForeignKey("categories.productcategorykey"))


class Customers(Base):
    __tablename__ = 'customers'

    customerkey = Column(Integer, primary_key=True)
    prefix = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    birthdate = Column(String)
    maritalstatus = Column(String)
    gender = Column(String)
    emailaddress = Column(String)
    annualincome = Column(String)
    totalchildren = Column(String)
    educationlevel = Column(String)
    occupation = Column(String)





class Products(Base):
    __tablename__ = 'products'

    productkey = Column(Integer, primary_key=True)
    productsubcategorykey = Column(Integer, ForeignKey('subcategories.productsubcategorykey'))
    productsku = Column(String)
    productname = Column(String)
    modelname = Column(String)
    productdescription = Column(String)
    productcolor = Column(String)
    productsize = Column(String)
    productstyle = Column(String)
    productcost = Column(DECIMAL(precision=10, scale=2))
    productprice = Column(DECIMAL(precision=10, scale=2))


class Sales(Base):
    __tablename__ = 'sales'

    salekey = Column(Integer, primary_key=True)
    orderdate = Column(Integer)
    stockdate = Column(String)
    ordernumber = Column(String)
    productkey = Column(Integer, ForeignKey('products.productkey'))
    customerkey = Column(Integer, ForeignKey('customers.customerkey'))
    territorykey = Column(Integer, ForeignKey('territories.salesterritorykey'))
    orderlineitem = Column(Integer)
    orderquantity = Column(Integer)



class Territories(Base):
    __tablename__ = 'territories'

    salesterritorykey = Column(Integer, primary_key=True)
    region = Column(String)
    country = Column(String)
    continent = Column(String)


Session = sessionmaker(bind=engine_db)
session = Session()