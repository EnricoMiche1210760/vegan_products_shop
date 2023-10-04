from .VeganMarket import *

class Sell(VeganMarket):
    
    def __init__(self, market):
        super().__init__(market)
        self._market_dir = {}
        self._gross_profit = 0
        self._net_profit = 0
    
    def _load_from_store(self):
        return super()._load(self._market_dict)
        
    def get(self, product, quantity):
        self._market_dir = self._load_from_store()

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
        super()._update_profits(product, quantity) 
            
        super()._save_store()        
        
        return required_product    