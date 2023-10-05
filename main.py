from market import Stock, Sell
from manage_products import add_product_to_store, sell_products

HELPER_STR="""
I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al magazzino
elenca: elenca i prodotto in magazzino
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma
"""

if __name__ == "__main__":
    
    '''
    Inserisci un comando: aiuto
    I comandi disponibili sono i seguenti:
    aggiungi: aggiungi un prodotto al magazzino
    elenca: elenca i prodotto in magazzino
    vendita: registra una vendita effettuata
    profitti: mostra i profitti totali
    aiuto: mostra i possibili comandi
    chiudi: esci dal programma  
    '''
    while 1:
        command = input("Inserisci un comando: ")
        if command == "aiuto":
            print(HELPER_STR)
        elif command == "aggiungi":
            stock = Stock("vegan_market.json")
            print(stock._market)
            print(add_product_to_store(stock))
            
        elif command == "elenca":
            print(vegan_market)
            pass
        elif command == "vendita":
            cart = Sell("vegan_market.json") 
            print(sell_products(cart))
            
            pass
        elif command == "profitti":
            pass
        elif command == "chiudi":
            print("Bye bye")
            break
        else:
            print(f"Comando non valido\n{HELPER_STR}")
            