from market import VeganMarket


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