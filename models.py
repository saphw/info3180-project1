from this import d
from . import db

#title, number of bedrooms, number of bathrooms,location and price. property id
class propertyData(db.Model):
   
    propertyid= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(100))
    description= db.Column(db.String(1000))
    bedrooms= db.Column(db.Integer)
    bathrooms= db.Column(db.Integer)
    location= db.Column(db.String(100))
    price= db.Column(db.Integer)
    type=db.Column(db.String(9))
    photo = db.Column(db.String(100))


    def __init__(self, title, description, bedrooms, bathrooms, location, price,type, fileName):
        self.title= title
        self.description= description
        self.bedrooms=bedrooms
        self.bathrooms=bathrooms
        self.location=location
        self.price= price
        self.type= type
        self.image= fileName

    
    def __repr__(self):
        return '<Property %r>' % self.propertyid
