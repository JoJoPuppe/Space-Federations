def start(table, x = 0, y = 0):
    cards = table.create('31000a40-f835-4d50-8e76-d41266250004', 6, 100, quantity = 4, persist = True)
    for card in cards:
        notify("{} created {}.".format(me, card))
        card.moveTo(me.piles['Base'])
    cards = table.create('31000a40-f835-4d50-8e76-d41266250000', 6, 100, quantity = 3, persist = True)
    for card in cards:
        notify("{} created {}.".format(me, card))
        card.moveTo(me.piles['Base'])
    cards = table.create('31000a40-f835-4d50-8e76-d41266250011', 26, 100, quantity = 7, persist = True)
    for card in cards:
        notify("{} created {}.".format(me, card))
        card.moveTo(me.piles['Base'])
        me.piles['Base'].shuffle()
        shared.piles['Market'].shuffle()
	
def sitstand(group, x = 0, y = 0):
    isstanding = me.getGlobalVariable("standing")
    if isstanding == "1":
        notify("{} is now sitting.".format(me))
        me.setGlobalVariable("standing","0")
    else:
        notify("{} is now standing.".format(me))
        me.setGlobalVariable("standing","1")

def ssstatus(group, x = 0, y = 0):
    notify("Getting sit stand")
    for p in players:
        gv = p.getGlobalVariable("standing")
        if gv == "1":
            notify("{} is standing.".format(p))
        else:
            notify("{} is sitting.".format(p))

def becomedealer(group,x=0,y=0):
    notify("{} is now dealer.".format(me))
    setGlobalVariable("dealer",me._id)

def whosdealer(group,x=0,y=0):
    ret = getGlobalVariable("dealer")
    notify("{} dealer num".format(ret))
    ret = int(ret)
    notify("{} dealer num".format(ret))
    for p in players:
        if p._id == ret:
            notify("{} is dealer.".format(p))
            break

def listplayers(group, x = 0, y = 0):
    notify("{}".format(players))

def interrupt(group, x = 0, y = 0):
    notify('{} interrupts the game.'.format(me))

def passturn(group, x = 0, y = 0):
    notify('{} End TURN'.format(me))

def tap(card, x = 0, y = 0):
  mute()
  card.orientation ^= Rot90
  if card.orientation & Rot90 == Rot90:
    notify('{} turns {} sideways'.format(me, card))
  else:
    notify('{} turns {} upright'.format(me, card))

def flip(card, x = 0, y = 0):
    mute()
    if card.isFaceUp == True:
      notify("{} flips {} face down.".format(me, card))
      card.isFaceUp = False
    else:
      card.isFaceUp = True
      notify("{} flips {} face up.".format(me, card))

def discard(card, x = 0, y = 0):
  mute()
  src = card.group
  fromText = " from the table" if src == table else " from their " + src.name
  card.moveTo(me.Discard)
  notify("{} discards {}{}.".format(me, card, fromText))
  
def discardRnd(group, x = 0, y = 0):
  mute()
  if len(me.hand) == 0 : return 
  randomCard = len(me.hand)
  rC = rnd(0, randomCard - 1)
  notify("{}".format(rC))
  me.hand[rC].moveTo(me.Discard)
  notify("{} discards a random Card.".format(me))

def highlightcard(card, x = 0, y = 0):
  mute()
  if card.highlight == "#ff0000":
    card.highlight = None
    notify('{} removes highlight from {}'.format(me, card))
  else:
    card.highlight = "#ff0000"
    notify('{} highlights {}'.format(me, card))

def drawBase(group, x = 0, y = 0):
    if len(me.piles['Base']) == 0: return
    mute()
    me.piles['Base'][0].moveTo(me.hand)
    notify("{} draws a card.".format(me))
	
def drawMarket(group, x = 0, y = 0):
    if len(shared.piles['Market']) == 0: return
    mute()
    shared.piles['Market'][0].moveTo(me.hand)
    notify("{} draws a card.".format(me))
	
def drawDamage(group, x = 0, y = 0):
    if len(shared.piles['Damage']) == 0: return
    mute()
    shared.piles['Damage'][0].moveTo(me.hand)
    notify("{} draws a card.".format(me))

def drawManyBase(group, count = None):
    if len(me.piles['Base']) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 7)
    for c in me.piles['Base'].top(count): c.moveTo(me.hand)
    notify("{} draws {} cards.".format(me, count))
	
def dealManyMarket(group, count=None):
    dealerid = int(getGlobalVariable("dealer"))
    if me._id != dealerid:
        whisper("You are not the dealer player.")
        return
    if len(shared.piles['Market']) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards?", 5)
    for num in range(count):
        for p in players:
            standing = int(p.getGlobalVariable("standing"))
            if standing == 0:
                notify("Dealing {} a card.".format(p))
                for c in shared.piles['Market'].top(1): c.moveTo(p.hand)

def dealManyToTableMarket(group, x = 0, y = 0, count=None):
    if len(shared.piles['Market']) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards to table?", 6)
    for c in shared.piles['Market'].top(count): 
        c.moveTo(table)
    notify("Dealing {} cards to table.".format(count))

def mill(group, count = None):
    if len(shared.Deck) == 0: return
    mute()
    if count == None: count = askInteger("Mill how many cards?", 1)
    for c in shared.Deck.top(count): c.moveTo(shared.Discard)
    notify("{} mills the top {} cards from the Deck.".format(me, count))

def shuffleBase(group, x = 0, y = 0):
   mute()
   me.piles['Base'].shuffle()
   notify("{} shuffled the.".format(me))
   
def shuffleMarket(group, x = 0, y = 0):
   mute()
   shared.piles['Market'].shuffle()
   notify("{} shuffled.".format(me))

def shuffleIntoDeck(group, x = 0, y = 0):
    mute()
    for c in group: c.moveTo(me.piles['Base'])
    me.piles['Base'].shuffle()
    notify("{} shuffled the service into the base.".format(me))

def lookAndTake(group, x = 0, y = 0) :
    shared.piles['Dock'].lookAt(0)