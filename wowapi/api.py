from .connectors import (
    AuctionConnector, ItemConnector, ItemSetConnector, CharacterConnector,
    PetAbilitiesConnector, PetSpeciesConnector, PetStatsConnector,
    RealmLeaderboardConnector, RegionLeaderboardConnector
)
from .resources import (
    AuctionResource, ItemResource, ItemSetResource, CharacterResource,
    PetAbilitiesResource, PetSpeciesResource, PetStatsResource,
    RealmLeaderboardResource, RegionLeaderboardResource
)


def get_auctions(host, realm_slug, **kwargs):
    connector = AuctionConnector(host, *[realm_slug], **kwargs)
    response_dict = connector.get_resource()
    return AuctionResource(response_dict)


def get_item(host, item_id, **kwargs):
    connector = ItemConnector(host, *[item_id], **kwargs)
    response_dict = connector.get_resource()
    return ItemResource(response_dict, all_keywords=True)


def get_item_set(host, set_id, **kwargs):
    connector = ItemSetConnector(host, *[set_id], **kwargs)
    response_dict = connector.get_resource()
    return ItemSetResource(response_dict, all_keywords=True)


def get_character(host, realm_slug, character_name, **kwargs):
    connector = CharacterConnector(
        host, *[realm_slug, character_name], **kwargs)
    response_dict = connector.get_resource()
    return CharacterResource(response_dict, all_keywords=True)


def get_pet_abilities(host, ability_id, **kwargs):
    connector = PetAbilitiesConnector(host, *[ability_id], **kwargs)
    response_dict = connector.get_resource()
    return PetAbilitiesResource(response_dict, all_keywords=True)


def get_pet_species(host, species_id, **kwargs):
    connector = PetSpeciesConnector(host, *[species_id], **kwargs)
    response_dict = connector.get_resource()
    return PetSpeciesResource(response_dict, all_keywords=True)


def get_pet_stats(host, species_id, **kwargs):
    connector = PetStatsConnector(host, *[species_id], **kwargs)
    response_dict = connector.get_resource()
    return PetStatsResource(response_dict, all_keywords=True)


def get_realm_leaderboard(host, realm_slug, **kwargs):
    connector = RealmLeaderboardConnector(host, *[realm_slug], **kwargs)
    response_dict = connector.get_resource()
    return RealmLeaderboardResource(response_dict, all_keywords=True)


def get_region_leaderboard(host, **kwargs):
    connector = RegionLeaderboardConnector(host, **kwargs)
    response_dict = connector.get_resource()
    return RegionLeaderboardResource(response_dict, all_keywords=True)