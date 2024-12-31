# Description: This script will cast buffs and bandage the player
# Version: 1.1

# Import the system module
import sys
# Buffs
spellsList = ['Bless', 'Protection', 'Reactive Armor']
# Unequip hands
left = Player.GetItemOnLayer('LeftHand')
right = Player.GetItemOnLayer('RightHand')
if Player.CheckLayer('LeftHand'):
    Player.UnEquipItemByLayer('LeftHand',100)
if Player.CheckLayer('RightHand'):
    Player.UnEquipItemByLayer('RightHand',100)
Misc.Pause(200)
# Cast spells
for spell in spellsList:
    if Player.BuffsExist(spell) == False:
        Spells.Cast(spell)
        Target.WaitForTarget(1000, False)
        Target.Self()
        Misc.Pause(4000)
    Misc.Pause(200)

# Bandages
print("Bende")

Items.UseItemByID(0x0E21,0x0000)
Target.WaitForTarget(1000, False)
Target.Self()
Misc.Pause(10000)
# Equip hands
if left:
    Player.EquipItem(left)
    Misc.Pause(500)
if right:
    Player.EquipItem(right)
    Misc.Pause(500)
    
sys.exit(99)