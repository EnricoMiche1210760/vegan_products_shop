class EmptyShopException(Exception):
    '''
    Eccezione generata quando il dizionario è vuoto
    dict_var (dict): dizionario che ha causato l'errore
    message (str): spiegazione dell'errore
    '''
    def __init__(self, dict_var, message="Il negozio attualmente non ha prodotti in vendita."):
        self.dict_var = dict_var
        self.message = message
        super().__init__(self.message)