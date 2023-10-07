from market import Stock, Sell

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
                print(cart)
            except ValueError as e:
                print(e)
        else:
            print( "Errore! Prodotto non presente in negozio!")  
    except Exception as e:
        print(e)
    
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
    except Exception as e:
        try:
            buy_price = float(input("Prezzo di acquisto: "))
            sell_price = float(input("Prezzo di vendita: "))
            vegan_shop.add(product, quantity, buy_price, sell_price)
        except ValueError as error:
            print(error)
            return "Impossibile aggiungere il prodotto"
    
    feedback_string = f"AGGIUNTO: {quantity} X {product}"        
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
            _sell_product(cart, product_info, buy_list)

        buy_more = input("Aggiungere un altro prodotto ? (si/no) ")
        if buy_more.lower() == "si" or buy_more.lower() == "sì":
            continue
        else:
            break 
    return cart.get_bill(buy_list)
      
        