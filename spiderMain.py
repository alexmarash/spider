# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import random

# Create a deck of cards
def create_deck(suit_quantity):
    deck = []
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for i in range(4 * (5 - suit_quantity)):
        for j in range(suit_quantity):

        #for suit in suits:
            for rank in ranks:
                #deck.append(rank + suit)
                deck.append(rank + suits[j])
    #print (deck)

    return deck

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Deal cards to the tableau
def deal_cards(deck):
    tableau = [[] for _ in range(10)]

    j = 0
    for i in range(54):

        #print (deck)

        tableau[j].append(deck.pop(0))
        if j == 9:
            j = 0
        else:
            j += 1


    #for i in range(4):
    #    for j in range(10):
    #        tableau[j].append(deck.pop(0))
    return tableau

# Display the tableau
def display_tableau(tableau):
    print ("____0_____1_____2_____3_____4_____5_____6_____7_____8_____9_____10 ")
    i = 0
    for row in tableau:
        print(i, row)
        i += 1

# Main game loop
def play_spider_solitaire():

    suits_quantity = int(input("Choose how many suits "))


    deck = create_deck(suits_quantity)
    shuffle_deck(deck)
    tableau = deal_cards(deck)
    while True:
        # Display the tableau
        display_tableau(tableau)

        # Get user input
        move = input("Enter your move (format: [source_row_index] [source_card_index] [destination_row_index]): NO COMMAS, just spaces ")
        if move == 'quit':
            break

        # Parse the user input
        source_row, source_card, destination_row = map(int, move.split())

        # Perform the move
        try:
            card = tableau[source_row][source_card]
            print ("first card to move", card, card[:-1])

            if len(tableau[destination_row]) != 0:
                print ("destination card to go on top of", tableau[destination_row][-1])
            else:
                print ("destination row is blank")

            if check_valid_source(tableau, source_row, source_card) and \
                    check_valid_destination(tableau, destination_row, card):

                for i in range(source_card, len(tableau[source_row])):
                    #tableau[source_row].pop(source_card)
                    this_card = tableau[source_row].pop(source_card)
                    tableau[destination_row].append(this_card)
            else:
                print ("Move is not valid, choose again")
        except:
            print ("Move not valid, exception")


def check_valid_source(tableau, source_row, source_card):
    valid_move = True
    for i in range(source_card, len(tableau[source_row]) - 1):
        if integer_rank(tableau[source_row][i][:-1]) != integer_rank(tableau[source_row][i + 1][:-1]) + 1 or \
            tableau[source_row][i][-1] != tableau[source_row][i + 1][-1]:
            valid_move = False

    print ("valid source ", valid_move )

    return valid_move

def check_valid_destination(tableau, destination_row, card):
    valid_move = True

    if len(tableau[destination_row]) == 0:
        return valid_move

    print (integer_rank(card[:-1]), integer_rank(tableau[destination_row][-1][:-1]))

    if integer_rank(card[:-1]) != integer_rank(tableau[destination_row][-1][:-1]) - 1:
        valid_move = False

    print ("valid destination ", valid_move)

    return valid_move

def integer_rank(rank):
    match rank:
        case 'A':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case '10':
            return 10
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13

# Start the game
play_spider_solitaire()
