#Controlling post and put request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example5.db'
db = SQLAlchemy(app)

def custom_escape_html(text):
    """
    Custom function to escape HTML tags from the input text.
    """
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&#39;",
        ">": "&gt;",
        "<": "&lt;",
    }
    return "".join(html_escape_table.get(c, c) for c in text)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)

    def escape_html_tags(self):
        for attr_name in self.__mapper__.columns.keys():
            if isinstance(getattr(self, attr_name), str):
                setattr(self, attr_name, custom_escape_html(getattr(self, attr_name)))

@db.event.listens_for(Product, 'before_insert')
@db.event.listens_for(Product, 'before_update')
def escape_html_tags(mapper, connection, target):
    target.escape_html_tags()

db.create_all()

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Product, methods=['GET', 'POST', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
