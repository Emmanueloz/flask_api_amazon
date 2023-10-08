from flask import (Blueprint, request, jsonify)

bp = Blueprint('api', __name__, url_prefix="/api")


@bp.post("/")
def post_product():
    try:
        data = request.json
        product_name = data.get('product')

        from .get_product import get_product
        result = get_product(product_name)

        if not result["results"]:
            raise Exception("Mensaje de error personalizado")
        return jsonify(result["results"])
    except Exception as e:
        error_data = {"error": str(e)}
        return jsonify(error_data), 500


@bp.route("/test")
def route_test():
    from .get_product import get_test

    return jsonify(get_test())
