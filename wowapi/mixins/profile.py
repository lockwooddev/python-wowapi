class ProfileMixin:
    """All Profile API methods"""

    # Account Profile API (requiring Authorization Code Flow token)

    def get_account_profile_summary(
        self, region, namespace, token, **filters
    ):
        """
        Returns a profile summary for an account
        """
        filters['namespace'] = namespace
        resource = 'profile/user/wow'
        return self.get_oauth_resource(resource, region, token, **filters)

    def get_protected_character_profile_summary(
        self, region, namespace, token, realm_id, character_id, **filters
    ):
        """
        Returns a protected profile summary for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/user/wow/protected-character/{0}-{1}'
        return self.get_oauth_resource(
            resource,
            region,
            token,
            *[realm_id, character_id],
            **filters
        )

    def get_account_collection_index(self, region, namespace, token, **filters):
        """
        Returns an index of collection types for an account
        """
        filters['namespace'] = namespace
        resource = 'profile/user/wow/collections'
        return self.get_oauth_resource(resource, region, token, **filters)

    def get_mount_collection_summary(self, region, namespace, token, **filters):
        """
        Returns a summary of the mounts an account has obtained
        """
        filters['namespace'] = namespace
        resource = 'profile/user/wow/collections/mounts'
        return self.get_oauth_resource(resource, region, token, **filters)

    def get_pet_collection_summary(self, region, namespace, token, **filters):
        """
        Returns a summary of the pets an account has obtained
        """
        filters['namespace'] = namespace
        resource = 'profile/user/wow/collections/pets'
        return self.get_oauth_resource(resource, region, token, **filters)

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

    def get_character_achievements_statistics(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Achievements API
        Returns a character's statistics as they pertain to achievements
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/achievements/statistics'
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

    # Character Collections API

    def get_character_collection_index(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Collections API - Returns an index of collection types for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/collections'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    def get_character_mount_collection_index(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Collections API - Returns a summary of the mounts a character has obtained
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/collections/mounts'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    def get_character_pet_collection_index(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Collections API - Returns a summary of the pets a character has obtained
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/collections/pets'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    # Character Encounters API

    def get_character_encounters_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Encounters API - Returns a summary of a character's encounters
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/encounters'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    def get_character_dungeons(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Encounters API - Returns a summary of a character's completed dungeons
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/encounters/dungeons'
        return self.get_resource(resource, region, *[realm_slug, character_name], **filters)

    def get_character_raids(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Encounters API - Returns a summary of a character's completed raids
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/encounters/raids'
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

    # Character Hunter Pets API

    def get_character_hunter_pets_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Hunter Pets API - Returns a summary of the items equipped by a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/hunter-pets'
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

    # Character Professions API

    def get_character_professions_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Professions API - Returns a summary of professions for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/professions'
        params = [realm_slug, character_name]
        return self.get_resource(resource, region, *params, **filters)

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

    def get_character_profile_status(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Profile API - Returns the status and a unique ID for a character
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/status'
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

    # Character Quests API

    def get_character_quests(self, region, namespace, realm_slug, character_name, **filters):
        """
        Character Quests API
        Returns a character's active quests as well as a link to the character's completed quests
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/quests'
        params = [realm_slug, character_name]
        return self.get_resource(resource, region, *params, **filters)

    def get_character_completed_quests(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Quests API - Returns a list of quests that a character has completed
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/quests/completed'
        params = [realm_slug, character_name]
        return self.get_resource(resource, region, *params, **filters)

    # Character Reputations API

    def get_character_reputations_summary(
        self, region, namespace, realm_slug, character_name, **filters
    ):
        """
        Character Reputations API - Returns a summary of a character's reputations
        """
        filters['namespace'] = namespace
        resource = 'profile/wow/character/{0}/{1}/reputations'
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

    # Guild API

    def get_guild(self, region, namespace, realm_slug, guild_slug, **filters):
        """
        Guild API - Returns a single guild by its name and realm
        """
        filters['namespace'] = namespace
        params = [realm_slug, guild_slug]
        return self.get_resource('data/wow/guild/{0}/{1}', region, *params, **filters)

    def get_guild_activity(self, region, namespace, realm_slug, guild_slug, **filters):
        """
        Guild API - Returns a single guild's activity by name and realm
        """
        filters['namespace'] = namespace
        params = [realm_slug, guild_slug]
        return self.get_resource('data/wow/guild/{0}/{1}/activity', region, *params, **filters)

    def get_guild_achievements(self, region, namespace, realm_slug, guild_slug, **filters):
        """
        Guild API - Returns a single guild's achievements by name and realm
        """
        filters['namespace'] = namespace
        params = [realm_slug, guild_slug]
        return self.get_resource('data/wow/guild/{0}/{1}/achievements', region, *params, **filters)

    def get_guild_roster(self, region, namespace, realm_slug, guild_slug, **filters):
        """
        Guild API - Returns a single guild's roster by its name and realm
        """
        filters['namespace'] = namespace
        params = [realm_slug, guild_slug]
        return self.get_resource('data/wow/guild/{0}/{1}/roster', region, *params, **filters)
