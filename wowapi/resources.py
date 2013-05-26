from .exceptions import APIError
from .connectors import APIConnector

import copy
import logging


logger = logging.getLogger("wowapi")


class APIResource(object):

    def __init__(self, response_dict, all_keywords=False):
        self.data = response_dict

        # set all first row keys as attribute
        if all_keywords:
            for key in self.data:
                setattr(self, key, self.data[key])


class AuctionResource(APIResource):

    def __init__(self, response_dict):
        super(AuctionResource, self).__init__(response_dict)
        self.url = self.data["files"][0]["url"]
        self.last_modified = self.data["files"][0]["lastModified"]
        self.auction_data = {}

    def is_updated(self, timestamp=None):
        new = False

        if timestamp:
            if timestamp < self.last_modified:
                new = True
        else:
            # if no timestamp argument. Download auctions.
            new = True

        if new:
            try:
                self.auction_data = APIConnector.handle_request(self.url)
            except APIError, e:
                logger.error(e)
                raise APIError(e)

        return new

    def get_property(self, key1, key2, false_return=[]):
        if self.auction_data:
            property_ = self.auction_data.get(key1)
            return property_[key2]
        return false_return

    @property
    def all(self):
        keywords = ["alliance", "horde", "neutral"]
        all_ = []
        if self.auction_data:
            dict_copy = copy.deepcopy(self.auction_data)
            for k in keywords:
                auctions = dict_copy.get(k)
                auctions = auctions["auctions"]

                for auction in auctions:
                    auction["faction"] = k
                    all_.append(auction)
        return all_

    @property
    def alliance(self):
        return self.get_property("alliance", "auctions")

    @property
    def horde(self):
        return self.get_property("horde", "auctions")

    @property
    def neutral(self):
        return self.get_property("neutral", "auctions")

    @property
    def realm_name(self):
        return self.get_property("realm", "name", '')

    @property
    def realm_slug(self):
        return self.get_property("realm", "slug", '')


class ItemResource(APIResource):
    pass