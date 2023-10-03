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
        
        if not path.isfile(self._market):
            market_dict = {"products": {}}
            
            with open(self._market, "w", encoding='utf-8') as mrkt:
                json.dump(market_dict, mrkt, indent=6)
        
    def is_in_store(self, product):
        try:
            mrkt = open(self._market, "r", encoding='utf-8')
        except FileNotFoundError as err:
            print("Il contenuto del magazzino non è attualmente disponibile")
            return False
        market_dict = json.load(mrkt)
        if product in market_dict.keys():
            return True
        return False
        
    def add(self, product, quantity=1, price=()):
        if not price:
            return
        else:
            #with open(self._market, "w+", encoding='utf-8') as mrkt:
            #    mmrkt
            return   
    def get(self, product):
        pass
    def sell(self, product):
        pass        
    def profits(self):
        pass


