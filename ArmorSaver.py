dicto = dict()
armors = int
dicto['LeatherArmor'] = (6,'Images/Armor/LeatherArmor.png','Images/Inventory/ArmorIco.png','Images/Armor/EquipedLeatherArmor.png','Images/Armor/LeatherArmor1.png','LeatherArmor')
def openarmor(Armors,Armor):
    with open('Armors.txt','r') as f:
        armors = int(f.readline().strip( '\n' ))
        for i in range(armors):
            Armor = Armor(dicto[f.readline().strip( '\n' )],Armors)
def savearmor(Armors):
    with open('Armors.txt','w') as f:
        f.write(str(len(Armors) + '\n'))
        for arm in Armors:
            f.write(arm.name + '\n')
