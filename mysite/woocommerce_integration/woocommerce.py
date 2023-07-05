import requests

def get_product_list():
    url = 'http://127.0.0.1:8000/myapp/wp-json/wc/v3/products' 
    consumer_key = 'ck_3a81c4701d2c9b8875092d1a3f53814bacf3b90f'  
    consumer_secret = 'cs_aa8c2f1b0d48cc4bb29a55531aa2d3bf961a6d43'  
    
    response = requests.get(url, auth=(consumer_key, consumer_secret))
    
    if response.status_code == 200:
        products = response.json()
        return products
    else:
        return None