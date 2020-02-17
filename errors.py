class Error(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        print("This error to be sent", message, status_code)
