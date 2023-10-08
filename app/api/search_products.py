from flask import (Blueprint, request, jsonify)

bp = Blueprint('api', __name__, url_prefix="/api")


@bp.post("/")
def post_product():
    try:
        data = request.json
        product_name = data.get('product')

        from .get_product import get_product, get_test
        result = get_product(product_name)

        if not result["results"]:
            raise Exception("Mensaje de error personalizado")
        return jsonify(result["results"])
    except Exception as e:
        error_data = {"error": str(e)}
        return jsonify(error_data), 500
