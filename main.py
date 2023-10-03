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

def add_product(vegan_market):
    product = input("Nome del prodotto: ")
    try:
        quantity = int(input("Quantità: "))
    except ValueError as e:
        print(e)
        return "Impossibile inserire la quantità desiderata."
    
    feedback_str = f"AGGIUNTO: {quantity} X {product}"
    if vegan_market.is_in_store(product):
        vegan_market.add(product, quantity)
        return feedback_str
    
    try:
        buy_price = float(input("Prezzo di acquisto: "))
        sell_price = float(input("Prezzo di vendita: "))
    except Exception as e:
        print(e)
        return "Il prezzo inserito non è corretto"
    
    vegan_market.add(product, quantity, (buy_price, sell_price))
    return feedback_str

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
            pass
        elif command == "vendita":
            pass
        elif command == "profitti":
            pass
        elif command == "chiudi":
            print("Bye bye")
            break
        else:
            print(f"Comando non valido\n{HELPER_STR}")
            