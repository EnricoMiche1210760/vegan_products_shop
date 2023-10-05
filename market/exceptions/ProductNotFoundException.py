class ProductNotFoundException(Exception):
    """
    Exception raised when inserting a new product without sell and buy price.
    Attributes:
        dict_var (dict): input dictionary which caused the error
        message (str): explanation of the error
    """
    def __init__(self, product, message="A new product require to specify the buy and sell price."):
        self.dict_var = product
        self.message = message
        super().__init__(self.message)