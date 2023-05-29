from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Calendar(db.Model):
    __tablename__ = 'calendar'
    date = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return 'Calendar %r' % self.date


class Categories(db.Model):
    __tablename__ = 'categories'
    productcategorykey = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String)

    def __repr__(self):
        return 'Categories %r' % self.productcategorykey


class SubCategories(db.Model):
    __tablename__ = 'subcategories'
    productsubcategorykey = db.Column(db.Integer, primary_key=True)
    subcategoryname = db.Column(db.String)
    productcategorykey = db.Column(db.Integer, db.ForeignKey("categories.productcategorykey"))

    def __repr__(self):
        return 'SubCategories %r' % self.productsubcategorykey


class Customers(db.Model):
    __tablename__ = 'customers'
    customerkey = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    birthdate = db.Column(db.String)
    maritalstatus = db.Column(db.String)
    gender = db.Column(db.String)
    emailaddress = db.Column(db.String)
    annualincome = db.Column(db.String)
    totalchildren = db.Column(db.String)
    educationlevel = db.Column(db.String)
    occupation = db.Column(db.String)

    def __repr__(self):
        return 'Customers %r' % self.customerkey


class Products(db.Model):
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
    productprice = db.Column(db.DECIMAL(precision=10, scale=2))

    def __repr__(self):
        return 'Products %r' % self.productkey


class Sales(db.Model):
    __tablename__ = 'sales'
    salekey = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.Integer)
    stockdate = db.Column(db.String)
    ordernumber = db.Column(db.String)
    productkey = db.Column(db.Integer, db.ForeignKey('products.productkey'))
    customerkey = db.Column(db.Integer, db.ForeignKey('customers.customerkey'))
    territorykey = db.Column(db.Integer, db.ForeignKey('territories.salesterritorykey'))
    orderlineitem = db.Column(db.Integer)
    orderquantity = db.Column(db.Integer)

    def __repr__(self):
        return 'Sales %r' % self.salekey


class Territories(db.Model):
    __tablename__ = 'territories'
    salesterritorykey = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String)
    country = db.Column(db.String)
    continent = db.Column(db.String)

    def __repr__(self):
        return 'Territories %r' % self.salesterritorykey