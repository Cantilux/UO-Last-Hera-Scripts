import sys

# Lista degli incantesimi di buff da lanciare
buff_list = ['Bless', 'Protection']
# rimuove le armi dalle mani
right_item = Player.GetItemOnLayer('RightHand')
left_item = Player.GetItemOnLayer('LeftHand')
if right_item != None:
    Player.UnEquipItemByLayer('RightHand',100)
if left_item != None:
    Player.UnEquipItemByLayer('LeftHand',100)
Misc.Pause(200)
# Ciclo per i buff
for buff in buff_list:
    # Verifica se il buff è già attivo
    if Player.BuffsExist(buff) == False:
        # Lancio del buff
        Spells.Cast(buff)
        Target.WaitForTarget(500, False)
        # Target su se stesso
        Target.Self()
        Misc.Pause(4000)
    Misc.Pause(200)
# Verifica se il player ha bisogno di cure
if Player.Hits < Player.HitsMax:
    Spells.Cast('Heal')
    Target.WaitForTarget(1000, False)
    Target.Self()
    Misc.Pause(5000)
Misc.Pause(200)
# Equipaggia le armi precedentemente rimosse
if right_item != None:
    Items.UseItem(right_item)
    Target.WaitForTarget(500, True)
    Target.Cancel()
    Misc.Pause(500)
if left_item != None:
    Items.UseItem(left_item)
    Target.WaitForTarget(500, True)
    Target.Cancel()
    Misc.Pause(500)
Misc.Pause(200)
# Verifica se il player ha bisogno di mana
if Player.Mana < Player.ManaMax:
    # Utilizza la skill di meditazione
    Player.UseSkill('Meditation')
    
sys.exit(99)