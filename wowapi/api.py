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
    return ItemResource(response_dict)











# item = api.get_item('eu.battle.net', 9999, locale='en_GB')

# auction_page = api.get_auctions_overview('eu.battle.net', 'khadgar')
# new = auction_page.updated(last_ts) # return true or false

# if new:
#     auctions = auction_page.get_auctions()
# else:
#     pass

# auctions.horde
# auctions.alliance
# auctions.neutral
# auctions.all # modified. One list with faction as property

