from .VeganMarket import *
from .market_exception import FatalErrorException


class Stock(VeganMarket):   
    
    def __init__(self, market):
        super().__init__(market)
        self._market_dict = {}
           
    def _load_from_store(self):
        return super()._load(self._market_dict)
    
    def _add_new_product(self, product, quantity):
        try:
            buy_price = float(input("Prezzo di acquisto: "))
            sell_price = float(input("Prezzo di vendita: "))
        except Exception as e:
            print(e)
            return None
        finally:
            if buy_price <= 0 or sell_price <= 0:
                print("Error! Buy or sell price are not correct! Product has not be stored")
                return None
            else:
                self._market_dict["products"][product] = {"quantity":quantity, "buy":buy_price, "sell":sell_price}
            return [buy_price, sell_price]
        
    def add(self, product, quantity=1):
        product = product.lower()
        self._market_dict = self._load_from_store()    
        
        if len(self._market_dict) == 0:
            self._market_dict = super()._create_store()
        
        assert type(quantity) is int, f"quantity must be int. Got {type(quantity)}"
        assert quantity >= 0, f"quantity must be a positive number. Got quantity={quantity}"        
        
        if product in self._market_dict["products"]:    
            self._market_dict["products"][product]["quantity"] += quantity
        elif not self._add_new_product(product, quantity):
            return None   
        super()._save_store(dict(self._market_dict))
            
        return { product: self._market_dict["products"][product] } 
    
    def is_in_store(self, product):
        self._market_dict = self._load_from_store()
        if len(self._market_dict) == 0:
            raise FatalErrorException(self._market_dict)
        
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False 
    
