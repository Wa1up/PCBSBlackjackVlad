from operator import le
from selectors import EpollSelector
from telnetlib import PRAGMA_HEARTBEAT
from xmlrpc.client import TRANSPORT_ERROR
from cards import originaldeck#, originaldecklen
from players import Player, botnames
from random import randint, random, randrange, choice

def giverandomcard():
    originaldecklen = len(originaldeck) - 1
    randomcard = randint(0, originaldecklen)
    #print(f"randomcard(number):{randomcard}, originaldecklen: {originaldecklen}", )
    saverandomcard = originaldeck[randomcard]
    originaldeck.remove(originaldeck[randomcard])
    return(saverandomcard)
    

croupier = Player(deck=[], score=0, name="Croupier")
player = Player(deck=[], score=0, name="Player")
bot1 = Player(deck=[], score=0, name=None)
bot2 = Player(deck=[], score=0, name=None)
bot3 = Player(deck=[], score=0, name=None)
botlist = [bot1, bot2, bot3]
botswhichplay = []

def showscore(pleya):
    number = checkoutace(pleya=player) * 10
    if checkoutace(pleya=pleya) != 0:
        if pleya.score + number > 21:
            print(f"{pleya.name} score is:{pleya.score}\n\n\n")
        elif pleya.score + number < 21:
            alternativeplayerscore = pleya.score + 10
            print(f"{pleya.name} score is {pleya.score}/{alternativeplayerscore}\n\n\n")
        elif pleya.score + number == 21:
            alternativeplayerscore = pleya.score + 10
            print(f"{pleya.name} score is {pleya.score}/{alternativeplayerscore}\n\n\n")
        else:
            print("something wrong")
    else:
        print(f"\n{pleya.name} score is:{pleya.score}\n\n\n")

def startgame():
    howmanybots = int(input("How many bots? maximum amount is 3(5 players in general): "))
    croupier.deck.append(giverandomcard())
    croupier.deck.append(giverandomcard())
    player.deck.append(giverandomcard())
    player.deck.append(giverandomcard())
    if howmanybots > 0:
        createbots(botcount=howmanybots)
        for bot in botswhichplay:
            bot.deck.append(giverandomcard())
            bot.deck.append(giverandomcard())
    else:
        pass
    
def showwhatsondeck():
    try:
        for botix in botswhichplay:
            print(f"{botix.name} have: ")
            for card in botix.deck:
                if card == botix.deck[0]:
                    print("???")
                else:
                    print(f"{card.name} {card.suit}")
            print("\n")
    except:
        pass

    print("Croupier have: ")
    for x in croupier.deck:
        if x == croupier.deck[0]:
            print("???")
        else:
            print(f"{x.name} {x.suit}")
    
    print("\n")
    print("You have:")
    for i in player.deck:
        print(f"{i.name} {i.suit}")

    showscore(pleya=player)
    

def showwhatsondeckfull():
    try:
        for botix in botswhichplay:
            print(f"{botix.name} have: ")
            for card in botix.deck:
                print(f"{card.name} {card.suit}")
            showscore(pleya=botix)
        print("\n")
    except:
        pass
    
    print("Croupier have: ")
    for x in croupier.deck:
        print(f"{x.name} {x.suit}")
    showscore(pleya=croupier)

    print("\n\nYou have:")
    for i in player.deck:
        print(f"{i.name} {i.suit}")
    showscore(pleya=player)

def hit():
    print("\n\nYou hit!\n\n")
    player.deck.append(giverandomcard())

def stand():
    print("\n\nYou stand!\n\n")
    pass

def checkoutace(pleya):
    while True:
        toret = 0
        for vc in pleya.deck:
            if vc.name == "Ace":
                toret += 1
            else:
                pass
        if toret == 0:
            return 0
        elif toret == 1:
            return 1
        else:
            return toret

        #1- 1 ace present 0-ace absent torret - x amount of ace we have
        
            
def showup():
    showwhatsondeckfull()
    wholeft = [player, croupier]
    allscores = []
    try:
        for neveiuf in botswhichplay:
            wholeft.append(neveiuf)
    except:
        pass
    
    for lefter in wholeft:
        if checkoutace(pleya=lefter) == 0:
            #print(f"{lefter.name} scores added")
            allscores.append(lefter.score)
        else:
            if lefter.score + (checkoutace(pleya=lefter) * 10) < 21 or lefter.score + (checkoutace(pleya=lefter) * 10) == 21:
                lefter.score += checkoutace(pleya=lefter) * 10
                allscores.append(lefter.score)
            else:
                allscores.append(lefter.score)
                
    allscores.sort(reverse=True)
    for jucy in wholeft:
        if jucy.score == allscores[0]:
            print(f"{jucy.name} won")
