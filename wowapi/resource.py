


class APIResource(object):

    def __init__(self, resource_dict):
        self.data = resource_dict

        for key in self.data:
            setattr(self, key, self.data[key])


class AuctionResource(object):
    pass


class ItemResource(object):