import sys

# Funzione per smontare da cavallo
def dismount():
    if Player.Mount != None:
        Mobiles.UseMobile(Player.Serial)

# Funzione per montare cavallo        
def ride():
    if Player.Mount == None:
        creatures = Mobiles.ApplyFilter(Mobiles.Filter())
        filterPet = Mobiles.Filter()
        filterPet.IgnorePets = True
        filtered = Mobiles.ApplyFilter(filterPet)
        for creature in creatures:
            if creature not in filtered:
                Mobiles.UseMobile(creature)
                sys.exit(99)

# Funzione per equipaggiare l'accetta
def equip_hatchet(hatchet):
    layer = Player.GetItemOnLayer('LeftHand')
    if layer != None:
        if Player.CheckLayer('LeftHand'):
            Player.UnEquipItemByLayer('LeftHand',100)
        if Player.CheckLayer('RightHand'):
            Player.UnEquipItemByLayer('RightHand',100)
        Misc.Pause(500)
    Player.EquipItem(hatchet)

# Funzione per tagliare gli alberi 
def chop_tree_tiles():
    # Ciclo per i tile vicini al player
    for x in range(-1, 2):
        for y in range(-1, 2):
            target_x = Player.Position.X + x
            target_y = Player.Position.Y + y
            target_z = Player.Position.Z
            tile = Statics.GetStaticsTileInfo(target_x, target_y, target_z)
            if len(tile) > 1:
                tileId = tile[0].StaticID
                # Verifica se il tile è un albero
                if Statics.GetTileFlag(tileId, 'Impassable') and Statics.GetTileFlag(tileId, 'Foliage'):
                    # Scende da cavallo
                    dismount()
                    # Equipaggia l'accetta
                    Items.UseItem(hatchet)
                    Target.WaitForTarget(500, False)
                    # Taglia l'albero
                    Target.TargetExecute(Player.Position.X + x, Player.Position.Y + y, Player.Position.Z, tileId)
    

# Zaino
backpack = Player.Backpack.Serial
# Lista delle accette nello zaino
hatchets = Items.FindAllByID(0x0F43, -1, backpack, -1)
# Verifica se ci sono accette nello zaino
if len(hatchets) > 0:
    # Accetta
    hatchet = hatchets[0]
    equip_hatchet(hatchet)
    stop_chop = False
    # Peso massimo
    max_weight = Player.MaxWeight - 10
    Journal.Clear()
    # Ciclo per tagliare gli alberi
    while stop_chop == False:
        # Verifica se c'è ancora legna da tagliare
        if Journal.Search("There is nothing here to chop") == True:
            Player.ChatSay("Non c'è niente qui da tagliare")
        # Verifica se il peso è maggiore del peso massimo
        if Player.Weight >= max_weight:
            stop_chop = True
            Player.ChatSay("Peso Massimo Raggiunto")
        # Taglia gli alberi
        chop_tree_tiles()
        Misc.Pause(6000)
    # Monta cavallo
    ride()
else:
    Player.ChatSay("0 Accette nello zaino")

sys.exit(99)