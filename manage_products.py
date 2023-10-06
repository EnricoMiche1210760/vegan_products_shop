from market import Stock, Sell

def _sell_product(vegan_market : Sell, product_info, cart):
    
    product = product_info[0]
    quantity = product_info[1]
    
    try:
        if vegan_market.is_in_store(product):
            try:
                get_product = vegan_market.get(product, quantity)
                if get_product is not None:
                    if product not in cart:
                        cart[product] = get_product.copy()
                    else:
                        cart[product]["quantity"] += quantity
                print(cart)
            except ValueError as e:
                print(e)
    except Exception as e:
        print(e)
    else:
        print( "Errore! Prodotto non presente in negozio!")  

def get_product_info():
    product = input("Nome del prodotto: ")
    try:
        quantity = int(input("Quantità: "))
    except ValueError as e:
        print(e)
        return None
    return [product, quantity]


def add_product_to_store(vegan_market : Stock):
    product_info = get_product_info()
    if not product_info:
        return "Impossibile inserire la quantità desiderata."
    product = product_info[0]
    quantity = product_info[1]
    
    try:
        vegan_market.add(product, quantity)
    except Exception as e:
        try:
            buy_price = float(input("Prezzo di acquisto: "))
            sell_price = float(input("Prezzo di vendita: "))
            vegan_market.add(product, quantity, buy_price, sell_price)
        except ValueError as error:
            print(error)
            return "Impossibile aggiungere il prodotto"
    
    feedback_string = f"AGGIUNTO: {quantity} X {product}"        
    return feedback_string

def sell_products(cart : Sell): 
    buy_list = {}
    while 1:
        product_info = get_product_info()
        if not product_info:
            print( "Impossibile inserire la quantità desiderata.")
        else:
            _sell_product(cart, product_info, buy_list)

        buy_more = input("Aggiungere un altro prodotto ? (si/no) ")
        if buy_more.lower() == "si" or buy_more.lower() == "sì":
            continue
        else:
            break 
    return cart.get_bill(buy_list)
      
        