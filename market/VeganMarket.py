import json
from os import path

class VeganMarket():
    def __init__(self, market):
        '''
        market: file json contenente tutti i prodotti presenti nel market
        '''
        self._market = market
        assert path.splitext(self._market)[-1] == ".json", "Tipo di file non supportato. Utilizzare un file json"
        
    def _create_store(self):    
        market_dict = {"products": {}, 
                        "profits":{
                            "gross": 0,
                            "net": 0
                        }
                        }
        
        self._save_store(market_dict)
        return market_dict
    
    def _save_store(self, market_dict):
        with open(self._market, "w", encoding='utf-8') as mrkt:
                json.dump(market_dict, mrkt, indent=6)
        
    def _is_store_available(self):
        if path.isfile(self._market):
            return True
        return False
    
    def _load(self, market_dict={}):
        if not self._is_store_available():
            return {}
        
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
            products_table_info += "{:<20} {:<15} €{:<15.2f}\n".format(product, quantity, sell_price)
            
        return products_table_info 
       
    def __repr__(self):
        store_content = self._show_store()
        if not store_content:
            return "Magazzino vuoto o inaccessibile."
        return store_content    
    
    def print_profits(self):
        market_dict = self._load()
        if len(market_dict) == 0:
            print("Impossibile ottenere i profitti!")
            return
        print(f"Profitto: lordo=€{market_dict['profits']['gross']} netto=€{market_dict['profits']['net']}")
        return
       