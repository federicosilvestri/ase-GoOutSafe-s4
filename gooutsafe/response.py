from flask import Response


class ContainsResponse(Response):

    def __contains__(self, b):
        return b in self.data.decode('utf-8')
