# imports here


class APIResource(object):

    def __init__(self, response_dict):
        self.data = response_dict

        for key in self.data:
            setattr(self, key, self.data[key])


class AuctionResource(APIResource):
    pass


class ItemResource(APIResource):
    pass