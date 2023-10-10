class ProductNotFoundException(Exception):
    '''
    Exception raised when inserting a new product in the dictionar the product price is not specified
    product (str): product raising the exception
    dict_var (dict): dictionary
    message (str): error message
    '''
    def __init__(self, product, dict_var, message="Un nuovo prodotto richiede di specificare il prezzo di vendita e di acquisto"):
        self.product = product
        self.dict_var = dict_var
        self.message = message
        super().__init__(self.message)