#Not tested correctly


from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
import html

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
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

def custom_unescape_html(text):
    """
    Custom function to unescape HTML tags from the input text.
    """
    return html.unescape(text)

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

def postprocessor(result):
    """
    Postprocessor to escape HTML tags from the response.
    """
    if 'objects' in result:
        for obj in result['objects']:
            for key, value in obj.items():
                if isinstance(value, str):
                    obj[key] = custom_escape_html(value)
    return result

def preprocess_post(data=None, **kwargs):
    """
    Preprocessor to escape HTML tags from the request payload for POST requests.
    """
    if data:
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = custom_escape_html(value)
    return data

def preprocess_put(data=None, **kwargs):
    """
    Preprocessor to escape HTML tags from the request payload for PUT requests.
    """
    if data:
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = custom_escape_html(value)
    return data

manager.create_api(Product, methods=['GET', 'POST', 'PUT', 'DELETE'], url_prefix='/product_details', preprocessors={
    'POST': [preprocess_post],
    'PUT_SINGLE': [preprocess_put],
    'PUT_MANY': [preprocess_put]
}, postprocessors={
    'GET_MANY': [postprocessor],
    'GET_SINGLE': [postprocessor],
    'POST': [postprocessor],
    'PUT_SINGLE': [postprocessor],
    'PUT_MANY': [postprocessor],
})

if __name__ == '__main__':
    app.run(debug=True)
