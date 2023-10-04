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
        
        #if len(self._market_dict) == 0:
        #    raise FatalError
        
        assert type(quantity) is int, f"quantity must be int. Got {type(quantity)}"
        assert quantity >= 0, f"quantity must be a positive number. Got quantity={quantity}"        
                
        if not price:
            self._market_dict["products"][product]["quantity"] += quantity

        elif price[0] <= 0 or price[1] <= 0:
            print("Error! Buy or sell price are not correct! Product has not be stored")
            return None
        else:
            self._market_dict["products"][product] = {"quantity":quantity, "buy":price[0], "sell":price[1]}
        
        super()._save_store(self._market_dict)
            
        return { product: self._market_dict["products"][product] } 
    
    def is_in_store(self, product):
        self._market_dict = self._load_from_store()         
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False
    
