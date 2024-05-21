class Command:
    def __init__(self, domain, function, params):
        self._domain = domain
        self._function = function
        self._params = params

    @property
    def domain(self):
        return self._domain

    @property
    def function(self):
        return self._function

    @property
    def params(self):
        return self._params

    @domain.setter
    def domain(self, value):
        self._domain = value

    @function.setter
    def function(self, value):
        self._function = value

    @params.setter
    def params(self, value):
        self._params = value

    def __str__(self):
        return f"Command(domain={self._domain}, function={self._function}, params={self._params})"

    def __repr__(self):
        return f"Command(domain={self._domain!r}, function={self._function!r}, params={self._params!r})"

    def to_json(self):
        return {"domain": self._domain, "function": self._function, "params": self._params}
