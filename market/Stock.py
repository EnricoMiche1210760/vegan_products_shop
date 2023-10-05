from .VeganMarket import *
from .exceptions import FatalErrorException, ProductNotFoundException


class Stock(VeganMarket):   
    
    def __init__(self, market):
        super().__init__(market)
        self._market_dict = {}
           
    def _load_from_store(self):
        return super()._load(self._market_dict)
    
    def _add_new_product(self, product, quantity, buy_price, sell_price):
        self._market_dict["products"][product] = {"quantity":quantity, "buy":buy_price, "sell":sell_price}
        return [buy_price, sell_price]
        
    def add(self, product, quantity=1, buy_price=-1, sell_price=-1):
        product = product.lower()
        self._market_dict = self._load_from_store()    
        
        if len(self._market_dict) == 0:
            self._market_dict = super()._create_store()
        
        assert type(quantity) is int, f"quantity must be int. Got {type(quantity)}"
        assert quantity >= 0, f"quantity must be a positive number. Got quantity={quantity}"        
        
        if product in self._market_dict["products"]:    
            self._market_dict["products"][product]["quantity"] += quantity
            
        elif buy_price == -1 and sell_price == -1:
            raise ProductNotFoundException(product)
        else: 
            self._add_new_product(product, quantity, buy_price, sell_price)
        
        super()._save_store(dict(self._market_dict))
            
        return { product: self._market_dict["products"][product] } 
    
    def is_in_store(self, product):
        self._market_dict = self._load_from_store()
        if len(self._market_dict) == 0:
            raise FatalErrorException(self._market_dict)
        
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False 
    
