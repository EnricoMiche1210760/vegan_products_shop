from .VeganMarket import *
from .market_exception import FatalErrorException

class Sell(VeganMarket):
    
    def __init__(self, market):
        super().__init__(market)
        self._market_dict = {}
        self._gross_profit = 0
        self._net_profit = 0
        
    def _load_from_store(self):
        return super()._load(self._market_dict)
    
    def _save_store(self):
        super()._save_store(self._market_dict)        
    
    def _load_profits_from_store(self):
        self._gross_profit = self._market_dict["profits"]["gross"] 
        self._net_profit = self._market_dict["profits"]["net"]
    
    def _update_profits(self, product, quantity):
        sell_price = self._market_dict["products"][product]["sell"]*quantity
        buy_price = self._market_dict["products"][product]["buy"]*quantity
        
        self._gross_profit += sell_price
        self._net_profit += (sell_price - buy_price)
        
        self._market_dict["profits"]["gross"] = round(self._gross_profit, 2)
        self._market_dict["profits"]["net"] = round(self._net_profit, 2)
        
    def is_in_store(self, product):
        
        self._market_dict = self._load_from_store()
        if len(self._market_dict) == 0:
            raise FatalErrorException(self._market_dict)
        
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False 
    
    def get(self, product, quantity):
        self._market_dict = self._load_from_store()
       
        if len(self._market_dict) == 0:
            raise FatalErrorException(self._market_dict)
        
        self._load_profits_from_store()
            
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
        total = 0
        bill = "VENDITA REGISTRATA\n"
        for product in cart.keys():
            bill += f"{cart[product]['quantity']} X {product}: €{cart[product]['sell']}\n"
            total += (cart[product]['sell']*cart[product]['quantity'])
        bill += f"Totale: €{total:.2f}"
        return bill
