from .VeganShop import *
from .exceptions import FatalErrorException, ProductNotFoundException


class Stock(VeganShop):   
    
    def __init__(self, market):
        '''
        market (str): file json contenente tutti i prodotti presenti nel market
        '''
        super().__init__(market)
        self._market_dict = {}
           
    def _load_from_store(self):
        '''
        ottiene il dizionario dal file json passato come parametro in __init__
        '''
        return super()._load(self._market_dict)
    
    def _add_new_product(self, product, quantity, buy_price, sell_price):
        '''
        aggiunge in negozio un nuovo prodotto, con quantità, prezzo di acquisto e di vendita
        product (str): prodotto da aggiungere al negozio
        quantity (int): quantità di prodotto 
        buy_price (float): prezzo di acquisto del prodotto
        sell_price (flaot): prezzo di vendita del prodotto
        '''
        self._market_dict["products"][product] = {"quantity":quantity, "buy":buy_price, "sell":sell_price}
        return [buy_price, sell_price]
        
    def add(self, product, quantity=1, buy_price=-1, sell_price=-1):
        '''
        aggiorna la quantità del prodotto in negozio. Se il prodotto non è presente e il prezzo non è specificato 
        produce l'eccezione: ProductNotFoundException
        product (str): prodotto da aggiungere al negozio
        quantity (int): quantità di prodotto 
        buy_price (float): prezzo di acquisto del prodotto
        sell_price (flaot): prezzo di vendita del prodotto
        '''
        product = product.lower()
        self._market_dict = self._load_from_store()    
        
        if len(self._market_dict) == 0:
            self._market_dict = super()._create_store()
        
        assert type(quantity) is int, f"La quantità deve essere di tipo int. Ricevuto {type(quantity)}"
        assert quantity >= 0, f"La quantità deve essere un numero negativo. Ricevuto quantity={quantity}"        
        
        if product in self._market_dict["products"]:    
            self._market_dict["products"][product]["quantity"] += quantity
            
        elif buy_price == -1 and sell_price == -1:
            raise ProductNotFoundException(product, self._market_dict)
        else: 
            self._add_new_product(product, quantity, buy_price, sell_price)
        
        super()._save_store(dict(self._market_dict))
            
        return { product: self._market_dict["products"][product] } 
    
    def is_in_store(self, product):
        '''
        controlla se un prodotto è già presente in negozio.
        Se non riesce a caricare il dizionario con i prodotti genera FatalErrorException
        product (str): prodotto da cercare
        '''
        self._market_dict = self._load_from_store()
        if len(self._market_dict) == 0:
            raise FatalErrorException(self._market_dict)
        
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False 
    
