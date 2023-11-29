import random

def licensing(deck, getcard):
    getcard.append(random.choice(deck))

def handcheck(handcard):
    total = sum(handcard)
    return total

def blackjack(com, player):
    if com == 21:
        print("Lose, Computer has Blackjack 😱")
        return True
    elif player == 21:
        print("Blackjack! You win 😃")
        return True
    else:
        return False

def match(com_score, com_card, player_score, player_card):
    if com_score >= player_score:
        print("You lose!😢")
        print(f"Your cards: {player_card}, score: {player_score}")
        print(f"Computer's cards: {com_card}, score: {com_score}")
    elif com_score < player_score:
        print("You win!✌🏼")
        print(f"Your cards: {player_card}, score: {player_score}")
        print(f"Computer's cards: {com_card}, score: {com_score}")

def playerstatus(card, score):
    print(f"    Your cards: {card}, score: {score}")

def comstatus(card, score):
    printprint(f"    Computer card: {card}, score: {score}")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_score = 0
com_score = 0

player_card = []
com_card = []

play = False
play = input("Do you want to play a game of Blackjack?♠️♥️♣️♦️ Type 'y' or 'n': " )
if play == "y":
    play = True
else:
    print("Bye!👋🏼")
    play = False

#Game start licensing cards to player and com
while play:
    while len(com_card) < 2:
        licensing(cards, player_card)
        player_score = handcheck(player_card)
        licensing(cards, com_card)
        com_score = handcheck(com_card)

    #Show game Status
    # playerstatus(player_card, player_score)
    print(f"    Your cards: {player_card}, score: {player_score}")
    print(f"    Computer's first cards: {com_card[1:]}") #{com_card[1]}

    #Blackjack at start?
    if blackjack(com_score, player_score):
        print(f"    Your cards: {player_card}, current score: {player_score}")
        print(f"    Computer Black Jack: {com_card}, score: {com_score}")
        play = False
        break

    getCard = input("Type 'y' to get another card, type 'n' to pass: ")

    if getCard == "n":
        match(com_score, com_card, player_score, player_card)
        play = False
        break

    # print(f"Computer's cards: {com_card}") #寫code時用黎check住com card
    while getCard == "y":
    #Ask player get card or not
        licensing(cards, player_card)
        player_score = handcheck(player_card)
        #Over checking
        if player_score > 21 and 11 in player_card:
            for n, i in enumerate(player_card):
                if i == 11:
                    player_card[n] = 1
            player_score = handcheck(player_card)
            print(f"4    You have 'A' it turn to 1. Your cards: {player_card}, score: {player_score}")

        elif player_score > 21:
            print(f"5    Your cards: {player_card}, core: {player_score}")
            print(f"5.5    Computer's Cards: {com_card}, score: {com_score}")
            print("6     You went over.💥 You lose 😭")
            play = False
            break
        if blackjack(com_score, player_score):
            print(f"3    Your cards: {player_card}, current score: {player_score}")
            print(f"4    Computer Black Jack: {com_card}, score: {com_score}")
            play = False
            break
        else:
            match(com_score, com_card, player_score, player_card)
            play = False
            break
            # playerstatus(player_card, player_score)
            # print(f"5.5    Computer's Cards: {com_card}, score: {com_score}")
            # getCard = input("Type 'y' to get another card, type 'n' to pass: ")


    if play != False:
        #Com get card or not
        if com_score < player_score:
            if com_score > 16:
                print(f"7    Computer said PASS: {com_card[1:]}, score: {com_score}")
                getCard = input("One more card?? 'y' or 'n' to pass: ")

            elif com_score < 16:
                licensing(cards, com_card)
                com_score = handcheck(com_card[1:])
                print(f"99    Computer get 1 card: {com_card[1:]}, score: {com_score}")
                #Over checking
                if com_score > 16 and com_score < 21:
                    match(com_score, player_score)

                if com_score > 21 and 11 in com_card:
                    for n, i in enumerate(com_card):
                        if i == 11:
                            com_card[n] = 1
                    com_score = handcheck(player_card)
                    print(f"4    Com have 'A' it turn to 1. Com cards: {com_card}, score: {com_score}")

                elif com_score > 21:
                    print(f"9    Computer cards: {com_card}, score: {com_score}")
                    print(f"10    Computer went over💥. You win")
                    play = False
                    break
                elif com_score < player_score and com_score < 16:
                    licensing(cards, com_card)
                    com_score = handcheck(com_card[1:])
                    print(f"99    Computer get 1 more card: {com_card[1:]}, score: {com_score}")
                    com_score = handcheck(com_card)
                    if com_score > 16 and com_score < 21:
                        match(com_score, com_card, player_score, player_card)
                    elif com_score > 21:
                        com_score = handcheck(com_card)
                        print(f"9    Computer cards: {com_card}, score: {com_score}")
                        print(f"10    Computer went over. You win")
                        play = False
                        break
                else:
                    match(com_score, player_score)

    elif getCard == "n":
        match(com_score, com_card, player_score, player_card)
        print(f"12    Your cards: {player_card}, score: {player_score}")
        print(f"13    Computer's cards: {com_card}, score: {com_score}")
        play = False
        break



'''
Ace的檢查，如果大於21就會把11變成1

lst = [11,8,11]

for n, i in enumerate(lst):
    if i == 11:
        if sum(lst) >= 21:
            lst[n] = 1
print(lst)

'''
