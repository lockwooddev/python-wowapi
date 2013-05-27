from .connectors import (
    AuctionConnector, ItemConnector, CharacterConnector)
from .resources import (
    AuctionResource, ItemResource, CharacterResource)


def get_auctions(host, realm_slug, **kwargs):
    connector = AuctionConnector(host, *[realm_slug], **kwargs)
    response_dict = connector.get_resource()
    return AuctionResource(response_dict)


def get_item(host, item_id, **kwargs):
    connector = ItemConnector(host, *[item_id], **kwargs)
    response_dict = connector.get_resource()
    return ItemResource(response_dict, all_keywords=True)


def get_character(host, realm_slug, character_name, **kwargs):
    connector = CharacterConnector(
        host, *[realm_slug, character_name], **kwargs)
    response_dict = connector.get_resource()
    return CharacterResource(response_dict, all_keywords=True)

