from .connectors import (
    AuctionConnector, ItemConnector)
from .resources import (
    AuctionResource, ItemResource)


def get_auctions(host, *args, **kwargs):
    connector = AuctionConnector(host, args, kwargs)
    response_dict = connector.get_resource()
    return AuctionResource(response_dict)


def get_item(host, *args, **kwargs):
    connector = ItemConnector(host, args, kwargs)
    response_dict = connector.get_resource()
    return ItemResource(response_dict, all_keywords=True)

