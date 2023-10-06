from market import Stock, Sell, VeganMarket
from manage_products import add_product_to_store, sell_products

HELPER_STR="""
I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al negozio
elenca: elenca i prodotto in negozio
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma
"""

help(Sell)

if __name__ == "__main__":   
    while 1:
        command = input("Inserisci un comando: ")
        if command == "aiuto":
            print(HELPER_STR)
        elif command == "aggiungi":
            stock = Stock("vegan_market.json")
            print(stock._market)
            print(add_product_to_store(stock))
            
        elif command == "elenca":
            vegan_market = VeganMarket("vegan_market.json")
            print(vegan_market)
            
        elif command == "vendita":
            cart = Sell("vegan_market.json") 
            print(sell_products(cart))
            
        elif command == "profitti":
            profits = VeganMarket("vegan_market.json")
            profits.print_profits()

        elif command == "chiudi":
            print("Bye bye")
            break
        else:
            print(f"Comando non valido\n{HELPER_STR}")
            