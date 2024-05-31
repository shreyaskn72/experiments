#Controlling post and put request

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
import html

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example3.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)

db.create_all()

@db.event.listens_for(Product, 'before_insert')
@db.event.listens_for(Product, 'before_update')
def escape_html_tags(mapper, connection, target):
    target.name = html.escape(target.name)
    target.description = html.escape(target.description)

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Product, collection_name="product_details", methods=['GET', 'POST', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
