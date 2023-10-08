from flask import Flask, render_template
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def index():
        return render_template("index.jinja")
    from .api import search_products
    app.register_blueprint(search_products.bp)

    return app
