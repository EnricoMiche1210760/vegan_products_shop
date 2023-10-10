from .VeganShop import *
from .exceptions import EmptyShopException, ProductNotFoundException


class Stock(VeganShop):   
    
    def __init__(self, market):
        '''
        market (str): file json containing all product available in the shop
        '''
        super().__init__(market)
        self._market_dict = {}
           
    def _load_from_store(self):
        '''
        Load the dictionary from json file passed as parameter in __init__
        '''
        return super()._load(self._market_dict)
    
    def _add_new_product(self, product, quantity, buy_price, sell_price):
        '''
        Add a new product in the store, with quantity, buy price and sell price
        product (str): product to be added in the store
        quantity (int): quantity of product
        buy_price (float): product buy price
        sell_price (flaot):  product sell price
        '''
        if buy_price < 0 or sell_price < 0:
            raise ValueError("Digitato un prezzo errato!")
        if sell_price < buy_price:
            raise ValueError("Errore! Prezzo di vendita più basso del prezzo di acquisto")
        self._market_dict["products"][product] = {"quantity":quantity, "buy":round(buy_price, 2), "sell":round(sell_price, 2)}
        return [buy_price, sell_price]
        
    def add(self, product, quantity=1, buy_price=None, sell_price=None):
        '''
        Update product quantity on the store. If a new product is inserted and price is not given 
        raise: ProductNotFoundException
        product (str): product to be added in the store
        quantity (int): quantity of product
        buy_price (float): product buy price
        sell_price (flaot):  product sell price
        '''
        product = product.lower()
        self._market_dict = self._load_from_store()    
        
        if len(self._market_dict) == 0:
            self._market_dict = super()._create_store()
        
        if type(quantity) is not int:
            raise ValueError( f"La quantità deve essere di tipo int. Ricevuto {type(quantity)}")
        if quantity <= 0: 
            raise ValueError(f"La quantità deve essere un numero positivo. Ricevuto quantity={quantity}")        
        
        if product in self._market_dict["products"]:    
            self._market_dict["products"][product]["quantity"] += quantity
            
        elif not buy_price or not sell_price:
            raise ProductNotFoundException(product, self._market_dict)
        else: 
            self._add_new_product(product, quantity, buy_price, sell_price)
        
        super()._save_store(dict(self._market_dict))
            
        return { product: self._market_dict["products"][product] } 
    
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
    
