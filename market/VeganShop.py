import json
from os import path

class VeganShop():
    def __init__(self, market):
        '''
        market (str): file json contenente tutti i prodotti presenti nel market
        '''
        self._market = market
        assert path.splitext(self._market)[-1] == ".json", "Tipo di file non supportato. Utilizzare un file json"
        
    def _create_store(self):
        '''
        crea il file che deve contenere i dati del negozio
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
        salva il file con i dati del negozio
        market_dict (dict); dizionario con i dati del negozio
        '''
        with open(self._market, "w", encoding='utf-8') as mrkt:
                json.dump(market_dict, mrkt, indent=6)
        
    def _is_store_available(self):
        '''
        controlla se il file con i dati del negozio esiste
        '''
        if path.isfile(self._market):
            return True
        return False
    
    def _load(self, market_dict={}):
        '''
        carica i dati di negozio dal file e li restituisce in un dizionario
        market_dict (dict): dizionario
        '''
        if not self._is_store_available():
            return {}
        
        with open(self._market, "r", encoding='utf-8') as mrkt:
           market_dict = json.load(mrkt)
        return market_dict
    
    def _show_store(self):
        '''
        mostra il contenuto del negozio
        '''
        if not self._is_store_available():
            print("Il contenuto del negozio non è attualmente disponibile")
            return None
        
        products_table_info = "{:<20} {:<15} {:<15}\n".format("Prodotto","Quantità","Prezzo")
        
        market_dict = self._load()
        for product in market_dict["products"]:
            quantity = market_dict["products"][product]["quantity"]
            sell_price = market_dict["products"][product]["sell"]           
            products_table_info += "{:<20} {:<15} €{:<15.2f}\n".format(product, quantity, sell_price)
            
        return products_table_info 
       
    def __repr__(self):
        '''
        stampa i dati contenuti nel file json del negozio
        '''
        store_content = self._show_store()
        if not store_content:
            return "Negozio vuoto o inaccessibile.\n"
        return store_content + "\n"   
    
    def print_profits(self):
        '''
        stampa i profitti del negozio
        '''
        market_dict = self._load()
        if len(market_dict) == 0:
            print("Impossibile ottenere i profitti del negozio!\n")
            return
        print(f"Profitto: lordo=€{market_dict['profits']['gross']:.2f} netto=€{market_dict['profits']['net']:.2f}\n")
        return
       