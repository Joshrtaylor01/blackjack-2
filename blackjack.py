import random
dealerBust = False
playerBust = False
playerHold = False
dealerHold = False
endGame = False
King = Queen = Jack = 10
Ace = 1

vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, Ace]
cards = ['Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades', 'Six of Spades', 'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 'Five of Hearts', 'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs', 'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds', 'Five of Diamonds', 'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds', 'Ten of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds']
dealerScore = 0
playerScore = 0


def deal_card():
    global playerScore
    global playerHold
    if not playerHold:
        deal = str(input("draw? [1/0]: "))
        if deal == 'y':
            r = random.randint(0, len(vals))
            c = vals[r]
            print(name, 'got a', cards[r])
            if vals[r] == Ace:
                hl = int(input('Do you want it to be a 11 or 1?'))
                if hl == 1 or hl == 11:
                    c = hl
                else:
                    global endGame
                    print("you big fact cheat, you lose")
                    endGame = True
            playerScore += c
            print(playerScore)
            cards.pop(r)
            vals.pop(r)
        elif deal == 'n':
            playerHold = True


def dealerDraw():
    global dealerHold
    global dealerScore
    if not dealerHold and not playerBust:
        if dealerScore <= 17:
            r = random.randint(0, len(vals))
            w = vals[r]
            dealerScore += w
            cards.pop(r)
            vals.pop(r)
        else:
            dealerHold = True


def isBust(score):
    if score > 21:
        return True


def checkWin(dealerScore, playerScore):
    global endGame
    if isBust(playerScore) and isBust(dealerScore):
        print("P: ", playerScore, "D: ", dealerScore)
        print("both of you lost, lol")
        endGame = True
    elif playerScore == 21 or not isBust(playerScore) and isBust(dealerScore) or playerScore > dealerScore and dealerHold:
        print("P: ", playerScore, "D: ", dealerScore)
        print(name, 'wins! Good Job!')
        endGame = True
    elif dealerScore == 21 or isBust(playerScore) and not isBust(dealerScore) or playerScore < dealerScore and playerHold:
        print("P: ", playerScore, "D: ", dealerScore)
        print("Dealers win! Rough Luck :(")
        endGame = True


print("Lets play Black jack!")
name = str(input("name?: "))


while not endGame:
    deal_card()
    isBust(playerScore)
    dealerDraw()
    isBust(playerScore)
    isBust(dealerScore)
    checkWin(dealerScore, playerScore)