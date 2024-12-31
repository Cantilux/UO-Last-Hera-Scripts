# Description: This script will heal the player using the Magery skill.
# Version: 1.0

# save the last attack target
lastAttack = Target.GetLastAttack()
# unequip hands
left = Player.GetItemOnLayer('LeftHand')
right = Player.GetItemOnLayer('RightHand')
if Player.CheckLayer('LeftHand'):
    Player.UnEquipItemByLayer('LeftHand',100)
if Player.CheckLayer('RightHand'):
    Player.UnEquipItemByLayer('RightHand',100)
Misc.Pause(200)
# cast spells
Spells.Cast('Heal')
Target.WaitForTarget(1000, False)
Target.Self()
Misc.Pause(4000)
# re-equip hands
if left:
    Player.EquipItem(left)
    Misc.Pause(500)
if right:
    Player.EquipItem(right)
    Misc.Pause(500)

# player is in war mode
Player.SetWarMode(True)
# attack the last attack target
Player.Attack(lastAttack)