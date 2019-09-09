class CommunityMixin:
    """All Community API methods"""

    def get_oauth_profile(self, region):
        """
        World of Warcraft Profile API - data about wow profile for oauth token

        ```python
        api.get_oauth_profile('us')
        ```
        """
        return self.get_resource('wow/user/characters', region)

    def get_achievement(self, region, id, **filters):
        """
        Achievement API

        ```python
        api.get_achievement('us', 2144, locale='pt_BR')
        ```
        """
        return self.get_resource('wow/achievement/{0}', region, *[id], **filters)

    def get_auctions(self, region, realm_slug, **filters):
        """
        Auction API data status
        """
        return self.get_resource('wow/auction/data/{0}', region, *[realm_slug], **filters)

    def get_bosses(self, region, **filters):
        """
        Boss API - Master list of bosses
        """
        return self.get_resource('wow/boss/', region, **filters)

    def get_boss(self, region, id, **filters):
        """
        Boss API - Boss details
        """
        return self.get_resource('wow/boss/{0}', region, *[id], **filters)

    def get_realm_leaderboard(self, region, realm, **filters):
        """
        Challenge Mode API - realm leaderboard
        """
        return self.get_resource('wow/challenge/{0}', region, *[realm], **filters)

    def get_region_leaderboard(self, region, **filters):
        """
        Challenge Mode API - region leaderboard
        """
        return self.get_resource('wow/challenge/region', region, **filters)

    def get_character_profile(self, region, realm, character_name, **filters):
        """
        Character Profile API - base info or specific comma separated fields as filters

        ```python
        api = WowApi('client-id', 'client-secret')
        api.get_character_profile('eu', 'khadgar', 'patchwerk')
        api.get_character_profile('eu', 'khadgar', 'patchwerk', locale='en_GB', fields='guild,mounts')
        ```
        """  # noqa
        return self.get_resource(
            'wow/character/{0}/{1}', region, *[realm, character_name], **filters
        )

    def get_guild_profile(self, region, realm, guild_name, **filters):
        """
        Guild Profile API - base info or specific comma separated fields as filters

        ```python
        api = WowApi('client-id', 'client-secret')
        api.get_guild_profile('eu', 'khadgar')
        api.get_guild_profile('eu', 'khadgar', locale='en_GB', fields='achievements,challenge')
        ```
        """
        return self.get_resource('wow/guild/{0}/{1}', region, *[realm, guild_name], **filters)

    def get_item(self, region, id, **filters):
        """
        Item API - detail item
        """
        return self.get_resource('wow/item/{0}', region, *[id], **filters)

    def get_item_set(self, region, id, **filters):
        """
        Item API - detail item set
        """
        return self.get_resource('wow/item/set/{0}', region, *[id], **filters)

    def get_mounts(self, region, **filters):
        """
        Mounts API - all supported mounts
        """
        return self.get_resource('wow/mount/', region, **filters)

    def get_pets(self, region, **filters):
        """
        Pets API - all supported pets
        """
        return self.get_resource('wow/pet/', region, **filters)

    def get_pet_ability(self, region, id, **filters):
        """
        Pets API - pet ability details
        """
        return self.get_resource('wow/pet/ability/{0}', region, *[id], **filters)

    def get_pet_species(self, region, id, **filters):
        """
        Pets API - pet species details
        """
        return self.get_resource('wow/pet/species/{0}', region, *[id], **filters)

    def get_pet_stats(self, region, id, **filters):
        """
        Pets API - pet stats details
        """
        return self.get_resource('wow/pet/stats/{0}', region, *[id], **filters)

    def get_leaderboards(self, region, bracket, **filters):
        """
        Pvp API - pvp bracket leaderboard and rbg
        """
        return self.get_resource('wow/leaderboard/{0}', region, *[bracket], **filters)

    def get_quest(self, region, id, **filters):
        """
        Quest API - metadata for quests
        """
        return self.get_resource('wow/quest/{0}', region, *[id], **filters)

    def get_realm_status(self, region, **filters):
        """
        Realm Status API - realm status for region
        """
        return self.get_resource('wow/realm/status', region, **filters)

    def get_recipe(self, region, id, **filters):
        """
        Recipe API - recipe details
        """
        return self.get_resource('wow/recipe/{0}', region, *[id], **filters)

    def get_spell(self, region, id, **filters):
        """
        Spell API - spell details
        """
        return self.get_resource('wow/spell/{0}', region, *[id], **filters)

    def get_characters(self, region, **filters):
        """
        User API - List of characters of account

        ```python
        WowApi.get_characters('us')
        ```
        """
        return self.get_resource('wow/user/characters', region, **filters)

    def get_zones(self, region, **filters):
        """
        Zone API - master list
        """
        return self.get_resource('wow/zone/', region, **filters)

    def get_zone(self, region, id, **filters):
        """
        Zone API - detail zone
        """
        return self.get_resource('wow/zone/{0}', region, *[id], **filters)

    def get_battlegroups(self, region, **filters):
        """
        Data Resources API - all battlegroups
        """
        return self.get_resource('wow/data/battlegroups/', region, **filters)

    def get_character_races(self, region, **filters):
        """
        Data Resources API - all character races
        """
        return self.get_resource('wow/data/character/races', region, **filters)

    def get_character_classes(self, region, **filters):
        """
        Data Resources API - all character classes
        """
        return self.get_resource('wow/data/character/classes', region, **filters)

    def get_character_achievements(self, region, **filters):
        """
        Data Resources API - all character achievements
        """
        return self.get_resource('wow/data/character/achievements', region, **filters)

    def get_guild_rewards(self, region, **filters):
        """
        Data Resources API - all guild rewards
        """
        return self.get_resource('wow/data/guild/rewards', region, **filters)

    def get_guild_perks(self, region, **filters):
        """
        Data Resources API - all guild perks
        """
        return self.get_resource('wow/data/guild/perks', region, **filters)

    def get_guild_achievements(self, region, **filters):
        """
        Data Resources API - all guild achievements
        """
        return self.get_resource('wow/data/guild/achievements', region, **filters)

    def get_item_classes(self, region, **filters):
        """
        Data Resources API - all item classes
        """
        return self.get_resource('wow/data/item/classes', region, **filters)

    def get_talents(self, region, **filters):
        """
        Data Resources API - all talents, specs and glyphs for each class
        """
        return self.get_resource('wow/data/talents', region, **filters)

    def get_pet_types(self, region, **filters):
        """
        Data Resources API - all pet types
        """
        return self.get_resource('wow/data/pet/types', region, **filters)