'''
    print("Croupier have: ")
    for x in croupier.deck:
        print(f"{x.name} {x.suit}")
    
    print(f"Croupier score: {croupier.score}")

    print("\n\nYou have:")
    for i in player.deck:
        print(f"{i.name} {i.suit}")
    
    
    if checkoutace(pleya=player) == 1 or checkoutace(pleya=player) > 1:
        number = checkoutace(pleya=player) * 10
        if player.score + number > 21:
            print(f"Your score is: {player.score}\n\n\n")
        elif player.score + number < 21:
            alternativeplayerscore = player.score + 10
            print(f"Your score is: {alternativeplayerscore}\n\n\n")
        elif player.score + number == 21:
            print(f"Your score is: {player.score}\nBLACKJACK!")
        else:
            print("something wrong")
    else:
        print(f"\nYour score is:{player.score}\n\n\n")

    
    if checkoutace(pleya=player) == 1:
        if player.score + number < 21:
            player.score += number
        elif player.score + number > 21:
            pass
        elif player.score + number == 21:
            player.score = 21
            print("BLACKJACK!")
            pass
    else:
        pass
    if player.score > croupier.score:
        print(f"{player.name} wins!")
    elif player.score < croupier.score:
        print(f"{player.name} lose!")
    else:
        print("push")
'''

def updatescore(person):
    person.score = 0
    for x in person.deck:
        person.score += x.points

wholost = []
whowon = []

def ifplayerlost(pleyya):
        if pleyya.score > 21: 
            print(f"\n{pleyya.name} lost!")
            if pleyya == player or pleyya == croupier:
                showscore(pleya=pleyya)
            else:
                print("He had")
                for t in pleyya.deck:
                    print(f"{t.name}, {t.suit}")
                showscore(pleya=pleyya)
            return True
        else:
            return False

def dowehavealoser():
    if ifplayerlost(pleyya=player) == True:
        #print(f"{player.name} lost!")
        wholost.append(player)
    else:
        pass
    if ifplayerlost(pleyya=croupier) == True:
        #print(f"{croupier.name} lost!")
        wholost.append(croupier)
    else:
        pass
    for bottolose in botswhichplay:
        if ifplayerlost(pleyya=bottolose) == True:
            #print(f"{bottolose.name} lost!")
            if bottolose in wholost:
                pass
            else:
                wholost.append(bottolose)
        else:
            pass

def dowehaveawinner():
    # 0 - we do have 1 = no we dont
    competitors = []

    def ifplayerinstawin(pleyaa, pleyaascore):
        if pleyaascore == 21:
            #showwhatsondeckfull()
            print(f"{pleyaa.name} win!")
            return True
        else:
            return False
    

    if checkoutace(pleya=player) == 0:
        pass
    else:
        alternativeplayerscore = player.score + (checkoutace(pleya=player) * 10)
        if ifplayerinstawin(pleyaa=player, pleyaascore=alternativeplayerscore) == False:
            pass
        else:
            print(f"{player.name} got himself a blackjack!")
            #for card in player.deck:
                #print(f"{card.name} {card.suit}")
            print("\n")
            whowon.append(player)
    
    if checkoutace(pleya=croupier) == 0:
        pass
    else:
        alternativecroupscore = croupier.score + (checkoutace(pleya=croupier) * 10)
        if ifplayerinstawin(pleyaa=croupier, pleyaascore=alternativecroupscore) == False:
            pass
        else:
            print(f"{croupier.name} got himself a blackjack!")
            print("He had: ")
            for card in croupier.deck:
                (f"{card.name} {card.suit}")
            print(f"{showscore(pleya=croupier)}\n")
            whowon.append(croupier)
    
    for botix in botswhichplay:
        if checkoutace(pleya=botix) == 0:
            pass
        else:
            alternativebotixscore = botix.score + (checkoutace(pleya=botix) * 10)
            if ifplayerinstawin(pleyaa=botix, pleyaascore=alternativebotixscore) == False:
                pass
            else:
                print(f"{botix.name} got himself a blackjack!")
                for card in botix.deck:
                    print(f"{card.name} {card.suit}")
                print("\n")
                whowon.append(botix)

'''    
    try:
        #for winner in whowon:
        #    print(winner.name)
        return 1337
    except:
        print("No blackjacks for today")
        return 1
'''        
 
def playermoves():
    while True:
        try:
            ask = int(input("what do u want to do next? type 1 to hit and 2 to stand: "))
        except:
            print("incorrect input")
        if ask == 1:
            hit()
            updatescore(player)
            if player.score > 21:
                showwhatsondeck()
                break
            elif player.score == 21:
                showwhatsondeck()
                break
            else:
                showwhatsondeck()
        elif ask == 2:
            stand()
            break
        
def botmoves(bot):
    alternativescore = 0 #0 - no 1 - yes

    while True:
        if bot.score > 20:
            #print("break > 20")
            break
        elif bot.score < 16:
                bot.deck.append(giverandomcard())
                #print("card taken by bot")
                updatescore(bot)
        elif bot.score < 20:
            randchoice = randint(0, 1)
            if randchoice == 0:
                bot.deck.append(giverandomcard())
                #print("card taken by bot(bet take)")
                updatescore(bot)
            else:
                #print("else")
                break
        else:
            break                


def createbots(botcount):
    for i in range(0, botcount):
        xc = botlist[i]
        xc.name = choice(botnames)
        botswhichplay.append(xc)
