class SolarException(Exception):
    pass


class SolarParameterException(SolarException):
    pass


class SolarHTTPException(SolarException):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop("response", None)
        super().__init__(*args, **kwargs)
