class Error(Exception):
    error = 0
    message = ''

    def __init__(self, message, error):
        self.message = message
        self.error = error

    def as_dict(self):
        return {'message': self.message, 'error': self.error}

class APINotFound(Error):
    def __init__(self, message):
        self.message = message
        self.error = 404

class APIResourceNotFound(Error):
    def __init__(self, message):
        self.message = message
        self.error = 400

class APIMissingParams(Error):
    def __init__(self, message):
        self.message = message
        self.error = 400

class APIAuthError(Error):
    def __init__(self, message):
        self.message = message
        self.error = 401