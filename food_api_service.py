import requests



def request_info(product):
    if product.isdigit() and 12 <= len(product) <= 13: 
        url = f"https://world.openfoodfacts.org/api/v2/product/{product}.json"
        response = requests.get(url)
        data = response.json()
        prod = data.get("product")
        if prod is None:
            return {"error": "Product not found"}
        return prod
    else:
        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product}&search_simple=1&action=process&json=1"
        response = requests.get(url)
        data = response.json()
        products = data.get("products", [])
        if not products:
            return [{"error": "No products found"}]
        return products[:20]

    

