# Description: This script will create poison and apply it to a dagger
# Version: 1.0

# Init Macro loop
while True:
    # Backpack
    backpack = Player.Backpack.Serial
    # Daggers list in the backpack
    daggers = Items.FindAllByID(0x0F51, -1, backpack, -1)
    Misc.Pause(500)
    # Poisons list in the backpack
    potions = Items.FindAllByID(0x0F0A, -1, backpack, -1)
    # Check if there are poisons in the backpack
    if len(potions) < 1:
        # Create a poison
        Items.UseItemByID(0xe9b, 0)
        Gumps.WaitForGump(0x4dc, 10000)
        Misc.Pause(500)
        Gumps.SendAction(0x4dc, 1)
        Gumps.WaitForGump(0x4dc, 10000)
        Misc.Pause(500)
        Gumps.SendAction(0x4dc, 404)
        Gumps.WaitForGump(0x4dc, 10000)
        Misc.Pause(500)
        Gumps.SendAction(0x4dc, 611) #sostituire tipo di pozione
        Gumps.WaitForGump(0x4dc, 10000)
        Misc.Pause(500)
        Gumps.SendAction(0x4dc, 0)
        Misc.SendMessage("Potion Created")
    else:
        # Use the first poison in the backpack
        potion = potions[0]
        # Use the first dagger in the backpack
        dagger = daggers[0]
        # Apply the poison to the dagger
        Misc.SendMessage("Potion already present")
        Items.UseItem(potion.Serial)
        Target.WaitForTarget(1000)  
        Misc.Pause(500)
        Target.TargetExecute(dagger)   
        Target.Cancel()
        
    Misc.Pause(4000)