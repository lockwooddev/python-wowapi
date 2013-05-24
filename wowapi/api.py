from .connector import (
    AuctionConnector, ItemConnector
)


def get_auctions(host, *args, **kwargs):
    connector = AuctionRecource(host, args, kwargs)
    resource = connector.get_resource()
    return 

# def get_auctions_overview(region, realm):
#     return AuctionRecource()




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

