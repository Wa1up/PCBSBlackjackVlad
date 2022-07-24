class Card:
    def __init__(self, name, suit, points):
        self.name = name
        self.suit = suit
        self.points = points
    def __str__(self):
        return self.name, self.suit

heart2 = Card(name=2, suit="hearts", points=2)
heart3 = Card(name=3, suit="hearts", points=3)
heart4 = Card(name=4, suit="hearts", points=4)
heart5 = Card(name=5, suit="hearts", points=5)
heart6 = Card(name=6, suit="hearts", points=6)
heart7 = Card(name=7, suit="hearts", points=7)
heart8 = Card(name=8, suit="hearts", points=8)
heart9 = Card(name=9, suit="hearts", points=9)
heart10 = Card(name=10, suit="hearts", points=10)
heartjack = Card(name="Jack", suit="hearts", points=10)
heartqueen = Card(name="Queen", suit="hearts", points=10)
heartking = Card(name="King", suit="hearts", points=10)
heartace = Card(name="Ace", suit="hearts", points=1)

tiles2 = Card(name=2, suit="tiles", points=2)
tiles3 = Card(name=3, suit="tiles", points=3)
tiles4 = Card(name=4, suit="tiles", points=4)
tiles5 = Card(name=5, suit="tiles", points=5)
tiles6 = Card(name=6, suit="tiles", points=6)
tiles7 = Card(name=7, suit="tiles", points=7)
tiles8 = Card(name=8, suit="tiles", points=8)
tiles9 = Card(name=9, suit="tiles", points=9)
tiles10 = Card(name=10, suit="tiles", points=10)
tilesjack = Card(name="Jack", suit="tiles", points=10)
tilesqueen = Card(name="Queen", suit="tiles", points=10)
tilesking = Card(name="King", suit="tiles", points=10)
tilesace = Card(name="Ace", suit="tiles", points=1)

clovers2 = Card(name=2, suit="clovers", points=2)
clovers3 = Card(name=3, suit="clovers", points=3)
clovers4 = Card(name=4, suit="clovers", points=4)
clovers5 = Card(name=5, suit="clovers", points=5)
clovers6 = Card(name=6, suit="clovers", points=6)
clovers7 = Card(name=7, suit="clovers", points=7)
clovers8 = Card(name=8, suit="clovers", points=8)
clovers9 = Card(name=9, suit="clovers", points=9)
clovers10 = Card(name=10, suit="clovers", points=10)
cloversjack = Card(name="Jack", suit="clovers", points=10)
cloversqueen = Card(name="Queen", suit="clovers", points=10)
cloversking = Card(name="King", suit="clovers", points=10)
cloversace = Card(name="Ace", suit="clovers", points=1)

pikes2 = Card(name=2, suit="pikes", points=2)
pikes3 = Card(name=3, suit="pikes", points=3)
pikes4 = Card(name=4, suit="pikes", points=4)
pikes5 = Card(name=5, suit="pikes", points=5)
pikes6 = Card(name=6, suit="pikes", points=6)
pikes7 = Card(name=7, suit="pikes", points=7)
pikes8 = Card(name=8, suit="pikes", points=8)
pikes9 = Card(name=9, suit="pikes", points=9)
pikes10 = Card(name=10, suit="pikes", points=10)
pikesjack = Card(name="Jack", suit="pikes", points=10)
pikesqueen = Card(name="Queen", suit="pikes", points=10)
pikesking = Card(name="King", suit="pikes", points=10)
pikesace = Card(name="Ace", suit="pikes", points=1)

redjoker = Card(name="Jocker", suit=None, points=None)
blackjocker = Card(name="Jocker", suit=None, points=None)

originaldeck = [heart2, heart3, heart4, heart5, heart6, heart7, heart8, heart9, heart10, heartjack, heartqueen, heartking, heartace,
tiles2, tiles3, tiles4, tiles5, tiles6, tiles7, tiles8, tiles9, tiles10, tilesjack, tilesqueen, tilesking, tilesace,
clovers2, clovers3, clovers4, clovers5, clovers6, clovers7, clovers8, clovers9, clovers10, cloversjack, cloversqueen, cloversking, cloversace,
pikes2, pikes3, pikes4, pikes5, pikes6, pikes7, pikes8, pikes9, pikes10, pikesjack, pikesqueen, pikesking, pikesace]
# jokers not in use now



