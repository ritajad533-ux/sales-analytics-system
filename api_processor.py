import requests

def fetch_all_products():
    """Fetches product data from DummyJSON API."""
    try:
        response = requests.get("https://dummyjson.com/products?limit=100")
        if response.status_code == 200:
            return response.json().get('products', [])
    except Exception as e:
        print(f"API Error: {e}")
    return []

def create_product_mapping(api_products):
    """Creates a mapping of ProductID to product details."""
    # Note: Assignment requires mapping IDs like P101 to API ID 1
    mapping = {}
    for product in api_products:
        # Simple mapping logic: P101 -> 1, P102 -> 2
        mapped_id = f"P{100 + product['id']}"
        mapping[mapped_id] = {
            "API_Category": product.get("category"),
            "API_Brand": product.get("brand"),
            "API_Rating": product.get("rating")
        }
    return mapping