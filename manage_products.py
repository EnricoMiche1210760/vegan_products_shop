from market import VeganMarket

def get_product_info():
    product = input("Nome del prodotto: ")
    try:
        quantity = int(input("Quantità: "))
    except ValueError as e:
        print(e)
        return None
    return [product, quantity]


def add_product(vegan_market : VeganMarket):
    product_info = get_product_info()
    if not product_info:
        return "Impossibile inserire la quantità desiderata."
    product = product_info[0]
    quantity = product_info[1]
    
    
    feedback_str = f"AGGIUNTO: {quantity} X {product}"
    if vegan_market.is_in_store(product):
        if vegan_market.add(product, quantity):
            return feedback_str
    try:
        buy_price = float(input("Prezzo di acquisto: "))
        sell_price = float(input("Prezzo di vendita: "))
    except Exception as e:
        print(e)
        return "Il prezzo inserito non è corretto"
    
    if vegan_market.add(product, quantity, (buy_price, sell_price)):
        return feedback_str
    return "Impossibile aggiungere il prodotto"


def sell_product(vegan_market : VeganMarket):
    cart = {}
    while 1:
        product_info = get_product_info()
        if not product_info:
            return "Impossibile inserire la quantità desiderata."
        product = product_info[0]
        quantity = product_info[1]
        
        if not vegan_market.is_in_store(product):
            print( "Errore! Prodotto non presente in magazzino!")
        try:
            get_product = vegan_market.get(product, quantity)
            print(get_product)
            if get_product is not None:
                cart[product] = get_product.copy()
            print (cart)
        except ValueError as e:
            print(e)
        finally:
            buy_more = input("Aggiungere un altro prodotto ? (si/no) ")
            if buy_more.lower() == "si" or buy_more.lower() == "sì":
                continue
            else:
                break     