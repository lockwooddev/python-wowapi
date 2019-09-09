class ProfileMixin:
    """All Profile API methods"""

    # Character Achievements API

    def get_character_achievements_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Achievements API
        Returns a summary of the achievements a character has completed
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/achievements'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    # Character Appearance API

    def get_character_appearance_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Appearance API - Returns a summary of a character's appearance settings
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/appearance'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    # Character Equipment API

    def get_character_equipment_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Equipment API - Returns a summary of the items equipped by a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/equipment'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    # Character Media API

    def get_character_media_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Media API - Returns a summary of the media assets available for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/character-media'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    # Character Profile API

    def get_character_profile_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Profile API - Returns a profile summary for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    # Character PvP API

    def get_character_pvp_bracket_stats(
        self, region, namespace, realm_slug, character_name, bracket, **filters
    ):
        """
        Character PvP API - Returns the PvP bracket statistics for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/pvp-bracket/{2}'
        params = [realm_slug, character_name, bracket]
        return self.get_resource(resource, region, *params, **filters)

    def get_character_pvp_summary(self, region, namespace, realm_slug, character_name, **filters):
        """
        Character PvP API - Returns a PvP summary for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/pvp-summary'
        params = [realm_slug, character_name]
        return self.get_resource(resource, region, *params, **filters)

    # Character Specializations API

    def get_character_specializations_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Specializations API - Returns a summary of a character's specializations
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/specializations'
        params = [realm_slug, character_name]
        return self.get_resource(resource, region, *params, **filters)

    # Character Statistics API

    def get_character_stats_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Statistics API - Returns a statistics summary for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/statistics'
        params = [realm_slug, character_name]
        return self.get_resource(resource, region, *params, **filters)

    # Character Titles API

    def get_character_titles_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Titles API - Returns a summary of titles a character has obtained
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/titles'
        params = [realm_slug, character_name]
        return self.get_resource(resource, region, *params, **filters)

    # WoW Mythic Keystone Character Profile API

    def get_character_mythic_keystone_profile(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Profile API - Mythic Keystone Character Profile Index
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/mythic-keystone-profile'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    def get_character_mythic_keystone_profile_season(
        self, region, namespace, realm_slug, character_name, season_id, **filters
    ):
        """
        Profile API - Returns the Mythic Keystone season details for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/mythic-keystone-profile/season/{2}'
        params = [realm_slug, character_name, season_id]
        return self.get_resource(resource, region, *params, **filters)
