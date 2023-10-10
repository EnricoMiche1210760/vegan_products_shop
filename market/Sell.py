from .VeganShop import *
from .exceptions import EmptyShopException

class Sell(VeganShop):
    
    def __init__(self, market):
        '''
        market (str): file json containing all product available in the shop
        '''
        super().__init__(market)
        self._market_dict = {}
        self._gross_profit = 0
        self._net_profit = 0
        
    def _load_from_store(self):
        '''
        Load the dictionary from json file passed as parameter in __init__
        '''
        return super()._load(self._market_dict)
    
    def _save_store(self):
        '''
        Save the dictionary from json file passed as parameter in __init__
        '''
        super()._save_store(self._market_dict)        
    
    def _load_profits_from_store(self):
        '''
        Load profits (gross and net)
        '''
        self._gross_profit = self._market_dict["profits"]["gross"] 
        self._net_profit = self._market_dict["profits"]["net"]
    
    def _update_profits(self, product, sell_quantity):
        '''
        Update profits (gross and net) after a sell
        product (str): sold product
        sell_quantity (int): product sold quantity  
        '''
        sell_price = self._market_dict["products"][product]["sell"]*sell_quantity
        buy_price = self._market_dict["products"][product]["buy"]*sell_quantity
        
        self._gross_profit += sell_price
        self._net_profit += (sell_price - buy_price)
        
        self._market_dict["profits"]["gross"] = round(self._gross_profit, 2)
        self._market_dict["profits"]["net"] = round(self._net_profit, 2)
        
    def is_in_store(self, product):
        '''
        Check if a product is already in store.
        If dictionary is empty or without products raise: EmptyShopException
        product (str): product to be found
        '''
        self._market_dict = self._load_from_store()
        if len(self._market_dict) == 0 or len(self._market_dict["products"]) == 0:
            raise EmptyShopException(self._market_dict)
        
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False 
    
    def get(self, product, quantity):
        '''
        Manage the sell of a product from the store.
        Return a dictionary containing the required product, with the required quantity and the price of the single product.
        If products cannot be loaded from dict, raise EmptyShopException
        product (str): product to be sold
        quantity (int): quantity of product to be sold
        '''
        self._market_dict = self._load_from_store()
       
        if len(self._market_dict) == 0 or len(self._market_dict["products"]) == 0:
            raise EmptyShopException(self._market_dict)
        
        if type(quantity) is not int:
            raise ValueError( f"La quantità deve essere di tipo int. Ricevuto {type(quantity)}")
        if quantity <= 0: 
            raise ValueError(f"La quantità deve essere un numero positivo. Ricevuto quantity={quantity}")   
        
        self._load_profits_from_store()
        
        product = product.lower()
        
        available_items = self._market_dict["products"][product]["quantity"]
        if quantity > available_items:
            print(f"La quantità di prodotto richiesta non è disponibile. Rimangono {available_items} {product}")
            return None
        
        required_product = self._market_dict["products"][product].copy()
        required_product["quantity"] = quantity
        required_product.pop("buy")
        
        self._market_dict["products"][product]["quantity"] -= quantity
        self._update_profits(product, quantity) 
        
        if product and self._market_dict["products"][product]["quantity"] == 0:
            self._market_dict["products"].pop(product)
        self._save_store()        
        
        return required_product    
    
    def get_bill(self, cart):
        '''
        Records the sell of some products and print to the shell
        cart (dict): shopping cart
        '''
        total = 0
        bill = "VENDITA REGISTRATA\n"
        for product in cart.keys():
            bill += f" - {cart[product]['quantity']} X {product}: €{cart[product]['sell']:.2f}\n"
            total += (cart[product]['sell']*cart[product]['quantity'])
        bill += f"Totale: €{total:.2f}\n"
        return bill
