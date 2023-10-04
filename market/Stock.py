from .VeganMarket import *

class Stock(VeganMarket):   
    
    def __init__(self, market):
        super().__init__(market)
        self._market_dict = {}
           
    def _load_from_store(self):
        return super()._load(self._market_dict)
        
    def add(self, product, quantity=1, price=()):
        product = product.lower()
        self._market_dict = self._load_from_store()    
        #print(self._market_dict)
        print("giacomino")
        
        assert type(quantity) is int, f"quantity must be int. Got {type(quantity)}"
        assert quantity >= 0, f"quantity must be a positive number. Got quantity={quantity}"
        
        if not price:
            self._market_dict["products"][product]["quantity"] += quantity
            super()._save_store(self._market_dict)
        elif price[0] <= 0 or price[1] <= 0:
            print("Error! Buy or sell price are not correct! Product has not be stored")
            return None
        else:
            self._market_dict["products"][product] = {"quantity":quantity, "buy":price[0], "sell":price[1]}
            super()._save_store(self._market_dict)
            
        return { product: self._market_dict["products"][product] }
    
    
    
    def get(self, product, quantity):
        if not super()._is_store_available():
            print("Il contenuto del magazzino non è attualmente disponibile")
            return None

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
    
    def is_in_store(self, product):
        self._market_dict = self._load_from_store()         
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False
    
    def sell(self, product):
        pass        
    def profits(self):
        pass
