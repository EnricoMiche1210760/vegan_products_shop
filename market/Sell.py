from .VeganMarket import *
from market_exception import FatalErrorException

class Sell(VeganMarket):
    
    def __init__(self, market):
        super().__init__(market)
        self._market_dir = {}
        self._gross_profit = 0
        self._net_profit = 0
    
    def _load_from_store(self):
        return super()._load(self._market_dict)
    
    def _save_store(self):
        super()._save_store()        
    
    def _update_profits(self, product, quantity):
        self._gross_profit += (self._market_dir["products"][product]["sell"]*quantity)
        self._net_profit = self._gross_profit - (self._market_dir["products"][product]["buy"]*quantity)
        self._market_dir["profits"]["gross"] = self._gross_profit
        self._market_dir["profits"]["net"] = self._net_profit
    
    def get(self, product, quantity):
        self._market_dir = self._load_from_store()

        if len(self._market_dict) == 0:
            raise FatalErrorException(self._market_dict)

        available_items = self._market_dict["products"][product]["quantity"]
        
        if quantity > available_items:
            print(f"La quantità di prodotto richiesta non è disponibile. Rimangono {available_items} {product}")
            return None
        
        required_product = self._market_dict["products"][product].copy()
        required_product["quantity"] = quantity
        required_product.pop("buy")
        
        self._market_dict["products"][product]["quantity"] -= quantity
        if product and self._market_dict["products"][product]["quantity"] == 0:
            self._market_dict["products"].pop(product)
        
        self._update_profits(product, quantity) 
        self._save_store()        
        
        return required_product    
    
    def get_bill(self, cart):
        total = 0
        bill = "VENDITA REGISTRATA\n"
        for product in cart.keys():
            bill += f"{cart[product]['quantity']} X {product}: {cart[product]['sell']}\n"
            total += cart[product]['sell']
        bill += f"Totale: {total}"
        return bill
        
    
    ''' 
    def __repr__(self):
        store_content = self._get_bill()
        if not store_content:
            return "Magazzino vuoto o inaccessibile."
        return store_content    '''