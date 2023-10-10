class EmptyShopException(Exception):
    '''
    Exception raised when dictionary is void
    dict_var (dict): dictionary causing the error
    message (str): error message
    '''
    def __init__(self, dict_var, message="Il negozio attualmente non ha prodotti in vendita."):
        self.dict_var = dict_var
        self.message = message
        super().__init__(self.message)