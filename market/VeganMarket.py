import json
from os import path

class VeganMarket():
    def __init__(self, market):
        '''
        market: file json contenente tutti i prodotti presenti nel market
        '''
        self._market = market
        self._gross_profit = 0
        self._net_profit = 0

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
                        
    def _update_store(self, market_products, product = "" ):
        if product and market_products["products"][product]["quantity"] == 0:
            market_products["products"].pop(product)
            
        with open(self._market, "w", encoding='utf-8') as mrkt:
                json.dump(market_products, mrkt, indent=6)
    
    def _is_store_available(self):
        if not path.isfile(self._market):
            return False
        return True
    
    def _show_store(self):
        if not self._is_store_available():
            print("Il contenuto del magazzino non è attualmente disponibile")
            return None
        
        with open(self._market, "r", encoding='utf-8') as mrkt:
            market_products = json.load(mrkt)
        products_table_info = "{:<20} {:<15} {:<15}\n".format("Prodotto","Quantità","Prezzo")
        
        for product in market_products["products"]:
            quantity = market_products["products"][product]["quantity"]
            sell_price = market_products["products"][product]["sell"]           
            products_table_info += "{:<20} {:<15} {:<15}\n".format(product, quantity, sell_price)
            
        return products_table_info
    
    def is_in_store(self, product):
        if not self._is_store_available():
            print("Il contenuto del magazzino non è attualmente disponibile")
            return False
        mrkt = open(self._market, "r", encoding='utf-8')
        market_dict = json.load(mrkt)
        mrkt.close()
        if product.lower() in market_dict["products"].keys():
            return True
        return False
        
    def add(self, product, quantity=1, price=()):
        if not self._is_store_available():
            self._create_store()
        product = product.lower()
        
        assert type(quantity) is int, f"quantity must be int. Got {type(quantity)}"
        assert quantity >= 0, f"quantity must be a positive number. Got quantity={quantity}"
        
        with open(self._market, "r", encoding='utf-8') as mrkt:
                market_products = json.load(mrkt)
        if not price:
            market_products["products"][product]["quantity"] += quantity
            self._update_store(market_products)
        elif price[0] <= 0 or price[1] <= 0:
            print("Error! Buy or sell price are not correct! Product has not be stored")
            return None
        else:
            market_products["products"][product] = {"quantity":quantity, "buy":price[0], "sell":price[1]}
            self._update_store(market_products)
            
        return { product: market_products["products"][product] }
    
    def get(self, product, quantity):
        if not self._is_store_available():
            print("Il contenuto del magazzino non è attualmente disponibile")
            return None
        with open(self._market, "r", encoding='utf-8') as mrkt:
                market_products = json.load(mrkt)
        available_items = market_products["products"][product]["quantity"]
        
        if quantity > available_items:
            print(f"La quantità di prodotto richiesta non è disponibile. Rimangono {available_items} {product}")
            return None
        print(market_products)
        required_product = market_products["products"][product].copy()
        required_product["quantity"] = quantity
        required_product.pop("buy")
        print(required_product)
        
        market_products["products"][product]["quantity"] -= quantity       
        self._update_store(market_products, product=product)
                
        return required_product      
    
    
    def sell(self, product):
        pass        
    def profits(self):
        pass

    def __repr__(self):
        store_content = self._show_store()
        if not store_content:
            return "Magazzino vuoto o inaccessibile."
        return store_content

'''
with open(self._market, "r", encoding='utf-8') as mrkt:
                market_dict = json.load(mrkt)
            self._gross_profit = market_dict["profits"]["gross"]
            self._net_profit = market_dict["profits"]["net"]
'''