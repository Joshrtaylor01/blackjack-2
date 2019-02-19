import random

endGame = False

Ace = int()
vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, Ace, 2, 3, 4, 5, 6, 7, 8,
        9, 10, 10, 10, 10, Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, Ace]

cards = ['Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades', 'Six of Spades', 'Seven of Spades',
         'Eight of Spades', 'Nine of Spades', 'Ten of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades',
         'Ace of Spades', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 'Five of Hearts', 'Six of Hearts',
         'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts', 'Jack of Hearts', 'Queen of Hearts',
         'King of Hearts', 'Ace of Hearts', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs',
         'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs', 'Jack of Clubs',
         'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds',
         'Five of Diamonds', 'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds',
         'Ten of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds']


class Player:
    def __init__(self, score, bust, hold):
        self.score: int = score
        self.bust: bool = bust
        self.hold: bool = hold


P = Player(0, False, False)
D = Player(0, False, False)


def deal_card():
    if not P.hold:
        deal = str(input("draw? [y/n]: "))
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
            P.score += c
            print(P.score)
            cards.pop(r)
            vals.pop(r)
        elif deal == 'n':
            P.hold = True


def dealer_draw():
    if not D.hold and not P.bust:
        if D.score <= 17:
            r = random.randint(0, len(vals))
            w = vals[r]
            D.score += w
            cards.pop(r)
            vals.pop(r)
        else:
            D.hold = True


def is_bust(score):
    if score > 21:
        return True


def check_win():
    global endGame
    if is_bust(P.score) and is_bust(D.score):
        print("P: ", P.score, "D: ", D.score)
        print("both of you lost, lol")
        endGame = True
    elif P.score == 21 or not is_bust(P.score) and is_bust(
            D.score) or P.score > D.score and D.hold:
        print("P: ", P.score, "D: ", D.score)
        print(name, 'wins! Good Job!')
        endGame = True
    elif D.score == 21 or is_bust(P.score) and not is_bust(
            D.score) or P.score < D.score and P.hold:
        print("P: ", P.score, "D: ", D.score)
        print("Dealers win! Rough Luck :(")
        endGame = True


print("Lets play Black jack!")
name = str(input("name?: "))

while not endGame:
    deal_card()
    is_bust(P.score)
    dealer_draw()
    is_bust(D.score)
    check_win()