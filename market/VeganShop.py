import json
from os import path

class VeganShop():
    def __init__(self, market):
        '''
        market (str): file json containing all product available in the shop
        '''
        self._market = market
        assert path.splitext(self._market)[-1] == ".json", "Tipo di file non supportato. Utilizzare un file json"
        
    def _create_store(self):
        '''
        Create the file which has to contain store data
        '''
        market_dict = {"products": {}, 
                        "profits":{
                            "gross": 0,
                            "net": 0
                        }
                        }
        
        self._save_store(market_dict)
        return market_dict
    
    def _save_store(self, market_dict):
        '''
        Save file with store content.
        market_dict (dict); dictionary with store data
        '''
        with open(self._market, "w", encoding='utf-8') as mrkt:
                json.dump(market_dict, mrkt, indent=6)
        
    def _is_store_available(self):
        '''
        Check if store data file exists
        '''
        if path.isfile(self._market):
            return True
        return False
    
    def _load(self, market_dict={}):
        '''
        Load shop data from file and return a dictionary with the content
        market_dict (dict): dictionary
        '''
        if not self._is_store_available():
            return {}
        
        with open(self._market, "r", encoding='utf-8') as mrkt:
           market_dict = json.load(mrkt)
        return market_dict
    
    def _show_store(self):
        '''
        Show store content
        '''
        if not self._is_store_available():
            print("Il contenuto del negozio non è attualmente disponibile")
            return None
        
        products_table_info = "PRODOTTO\tQUANTITA'\tPREZZO\n"
        
        market_dict = self._load()
        for product in market_dict["products"]:
            quantity = market_dict["products"][product]["quantity"]
            sell_price = market_dict["products"][product]["sell"]           
            products_table_info += f"{product}\t{quantity}\t€{sell_price:.2f}\n"
            
        return products_table_info 
       
    def __repr__(self):
        '''
        Print json shop data content
        '''
        store_content = self._show_store()
        if not store_content:
            return "Negozio vuoto o inaccessibile.\n"
        return store_content + "\n"   
    
    def print_profits(self):
        '''
        Print shop profits
        '''
        market_dict = self._load()
        if len(market_dict) == 0:
            print("Impossibile ottenere i profitti del negozio!\n")
            return
        print(f"Profitto: lordo=€{market_dict['profits']['gross']:.2f} netto=€{market_dict['profits']['net']:.2f}\n")
        return
       