from market import Stock, Sell, VeganShop
from manage_products import add_product_to_store, sell_products

HELPER_STR="""
I comandi disponibili sono i seguenti:
- aggiungi: aggiungi un prodotto al negozio
- elenca: elenca i prodotto in negozio
- vendita: registra una vendita effettuata
- profitti: mostra i profitti totali
- aiuto: mostra i possibili comandi
- chiudi: esci dal programma
"""

#help(Sell)
#help(Stock)
#help(VeganShop)
#help(add_product_to_store)
#help(sell_products)

if __name__ == "__main__":   
    while 1:
        command = input("Inserisci un comando: ")
        if command.lower() == "aiuto":
            print(HELPER_STR)
        elif command.lower() == "aggiungi":
            stock = Stock("vegan_shop.json")
            print(add_product_to_store(stock))
            
        elif command.lower() == "elenca":
            vegan_shop = VeganShop("vegan_shop.json")
            print(vegan_shop)
            
        elif command.lower() == "vendita":
            cart = Sell("vegan_shop.json") 
            print(sell_products(cart))
            
        elif command.lower() == "profitti":
            profits = VeganShop("vegan_shop.json")
            profits.print_profits()

        elif command.lower() == "chiudi":
            print("Bye bye")
            break
        else:
            print(f"Comando non valido{HELPER_STR}")
            