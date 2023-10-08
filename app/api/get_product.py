def get_test(x_rapidAPI_key, api_key, product_name):
    data = {
        "products": [{"id": 1, "name": "Apple"}, {"id": 2, "name": "Samsung"}],
        "msg": "Datos de ejemplo con una función de test",
        "params": {
            "x-rapidAPI-key": x_rapidAPI_key,
            "api_key": api_key,
            "product": product_name
        }
    }
    return data


def get_product(product_name):
    import http.client
    import ssl
    import json
    from dotenv import load_dotenv
    import os

    load_dotenv()

    x_rapidAPI_key = os.getenv("X-RapidAPI-Key")
    api_key = os.getenv("API_KEY")

    conn = http.client.HTTPSConnection(
        "amazon_data_extractor.p.rapidapi.com", context=ssl._create_unverified_context())
    headers = {
        'X-RapidAPI-Key': x_rapidAPI_key,
        'X-RapidAPI-Host': "amazon_data_extractor.p.rapidapi.com"
    }
    conn.request(
        "GET", f"/search/{product_name}?api_key={api_key}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    result_json = json.loads(data.decode("utf-8"))
    return result_json
