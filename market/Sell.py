from .VeganShop import *
from .exceptions import EmptyShopException

class Sell(VeganShop):
    
    def __init__(self, market):
        '''
        market (str): file json contenente tutti i prodotti presenti nel market
        '''
        super().__init__(market)
        self._market_dict = {}
        self._gross_profit = 0
        self._net_profit = 0
        
    def _load_from_store(self):
        '''
        ottiene il dizionario dal file json passato come parametro in __init__
        '''
        return super()._load(self._market_dict)
    
    def _save_store(self):
        '''
        salva il dizionario nel file json passato come parametro in __init__
        '''
        super()._save_store(self._market_dict)        
    
    def _load_profits_from_store(self):
        '''
        carica i profitti (lordo e netto)
        '''
        self._gross_profit = self._market_dict["profits"]["gross"] 
        self._net_profit = self._market_dict["profits"]["net"]
    
    def _update_profits(self, product, sell_quantity):
        '''
        aggiorna i profitti (lordo e netto) dopo una vendita
        product (str): prodotto venduto
        sell_quantity (int): quantità venduta di prodotto 
        '''
        sell_price = self._market_dict["products"][product]["sell"]*sell_quantity
        buy_price = self._market_dict["products"][product]["buy"]*sell_quantity
        
        self._gross_profit += sell_price
        self._net_profit += (sell_price - buy_price)
        
        self._market_dict["profits"]["gross"] = round(self._gross_profit, 2)
        self._market_dict["profits"]["net"] = round(self._net_profit, 2)
        
    def is_in_store(self, product):
        '''
        controlla se un prodotto è già presente in negozio
        product (str): prodotto da cercare
        Se non riesce a caricare il dizionario con i prodotti genera EmptyShopException
        '''
        self._market_dict = self._load_from_store()
        if len(self._market_dict) == 0 or len(self._market_dict["products"]) == 0:
            raise EmptyShopException(self._market_dict)
        
        if product.lower() in self._market_dict["products"].keys():
            return True
        return False 
    
    def get(self, product, quantity):
        '''
        funzione che gestisce la vendita di un prodotto da negozio.
        Restituisce un dizionario contentente il prodotto richiesto, la quantità richiesta e il prezzo del singolo prodotto.
        Se non riesce a caricare il dizionario con i prodotti genera EmptyShopException
        product (str): prodotto da vendere
        quantity (int): quantità di prodotto da vendere
        '''
        self._market_dict = self._load_from_store()
       
        if len(self._market_dict) == 0 or len(self._market_dict["products"]) == 0:
            raise EmptyShopException(self._market_dict)
        
        if type(quantity) is not int:
            raise ValueError( f"La quantità deve essere di tipo int. Ricevuto {type(quantity)}")
        if quantity < 0: 
            raise ValueError(f"La quantità deve essere un numero negativo. Ricevuto quantity={quantity}")   
        
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
        '''
        registra la vendita degli articoli e la stampa a video
        cart (dict): carrello della spesa
        '''
        total = 0
        bill = "VENDITA REGISTRATA\n"
        for product in cart.keys():
            bill += f"{cart[product]['quantity']} X {product}: €{cart[product]['sell']:.2f}\n"
            total += (cart[product]['sell']*cart[product]['quantity'])
        bill += f"Totale: €{total:.2f}\n"
        return bill
