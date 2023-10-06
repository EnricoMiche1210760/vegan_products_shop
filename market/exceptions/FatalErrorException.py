class FatalErrorException(Exception):
    '''
    Eccezione generata quando il dizionario è vuoto
    dict_var (dict): dizionario che ha causato l'errore
    message (str): spiegazione dell'errore
    '''
    def __init__(self, dict_var, message="Impossibile ottenere i dati del negozio."):
        self.dict_var = dict_var
        self.message = message
        super().__init__(self.message)