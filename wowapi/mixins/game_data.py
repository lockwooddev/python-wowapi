class GameDataMixin:
    """All Game Data API methods"""

    # Achievement API

    def get_achievement_category_index(self, region, namespace, **filters):
        """
        Data Achievement API - Returns an index of achievement categories
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/achievement-category/index', region, **filters)

    def get_achievement_category(self, region, namespace, id, **filters):
        """
        Data Achievement API - Returns an achievement category by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/achievement-category/{0}', region, *[id],  **filters)

    def get_achievement_index(self, region, namespace, **filters):
        """
        Data Achievement API - Returns an index of achievements
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/achievement/index', region, **filters)

    def get_achievement_data(self, region, namespace, id, **filters):
        """
        Data Achievement API - Returns an achievement by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/achievement/{0}', region, *[id], **filters)

    def get_achievement_media(self, region, namespace, id, **filters):
        """
        Data Achievement API - Returns media for an achievement by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/achievement/{0}', region, *[id], **filters)

    # Auction House API

    def get_auctions(self, region, namespace, connected_realm_id, **filters):
        """
        Auction House API - Returns all active auctions for a connected realm
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/connected-realm/{0}/auctions',
            region,
            *[connected_realm_id],
            **filters
        )

    # Azerite Essence API

    def get_azerite_essence_index(self, region, namespace, **filters):
        """
        Data Azerite Essence API - Returns an index of azerite essences
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/azerite-essence/index', region, **filters)

    def get_azerite_essence(self, region, namespace, id, **filters):
        """
        Data Azerite Essence API - Returns an azerite essence by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/azerite-essence/{0}', region, *[id], **filters)

    def get_azerite_essence_media(self, region, namespace, id, **filters):
        """
        Data Azerite Essence API - Returns media for an azerite essence by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/azerite-essence/{0}', region, *[id], **filters)

    # Connected Realm API

    def get_connected_realm_index(self, region, namespace, **filters):
        """
        Data Connected Realm API - Returns an index of connected realms
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/connected-realm/index', region, **filters)

    def get_connected_realm(self, region, namespace, id, **filters):
        """
        Data Connected Realm API - Returns a connected realm by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/connected-realm/{0}', region, *[id], **filters)

    # Creature API

    def get_creature_family_index(self, region, namespace, **filters):
        """
        Data Creature API - Returns an index of creature families
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/creature-family/index', region, **filters)

    def get_creature_family(self, region, namespace, id, **filters):
        """
        Data Creature API - Returns a creature family by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/creature-family/{0}', region, *[id], **filters)

    def get_creature_type_index(self, region, namespace, **filters):
        """
        Data Creature API - Returns an index of creature types
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/creature-type/index', region, **filters)

    def get_creature_type(self, region, namespace, id, **filters):
        """
        Data Creature API - Returns a creature type by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/creature-type/{0}', region, *[id], **filters)

    def get_creature(self, region, namespace, id, **filters):
        """
        Data Creature API - Returns a creature by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/creature/{0}', region, *[id], **filters)

    def get_creature_display_media(self, region, namespace, id, **filters):
        """
        Data Creature API - Returns media for a creature display by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/creature-display/{0}', region, *[id], **filters)

    def get_creature_family_media(self, region, namespace, id, **filters):
        """
        Data Creature API - Returns media for a creature family by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/creature-family/{0}', region, *[id], **filters)

    # Guild Crest API

    def get_guild_crest_index(self, region, namespace, **filters):
        """
        Guild Crest API - Returns an index of guild crest media
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/guild-crest/index', region, **filters)

    def get_guild_crest_border_media(self, region, namespace, id, **filters):
        """
        Guild Crest API - Returns media for a guild crest border by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/guild-crest/border/{0}', region, *[id], **filters)

    def get_guild_crest_emblem_media(self, region, namespace, id, **filters):
        """
        Guild Crest API - Returns media for a guild crest emblem by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/guild-crest/emblem/{0}', region, *[id], **filters)

    # Item API

    def get_item_class_index(self, region, namespace, **filters):
        """
        Item API - Returns an index of item classes
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/item-class/index', region, **filters)

    def get_item_class(self, region, namespace, id, **filters):
        """
        Item API - Returns an item class by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/item-class/{0}', region, *[id], **filters)

    def get_item_set_index(self, region, namespace, **filters):
        """
        Item API - Returns an index of item sets
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/item-set/index', region, **filters)

    def get_item_set(self, region, namespace, id, **filters):
        """
        Item API - Returns an item set by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/item-set/{0}', region, *[id], **filters)

    def get_item_subclass(self, region, namespace, class_id, subclass_id, **filters):
        """
        Item API - Returns an item subclass by id
        """
        filters['namespace'] = namespace
        params = [class_id, subclass_id]
        resource = 'data/wow/item-class/{0}/item-subclass/{1}'
        return self.get_resource(resource, region, *params, **filters)

    def get_item_data(self, region, namespace, id, **filters):
        """
        Item API - Returns an item by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/item/{0}', region, *[id], **filters)

    def get_item_media(self, region, namespace, id, **filters):
        """
        Item API - Returns media for an item by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/item/{0}', region, *[id], **filters)

    # Journal API

    def get_journal_index(self, region, namespace, **filters):
        """
        Item API - Returns an index of journal expansions
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/journal-expansion/index', region, **filters)

    def get_journal_expansion(self, region, namespace, id, **filters):
        """
        Item API - Returns a journal expansion by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/journal-expansion/{0}', region, *[id], **filters)

    def get_journal_encounter_index(self, region, namespace, **filters):
        """
        Item API - Returns an index of journal encounters
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/journal-encounter/index', region, **filters)

    def get_journal_encounter(self, region, namespace, id, **filters):
        """
        Item API - Returns a journal encounter by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/journal-encounter/{0}', region, *[id], **filters)

    def get_journal_instance_index(self, region, namespace, **filters):
        """
        Item API - Returns an index of journal instances
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/journal-instance/index', region, **filters)

    def get_journal_instance(self, region, namespace, id, **filters):
        """
        Item API - Returns a journal instance
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/journal-instance/{0}', region, *[id], **filters)

    def get_journal_instance_media(self, region, namespace, id, **filters):
        """
        Item API - Returns media for a journal instance by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/journal-instance/{0}', region, *[id], **filters)

    # Mount API

    def get_mount_index(self, region, namespace, **filters):
        """
        Mount API - Returns an index of mounts
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/mount/index', region, **filters)

    def get_mount_data(self, region, namespace, id, **filters):
        """
        Mount API - Returns a mount by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/mount/{0}', region, *[id], **filters)

    # Mythic Keystone Affix API

    def get_mythic_keystone_affixes(self, region, namespace, **filters):
        """
        Mythic Keystone Affix API - get mythic keystone affixes
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/keystone-affix/index', region, **filters)

    def get_mythic_keystone_affix(self, region, namespace, affix_id, **filters):
        """
        Mythic Keystone Affix API - get mythic keystone affix by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/keystone-affix/{0}', region, *[affix_id], **filters)

    def get_mythic_keystone_affix_media(self, region, namespace, affix_id, **filters):
        """
        Mythic Keystone Affix API - get mythic keystone affix by id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/media/keystone-affix/{0}',
            region,
            *[affix_id],
            **filters
        )

    # Mythic Keystone Dungeon API

    def get_mythic_keystone_dungeon_index(self, region, namespace, **filters):
        """
        Mythic Keystone Dungeon API - get all mythic keystone dungeons
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/mythic-keystone/dungeon/index', region, **filters)

    def get_mythic_keystone_dungeon(self, region, namespace, dungeon_id, **filters):
        """
        Mythic Keystone Dungeon API - get mythic keystone dungeon by id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/mythic-keystone/dungeon/{0}', region, *[dungeon_id], **filters)

    def get_mythic_keystone_index(self, region, namespace, **filters):
        """
        Mythic Keystone Dungeon API - get links to documents related to mythic keystone dungeons
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/mythic-keystone/index', region, **filters)

    def get_mythic_keystone_period_index(self, region, namespace, **filters):
        """
        Mythic Keystone Dungeon API - get all mythic keystone periods
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/mythic-keystone/period/index', region, **filters)

    def get_mythic_keystone_period(self, region, namespace, period_id, **filters):
        """
        Mythic Keystone Dungeon API - get mythic keystone period by id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/mythic-keystone/period/{0}', region, *[period_id], **filters)

    def get_mythic_keystone_season_index(self, region, namespace, **filters):
        """
        Mythic Keystone Dungeon API - get all mythic keystone seasons
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/mythic-keystone/season/index', region, **filters)

    def get_mythic_keystone_season(self, region, namespace, season_id, **filters):
        """
        Mythic Keystone Dungeon API - get mythic keystone season by id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/mythic-keystone/season/{0}', region, *[season_id], **filters)

    # Mythic Keystone Leaderboard API

    def get_mythic_keystone_leaderboard_index(
        self, region, namespace, connected_realm_id, **filters
    ):
        """
        Mythic Keystone Leaderboard API
        Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm
        """
        filters['namespace'] = namespace
        resource = 'data/wow/connected-realm/{0}/mythic-leaderboard/index'
        return self.get_resource(resource, region, *[connected_realm_id], **filters)

    def get_mythic_keystone_leaderboard(
        self, region, namespace, connected_realm_id, dungeon_id, period, **filters
    ):
        """
        Mythic Keystone Leaderboard API - get a weekly mythic keystone leaderboard by period
        """
        filters['namespace'] = namespace
        resource = 'data/wow/connected-realm/{0}/mythic-leaderboard/{1}/period/{2}'
        params = [connected_realm_id, dungeon_id, period]
        return self.get_resource(resource, region, *params, **filters)

    # Mythic Raid Leaderboard API

    def get_mythic_raid_leaderboard(self, region, namespace, raid, faction, **filters):
        """
        Mythic Raid Leaderboard API - get mythic raid leaderboard of specific faction
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/leaderboard/hall-of-fame/{0}/{1}',
            region,
            *[raid, faction],
            **filters
        )

    # Pet API

    def get_pet_index(self, region, namespace, **filters):
        """
        Pet API - Returns an index of pets
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/pet/index', region, **filters)

    def get_pet_data(self, region, namespace, id, **filters):
        """
        Pet API - Returns a pet by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/pet/{0}', region, *[id], **filters)

    # Playable Class API

    def get_playable_class_index(self, region, namespace, **filters):
        """
        Playable Class API - Returns an index of playable classes
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-class/index', region, **filters)

    def get_playable_class(self, region, namespace, class_id, **filters):
        """
        Playable Class API - Returns a playable class by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-class/{0}', region, *[class_id], **filters)

    def get_playable_class_media(self, region, namespace, class_id, **filters):
        """
        Playable Class API - Returns a playable class media by ID
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/media/playable-class/{0}',
            region,
            *[class_id],
            **filters
        )

    def get_playable_class_pvp_talent_slots(self, region, namespace, class_id, **filters):
        """
        Playable Class API - Returns the PvP talent slots for a playable class by ID
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/playable-class/{0}/pvp-talent-slots', region, *[class_id], **filters)

    # Playable Race API

    def get_playable_race_index(self, region, namespace, **filters):
        """
        Playable Race API - Returns an index of playable races
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-race/index', region, **filters)

    def get_playable_race(self, region, namespace, race_id, **filters):
        """
        Playable Race API - Returns a playable race by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-race/{0}', region, *[race_id], **filters)

    # Playable Specialization API

    def get_playable_specialization_index(self, region, namespace, **filters):
        """
        Playable Specialization API - get playable specializations
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/playable-specialization/index', region, **filters)

    def get_playable_specialization(self, region, namespace, spec_id, **filters):
        """
        Playable Specialization API - get playable specialization by spec id
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/playable-specialization/{0}',
            region,
            *[spec_id],
            **filters
        )

    def get_playable_specialization_media(self, region, namespace, spec_id, **filters):
        """
        Playable Specialization API - Returns media for a playable specialization by ID
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/media/playable-specialization/{0}',
            region,
            *[spec_id],
            **filters
        )

    # Power Type API

    def get_power_type_index(self, region, namespace, **filters):
        """
        Power Type API - get power types
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/power-type/index', region, **filters)

    def get_power_type(self, region, namespace, power_type_id, **filters):
        """
        Power Type API - get power type by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/power-type/{0}', region, *[power_type_id], **filters)

    # Profession API

    def get_profession_index(self, region, namespace, **filters):
        """
        Profession API - Returns an index of professions
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/profession/index', region, **filters)

    def get_profession(self, region, namespace, id, **filters):
        """
        Profession API - Returns a profession by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/profession/{0}', region, *[id], **filters)

    def get_profession_media(self, region, namespace, id, **filters):
        """
        Profession API - Returns media for a profession by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/profession/{0}', region, *[id], **filters)

    def get_profession_skill_tier(self, region, namespace, prof_id, tier_id, **filters):
        """
        Profession API - Returns a skill tier for a profession by ID
        """
        filters['namespace'] = namespace
        return self.get_resource(
            'data/wow/profession/{0}/skill-tier/{1}', region, *[prof_id, tier_id], **filters)

    def get_recipe(self, region, namespace, id, **filters):
        """
        Profession API - Returns a recipe by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/recipe/{0}', region, *[id], **filters)

    def get_recipe_media(self, region, namespace, id, **filters):
        """
        Profession API - Returns media for a recipe by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/recipe/{0}', region, *[id], **filters)

    # PvP Season API

    def get_pvp_season_index(self, region, namespace, **filters):
        """
        PvP Season API - Returns an index of PvP seasons
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/pvp-season/index', region, **filters)

    def get_pvp_season(self, region, namespace, season_id, **filters):
        """
        PvP Season API - Returns a PvP season by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/pvp-season/{0}', region, *[season_id], **filters)

    def get_pvp_leaderboard_index(self, region, namespace, season_id, **filters):
        """
        PvP Season API - Returns an index of PvP leaderboards for a PvP season
        """
        filters['namespace'] = namespace
        resource = 'data/wow/pvp-season/{0}/pvp-leaderboard/index'
        return self.get_resource(resource, region, *[season_id], **filters)

    def get_pvp_leaderboard(self, region, namespace, season_id, bracket, **filters):
        """
        PvP Season API - Returns the PvP leaderboard of a specific PvP bracket for a PvP season
        """
        filters['namespace'] = namespace
        resource = 'data/wow/pvp-season/{0}/pvp-leaderboard/{1}'
        return self.get_resource(resource, region, *[season_id, bracket], **filters)

    def get_pvp_rewards_index(self, region, namespace, season_id, **filters):
        """
        PvP Season API - Returns an index of PvP rewards for a PvP season
        """
        filters['namespace'] = namespace
        resource = 'data/wow/pvp-season/{0}/pvp-reward/index'
        return self.get_resource(resource, region, *[season_id], **filters)

    # PvP Tier API

    def get_pvp_tier_media(self, region, namespace, tier_id, **filters):
        """
        PvP Tier API - Returns media for a PvP tier by ID
        """
        filters['namespace'] = namespace
        resource = 'data/wow/media/pvp-tier/{0}'
        return self.get_resource(resource, region, *[tier_id], **filters)

    def get_pvp_tier_index(self, region, namespace, **filters):
        """
        PvP Tier API - Returns an index of PvP tiers
        """
        filters['namespace'] = namespace
        resource = 'data/wow/pvp-tier/index'
        return self.get_resource(resource, region, **filters)

    def get_pvp_tier(self, region, namespace, tier_id, **filters):
        """
        PvP Tier API - Returns a PvP tier by ID
        """
        filters['namespace'] = namespace
        resource = 'data/wow/pvp-tier/{0}'
        return self.get_resource(resource, region, *[tier_id], **filters)

    # Quest API

    def get_quest_index(self, region, namespace, **filters):
        """
        Quest API - Returns an index of quests
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/index', region, **filters)

    def get_quest(self, region, namespace, id, **filters):
        """
        Quest API - Returns a quest by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/{0}', region, *[id], **filters)

    def get_quest_categories_index(self, region, namespace, **filters):
        """
        Quest API - Returns an index of quest categories

        (such as quests for a specific class, profession, or storyline)
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/category/index', region, **filters)

    def get_quest_catagory(self, region, namespace, id, **filters):
        """
        Quest API - Returns a quest category by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/category/{0}', region, *[id], **filters)

    def get_quest_area_index(self, region, namespace, **filters):
        """
        Quest API - Returns an index of quest areas
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/area/index', region, **filters)

    def get_quest_area(self, region, namespace, id, **filters):
        """
        Quest API - Returns a quest area by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/area/{0}', region, *[id], **filters)

    def get_quest_types_index(self, region, namespace, **filters):
        """
        Quest API - Returns an index of quest types

        (such as PvP quests, raid quests, or account quests)
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/type/index', region, **filters)

    def get_quest_type(self, region, namespace, id, **filters):
        """
        Quest API - Returns a quest type by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/quest/type/{0}', region, *[id], **filters)

    # Realm API

    def get_realm_index(self, region, namespace, **filters):
        """
        Realm API - get realms
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/realm/index', region, **filters)

    def get_realm(self, region, namespace, realm_slug, **filters):
        """
        Realm API - get realm by realm slug
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/realm/{0}', region, *[realm_slug], **filters)

    # Region API

    def get_region_index(self, region, namespace, **filters):
        """
        Region API - get regions
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/region/index', region, **filters)

    def get_region(self, region, namespace, region_id, **filters):
        """
        Region API - get region by region id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/region/{0}', region, *[region_id], **filters)

    # Reputations API

    def get_reputation_faction_index(self, region, namespace, **filters):
        """
        Reputations API - Returns an index of reputation factions
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/reputation-faction/index', region, **filters)

    def get_reputation_faction(self, region, namespace, id, **filters):
        """
        Reputations API - Returns a single reputation faction by ID.
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/reputation-faction/{0}', region, *[id], **filters)

    def get_reputation_tier_index(self, region, namespace, **filters):
        """
        Reputations API - Returns an index of reputation tiers
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/reputation-tiers/index', region, **filters)

    def get_reputation_tier(self, region, namespace, id, **filters):
        """
        Reputations API - Returns a single set of reputation tiers by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/reputation-tiers/{0}', region, *[id], **filters)

    # Spell API

    def get_spell(self, region, namespace, id, **filters):
        """
        Spell API - Returns a spell by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/spell/{0}', region, *[id], **filters)

    def get_spell_media(self, region, namespace, id, **filters):
        """
        Spell API - Returns media for a spell by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/media/spell/{0}', region, *[id], **filters)

    # Talent API

    def get_talent_index(self, region, namespace, **filters):
        """
        Talent API - Returns an index of talents
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/talent/index', region, **filters)

    def get_talent(self, region, namespace, id, **filters):
        """
        Talent API - Returns a talent by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/talent/{0}', region, *[id], **filters)

    def get_pvp_talent_index(self, region, namespace, **filters):
        """
        Talent API - Returns an index of PvP talents
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/pvp-talent/index', region, **filters)

    def get_pvp_talent(self, region, namespace, id, **filters):
        """
        Talent API - Returns a PvP talent by ID
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/pvp-talent/{0}', region, *[id], **filters)

    # Title API

    def get_title_index(self, region, namespace, **filters):
        """
        Title API - Returns an index of titles
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/title/index', region, **filters)

    def get_title(self, region, namespace, id, **filters):
        """
        Title API - Returns a title by id
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/title/{0}', region, *[id], **filters)

    # WoW Token API

    def get_token_index(self, region, namespace, **filters):
        """
        WoW Token API - Returns the WoW Token index
        """
        filters['namespace'] = namespace
        return self.get_resource('data/wow/token/index', region, **filters)
