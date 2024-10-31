import BalckJack_Art as BJA
import time
import random as Ran
import os

Cards = [11, 10, 2, 3, 4, 5, 9, 10, 6, 7, 8, 10, 10]

def DeckDeal():
    os.system('cls')
    print(BJA.logo)
    Player_Cards = []
    Dealer_Cards = []
    for i in range(1,3):
        C = Ran.randint(0,12)
        D = Ran.randint(0,12)
        Player_Cards.append(Cards[C])
        Dealer_Cards.append(Cards[D])
    print(f"Your Cards Are:- {Player_Cards}")
    print(f"Dealer Cards Are:- {Dealer_Cards[0]} ❓ ")
    time.sleep(3)
    Game(Player_Cards,Dealer_Cards)

def Game(P,D):
    os.system('cls')
    print(BJA.logo)
    Player_Cards = P
    Dealer_Cards = D
    print(f"Your Cards Are:- {Player_Cards}")
    print(f"Dealer Cards Are:- {Dealer_Cards[0]} ❓ ")
    response = input(" 'g' to Grab A new Card | 's' Stand With your Current Crad ")
    if response == 's':
        if sum(Player_Cards) == 21:
            print(f"Dealer Cards Were {Dealer_Cards} ")
            Win(True)
        elif sum(Dealer_Cards) == 21:
            print(f"Dealer Cards Were {Dealer_Cards} ")
            Bust(True)
        elif sum(Player_Cards) > sum(Dealer_Cards):
            print(f"Dealer Cards Were {Dealer_Cards} ")
            Win(True)
        elif sum(Player_Cards) == sum(Dealer_Cards):
            print("Draw")
            print(f"Dealer Cards Were {Dealer_Cards} ")
            Start()
        elif sum(Player_Cards) < sum(Dealer_Cards):
            print(f"Dealer Cards Were {Dealer_Cards} ")
            Bust(True)
    if response == 'g':
        Grab(Player_Cards,Dealer_Cards)

def Grab(P,D):
    Player_Cards = P
    Dealer_Cards = D
    os.system('cls')
    print(BJA.logo)
    print(f"Your Cards Are:- {Player_Cards}")
    print(f"Dealer Cards Are:- {Dealer_Cards[0]} ❓ ")
    g = Ran.randint(0,12)
    Player_Cards.append(Cards[g])
    print(f"Your Cards Are:- {Player_Cards}")
    if sum(Player_Cards) == 21:
        print(f"Dealer Cards Were {Dealer_Cards} ")
        Win(True)
    elif sum(Player_Cards) > 21:
        print(f"Dealer Cards Were {Dealer_Cards} ")
        Bust(True)
    else:
        choice = Ran.randint(1,2)
        if choice == 1:
            print("Dealer Chose to Stand")
            print(f"Dealer Cards Are:- {Dealer_Cards[0]} ❓ ")
            Game(Player_Cards,Dealer_Cards)
        else:
            o = Ran.randint(0,12)
            Dealer_Cards.append(Cards[o])
            print("Dealer grabbed a card")
            if sum(Dealer_Cards) == 21:
                print(f"Dealer Cards Were {Dealer_Cards} ")
                Bust(True)
            elif sum(Dealer_Cards) > 21:
                print(f"Dealer Cards Were {Dealer_Cards} ")
                Win(True)
            else:
                x = ""
                x += '❓ '
                print(f"Dealer Cards Are:- {Dealer_Cards[0]} ❓ " , x)
                Game(Player_Cards,Dealer_Cards)



def Bust(B):
    if B:
        print("Dealer Won")
        time.sleep(3)
        Start()

def Win(W):
    if W:
        print("You won")
        time.sleep(3)
        Start()


def Start():
    response = input("Play again 'y'|'n' ")
    if response == "y":
        DeckDeal()
    else:
        quit()

DeckDeal()
