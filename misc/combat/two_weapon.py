# Description: This script will equip a primary weapon and shield if no weapons are equipped, or equip a secondary weapon if a primary weapon is equipped.
# Version: 1.0

# Import the system module
import sys
# Primary weapon
primary = Items.FindByID(0x2D27, -1, Player.Backpack.Serial) #scimitar
# Secondary weapon
secondary = Items.FindByID(0x143E, -1, Player.Backpack.Serial) #halberd
# Shield
shield = Items.FindByID(0x1B7B, -1, Player.Backpack.Serial) #shield

# Function to unequip hands
def unequip():
    if Player.CheckLayer('LeftHand'):
        Player.UnEquipItemByLayer('LeftHand', 500)
        Misc.Pause(500)
    if Player.CheckLayer('RightHand'):
        Player.UnEquipItemByLayer('RightHand', 500)
        Misc.Pause(500)

# Function to equip primary weapon and shield
def equipPrimary():
    unequip()
    Player.EquipItem(primary)
    Misc.Pause(500)
    Player.EquipItem(shield)
    Misc.Pause(500)

# Function to equip secondary weapon
def equipSecondary():
    unequip()
    Player.EquipItem(secondary)
    

# Check if no weapons are equipped
if Player.CheckLayer('LeftHand') == False and Player.CheckLayer('RightHand') == False:
    equipPrimary()
    sys.exit()
# Check if a primary weapon is equipped
if Player.CheckLayer('LeftHand') == False and Player.CheckLayer('RightHand') == True:
    equipPrimary()
    sys.exit()
# Check if a secondary weapon is equipped
elif Player.CheckLayer('LeftHand') == True and Player.CheckLayer('RightHand') == False:
    equipPrimary()
    sys.exit()
# Check if both hands are equipped
elif Player.CheckLayer('LeftHand') == True and Player.CheckLayer('RightHand') == True:
    equipSecondary()
    sys.exit()