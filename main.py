from market import Stock
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
    
    vegan_market = Stock("vegan_market.json")
    print(vegan_market._market)
    
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
            print(add_product_to_store(vegan_market))
            
        elif command == "elenca":
            print(vegan_market)
            pass
        elif command == "vendita":
            print(sell_products(vegan_market))
            pass
        elif command == "profitti":
            pass
        elif command == "chiudi":
            print("Bye bye")
            break
        else:
            print(f"Comando non valido\n{HELPER_STR}")
            