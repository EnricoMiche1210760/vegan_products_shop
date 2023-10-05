class FatalErrorException(Exception):
    """
    Exception raised for errors in the input salary.
    Attributes:
        dict_var (dict): input dictionary which caused the error
        message (str): explanation of the error
    """
    def __init__(self, dict_var, message="Unable to load store data."):
        self.dict_var = dict_var
        self.message = message
        super().__init__(self.message)