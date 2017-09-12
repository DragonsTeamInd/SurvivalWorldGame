class QuestCompliteChecker():
    def check(self,quests,Armors,MeeleWeapons):
        for quest in quests:
            if quest.complite == False:
                if quest.Quest == 'Craft Armor':
                    if len(Armors) > 0:
                        quest.nownum += 1
                if quest.Quest == 'Craft Sword':
                    if len(MeeleWeapons) > 0:
                        quest.nownum += 1
