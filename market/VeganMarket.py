import json
from os import path

class VeganMarket():
    def __init__(self, market):
        '''
        market: file json contenente tutti i prodotti presenti nel market
        '''
        self._market = market
        #self._market_dir = {}
        #self._gross_profit = 0
        #self._net_profit = 0

        assert path.splitext(self._market)[-1] == ".json", "Tipo di file non supportato. Utilizzare un file json"
        
    def _create_store(self):    
        market_dict = {"products": {}, 
                        "profits":{
                            "gross": self._gross_profit,
                            "net": self._net_profit
                        }
                        }
        with open(self._market, "w", encoding='utf-8') as mrkt:
            json.dump(market_dict, mrkt, indent=6)
    
    def _save_store(self, market_dict, product = ""):
        with open(self._market, "w", encoding='utf-8') as mrkt:
                json.dump(market_dict, mrkt, indent=6)
        
    def _is_store_available(self):
        if path.isfile(self._market):
            return True
        return False
    
    def _load(self, market_dict={}):
        if not self._is_store_available():
            return None
        
        with open(self._market, "r", encoding='utf-8') as mrkt:
           market_dict = json.load(mrkt)
        return market_dict
    
    def _show_store(self):
        if not self._is_store_available():
            print("Il contenuto del magazzino non è attualmente disponibile")
            return None
        
        products_table_info = "{:<20} {:<15} {:<15}\n".format("Prodotto","Quantità","Prezzo")
        
        market_dict = self._load()
        for product in market_dict["products"]:
            quantity = market_dict["products"][product]["quantity"]
            sell_price = market_dict["products"][product]["sell"]           
            products_table_info += "{:<20} {:<15} {:<15}\n".format(product, quantity, sell_price)
            
        return products_table_info 
       
    def __repr__(self):
        store_content = self._show_store()
        if not store_content:
            return "Magazzino vuoto o inaccessibile."
        return store_content    
        
        
    def _update_profits(self, product, quantity):
        self._gross_profit += (self._market_dir["products"][product]["sell"]*quantity)
        self._net_profit = self._gross_profit - (self._market_dir["products"][product]["buy"]*quantity)
        self._market_dir["profits"]["gross"] = self._gross_profit
        self._market_dir["profits"]["net"] = self._net_profit
        
  
    
'''   
    def is_in_store(self, product):
        if not self._is_store_available():
            print("Il contenuto del magazzino non è attualmente disponibile")
            return False
        
        if product.lower() in self._market_dir["products"].keys():
            return True
        return False
'''
'''
with open(self._market, "r", encoding='utf-8') as mrkt:
                market_dict = json.load(mrkt)
            self._gross_profit = market_dict["profits"]["gross"]
            self._net_profit = market_dict["profits"]["net"]
'''