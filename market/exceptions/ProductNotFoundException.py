class ProductNotFoundException(Exception):
    '''
    Eccezione generata quando inserisco un nuovo prodotto nel dizionario senza specificarne il prezzo
    product (str): prodotto che ha causato l'eccezione
    dict_var (dict): dizionario
    message (str): spiegazione dell'errore
    '''
    def __init__(self, product, dict_var, message="Un nuovo prodotto richiede di specificare il prezzo di vendita e di acquisto"):
        self.product = product
        self.dict_var = dict_var
        self.message = message
        super().__init__(self.message)