from market import VeganMarket

HELPER_STR="""
I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al magazzino
elenca: elenca i prodotto in magazzino
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma
"""

def get_product_info():
    product = input("Nome del prodotto: ")
    try:
        quantity = int(input("Quantità: "))
    except ValueError as e:
        print(e)
        return None
    
    return [product, quantity]


def add_product(vegan_market):
    product_info = get_product_info()
    if not product_info:
        return "Impossibile inserire la quantità desiderata."
    
    feedback_str = f"AGGIUNTO: {product_info[1]} X {product_info[0]}"
    if vegan_market.is_in_store(product_info[0]):
        if vegan_market.add(product_info[0], product_info[1]):
            return feedback_str
    try:
        buy_price = float(input("Prezzo di acquisto: "))
        sell_price = float(input("Prezzo di vendita: "))
    except Exception as e:
        print(e)
        return "Il prezzo inserito non è corretto"
    
    if vegan_market.add(product_info[0], product_info[1], (buy_price, sell_price)):
        return feedback_str
    return "Impossibile aggiungere il prodotto"

def sell_product(vegan_market):
    product_info = get_product_info()
    if not product_info:
        return "Impossibile inserire la quantità desiderata."
    pass



if __name__ == "__main__":
    vegan_market = VeganMarket("vegan_market.json")
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
            print(add_product(vegan_market))
            
        elif command == "elenca":
            print(vegan_market)
            pass
        elif command == "vendita":
            print(sell_product(vegan_market))
            pass
        elif command == "profitti":
            pass
        elif command == "chiudi":
            print("Bye bye")
            break
        else:
            print(f"Comando non valido\n{HELPER_STR}")
            