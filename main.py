from logic import *





while True:
    startgame()
    updatescore(croupier)
    updatescore(player)
    for bot in botswhichplay:
        updatescore(bot)
    showwhatsondeck()
    dowehaveawinner()
    if player in whowon:
        showwhatsondeckfull()
        break
    if croupier in whowon:
        showwhatsondeckfull()
        break
    try:
        for winner in whowon:
            botswhichplay.remove(winner)
    except:
        pass
    playermoves()
    if player in wholost:
        break
    botmoves(bot=croupier)
    for botix in botswhichplay:
        botmoves(bot=botix)
    #showwhatsondeck()
    dowehaveawinner()
    dowehavealoser()
    if croupier in wholost:
        break
    else:
        pass
    try:
        for loser in wholost:
            botswhichplay.remove(loser)
    except:
        pass
    #print("\n WHOLOSTLIST")
    #for ii in wholost:
        #print(ii.name)
    if player in whowon:
        showwhatsondeckfull()
        break
    if croupier in whowon:
        showwhatsondeckfull()
        break
    try:
        for winner in whowon:
            botswhichplay.remove(winner)
    except:
        pass
    showup()
    break
