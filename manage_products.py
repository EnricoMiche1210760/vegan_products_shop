from market import Stock, Sell
from market.exceptions import ProductNotFoundException, EmptyShopException
def _sell_product(vegan_shop : Sell, product_info, cart):
    '''
    aggiunge al carrello della spesa un prodotto se disponibile
    vegan_shop (Sell): oggetto della classe Sell contentente i prodotti disponibili in negozio
    product_info (list): lista composta da prodotto e quantità richiesti
    cart (dict): dizionario contentente i prodotti da vendere
    '''
    product = product_info[0]
    quantity = product_info[1]
    
    try:
        if vegan_shop.is_in_store(product):
            try:
                get_product = vegan_shop.get(product, quantity)
                if get_product is not None:
                    if product not in cart:
                        cart[product] = get_product.copy()
                    else:
                        cart[product]["quantity"] += quantity
                    return "added"
            except ValueError as e:
                print(e)
                return "not added"
        else:
            print( "Mi dispiace! Il prodotto non è presente in negozio!")  
    except EmptyShopException as e:
        print(e)
        return "void"
    except Exception as e:
        return "not added"
    return "not added"
    
def get_product_info():
    '''
    richiede prodotto e quantità tramite shell
    '''
    product = input("Nome del prodotto: ")
    try:
        quantity = int(input("Quantità: "))
    except ValueError as e:
        print(e)
        return None
    return [product, quantity]


def add_product_to_store(vegan_shop : Stock):
    '''
    aggiunge al magazzino del negozio i prodotti passati come input da shell e
    restituisce un feedback sulla riuscita dell'operazione
    vegan_shop (Stock): stock di un negozio
    '''
    product_info = get_product_info()
    if not product_info:
        return "Impossibile inserire la quantità desiderata."
    product = product_info[0]
    quantity = product_info[1]
    
    try:
        vegan_shop.add(product, quantity)
    except ValueError as e:
        return e
    except ProductNotFoundException as e:
        try:
            buy_price = float(input("Prezzo di acquisto: "))
            sell_price = float(input("Prezzo di vendita: "))
            vegan_shop.add(product, quantity, buy_price, sell_price)
        except ValueError as error:
            print(error)
            return "Impossibile aggiungere il prodotto"
    
    feedback_string = f"AGGIUNTO: {quantity} X {product}\n"        
    return feedback_string

def sell_products(cart : Sell): 
    '''
    aggiunge al carrello i prodotti passati come input da shell e
    restituisce la fattura
    cart (Sell): carrello della spesa
    '''
    buy_list = {}
    while 1:
        product_info = get_product_info()
        if not product_info:
            print( "Impossibile inserire la quantità desiderata.")
        else:
           if _sell_product(cart, product_info, buy_list) == "void":
            break
        buy_more = input("Aggiungere un altro prodotto ? (si/no) ")
        if buy_more.lower() == "si" or buy_more.lower() == "sì":
            continue
        else:
            break 
    if len(buy_list) == 0:
        return "\n" 
    return cart.get_bill(buy_list)
      
        