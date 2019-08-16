In the documentation the following inconsistencies exist:

There are two identical wow/user/characters endpoints in the Community API: 'User API'
and 'World of Warcraft Profile API'


Community:
wow/user/characters
wow/achievement/:id
wow/auction/data/:realm
wow/boss/
wow/boss/:bossid
wow/challenge/:realm
wow/challenge/region
wow/character/:realm/:characterName
wow/guild/:realm/:guildName
wow/item/:itemId
wow/item/set/:setId
wow/mount/
wow/pet/
wow/pet/ability/:abilityID
wow/pet/species/:speciesID
wow/pet/stats/:speciesID
wow/leaderboard/:bracket
wow/quest/:questId
wow/realm/status
wow/recipe/:recipeId
wow/spell/:spellId
wow/user/characters
wow/zone/
wow/zone/:zoneid
wow/data/battlegroups/
wow/data/character/races
wow/data/character/classes
wow/data/character/achievements
wow/data/guild/rewards
wow/data/guild/perks
wow/data/guild/achievements
wow/data/item/classes
wow/data/talents
wow/data/pet/types


Data:
/data/wow/achievement-category/index
/data/wow/achievement-category/{achievementCategoryId}
/data/wow/achievement/index
/data/wow/achievement/{achievementId}
/data/wow/media/achievement/{achievementId}
/data/wow/azerite-essence/index
/data/wow/azerite-essence/{azeriteEssenceId}
/data/wow/media/azerite-essence/{azeriteEssenceId}
/data/wow/connected-realm/index
/data/wow/connected-realm/{connectedRealmId}
/data/wow/creature-family/index
/data/wow/creature-family/{creatureFamilyId}
/data/wow/creature-type/index
/data/wow/creature-type/{creatureTypeId}
/data/wow/creature/{creatureId}
/data/wow/media/creature-display/{creatureDisplayId}
/data/wow/media/creature-family/{creatureFamilyId}
/data/wow/guild/{realmSlug}/{nameSlug}
/data/wow/guild/{realmSlug}/{nameSlug}/achievements
/data/wow/guild/{realmSlug}/{nameSlug}/roster
/data/wow/guild-crest/index
/data/wow/media/guild-crest/border/{borderId}
/data/wow/media/guild-crest/emblem/{emblemId}
/data/wow/item-class/index
/data/wow/item-class/{itemClassId}
/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}
/data/wow/item/{itemId}
/data/wow/media/item/{itemId}
/data/wow/keystone-affix/index
/data/wow/keystone-affix/{keystoneAffixId}
/data/wow/leaderboard/hall-of-fame/{raid}/{faction}
/data/wow/mount/index
/data/wow/mount/{mountId}
/data/wow/mythic-keystone/dungeon/index
/data/wow/mythic-keystone/dungeon/{dungeonId}
/data/wow/mythic-keystone/index
/data/wow/mythic-keystone/period/index
/data/wow/mythic-keystone/period/{periodId}
/data/wow/mythic-keystone/season/index
/data/wow/mythic-keystone/season/{seasonId}
/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index
/data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeonId}/period/{period}
/data/wow/pet/index
/data/wow/pet/{petId}
/data/wow/playable-class/index
/data/wow/playable-class/{classId}
/data/wow/playable-class/{classId}/pvp-talent-slots
/data/wow/playable-race/index
/data/wow/playable-race/{playableRaceId}
/data/wow/playable-specialization/index
/data/wow/playable-specialization/{specId}
/data/wow/power-type/index
/data/wow/power-type/{powerTypeId}
/data/wow/pvp-season/index
/data/wow/pvp-season/{pvpSeasonId}
/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/index
/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/{pvpBracket}
/data/wow/pvp-season/{pvpSeasonId}/pvp-reward/index
/data/wow/media/pvp-tier/{pvpTierId}
/data/wow/pvp-tier/index
/data/wow/pvp-tier/{pvpTierId}
/data/wow/realm/index
/data/wow/realm/{realmSlug}
/data/wow/region/index
/data/wow/region/{regionId}
/data/wow/title/index
/data/wow/title/{titleId}
/data/wow/token/index


TODO:

- Guild community API
- API endpoint, fix documentation prefixes
- Finish live tests
- Implement spec checker with drone pipeline step
- Report inconsistencies on forum
- Update missing Community API endpoints
- Update updated game data api
- Update changelog
- Update version
- Release new version (semantic version yet to be determined: based on blizz deprecations)
