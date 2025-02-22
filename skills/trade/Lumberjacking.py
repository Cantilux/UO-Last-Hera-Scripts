# posizione del pg
player_x = Player.Position.X
player_y = Player.Position.Y
position_x = Player.Position.X
position_y = Player.Position.Y
tileLists = []
# controlla che ci siano oggetti nei tile adiacenti
for x in [-1, 0, 1]:
    position_x = player_x + x
    for y in [-1, 0, 1]:
        position_y = player_y + y
        tiles = Statics.GetStaticsTileInfo(position_x, position_y ,0)
        if len(tiles) >= 1:
            for t in tiles:
                tileLists.append([position_x, position_y, t.StaticID])
                
# inizia la verifica se c'è almeno un oggetto
if len(tileLists) >= 1:
    # per ogni tile in lista
    for tile in tileLists:
        # controlla che l'oggetto nel tile sia un albero
        if Statics.GetTileFlag(tile[2], 'Impassable') and Statics.GetTileFlag(tile[2], 'Foliage'):
            # serve per evitare errori
            Journal.Clear()
            # inizia a tagliare finché un albero non si esaurisce
            max_weight = Player.MaxWeight - 10
            chop = True
            while chop:
                item = Player.GetItemOnLayer('LeftHand')
                Items.UseItem(item)
                Target.WaitForTarget(1000, False)
                Target.TargetExecute(tile[0], tile[1] ,0, tile[2])
                Misc.Pause(500)
                if Journal.Search("There is nothing here to chop.") == True:
                    chop = False
                    break
                if Journal.Search("That is too far away.") == True:
                    chop = False
                    break
                if Journal.Search("It appears immune to your blow") == True:
                    chop = False
                    break
                if Player.Weight >= max_weight:
                    chop = False
                    Player.ChatSay("Peso Massimo Raggiunto")
                    break
                else:
                    Misc.Pause(8000)
