from market import Stock, Sell
from market.exceptions import ProductNotFoundException, EmptyShopException
def _sell_product(vegan_shop : Sell, product_info, cart):
    '''
    Add to shopping cart a product if available.
    vegan_shop (Sell): Sell object containing the products available
    product_info (list): list with product name and quantity required
    cart (dict): dictionary continaing products to be sold
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
    
def get_product_info(product=""):
    '''
    Get product and quantity from shell
    '''
    #feedback "quantity"
    if not product:
        product = input("Nome del prodotto: ")
    try:
        quantity = int(input("Quantità: "))
        if quantity < 0:
            raise ValueError()
    except ValueError as e:
        print("La quantità deve essere un numero intero maggiore di zero")
        return [product, None]
    return [product, quantity]


def add_product_to_store(vegan_shop : Stock):
    '''
    Add to store products passed by input from shell ad return a feedback
    whether the operation was successfully or not
    vegan_shop (Stock): stock of the vegan shop
    '''
    product_info = get_product_info()
    while not product_info[1]:
        #print( "Impossibile inserire la quantità desiderata.")
        product_info = get_product_info(product_info[0])
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
        except ValueError as error:
            print("Prezzo mancante o errato!")
            return "Impossibile aggiungere il prodotto"
        try:
            vegan_shop.add(product, quantity, buy_price, sell_price)
        except ValueError as error:
            print(error)
            return "Impossibile aggiungere il prodotto"
    
    feedback_string = f"AGGIUNTO: {quantity} X {product}\n"        
    return feedback_string

def sell_products(cart : Sell): 
    '''
    Add to cart products passed by input from shell ad return the bill
    cart (Sell): shopping cart
    '''
    buy_list = {}
    while 1:
        product_info = get_product_info()
        #feedback "quantity"
        while not product_info[1]:
            #print( "Impossibile inserire la quantità desiderata.")
            product_info = get_product_info(product_info[0])
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
      
        