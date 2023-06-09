import copy
import random

# Create a deck of cards
def create_deck(suit_quantity):
    deck = []
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    k = 2
    if suit_quantity == 1:
        k  = 8
    elif suit_quantity == 2:
        k = 4
    elif suit_quantity == 4:
        k = 2

    for i in range(k):
    #for i in range(2 * (5 - suit_quantity)):
        for j in range(suit_quantity):

        #for suit in suits:
            for rank in ranks:
                #deck.append(rank + suit)
                deck.append(rank + suits[j])


    if suit_quantity == 3:
        for rank in ranks:
            deck.append(rank + suits[0])
            deck.append(rank + suits[1])

    #print("Deck length", len(deck))

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
    return tableau, deck

# Display the tableau
def display_tableau(tableau, deck):
    print ("Deals left in deck ", int(len(deck)/10))

    print ("____0_____1_____2_____3_____4_____5_____6_____7_____8_____9_____10 ")
    i = 0
    for row in tableau:
        print(i, row)
        i += 1

# Main game loop
def play_spider_solitaire():

    gameRunning = True

    suits_quantity = int(input("Choose how many suits "))

    deck = create_deck(suits_quantity)
    shuffle_deck(deck)
    tableau, deck = deal_cards(deck)
    undoCopy = copy.deepcopy(tableau)

    while gameRunning:
        # Display the tableau
        display_tableau(tableau, deck)

        # Get user input
        move = input("Enter your move (format: [source_row_index] [source_card_index] [destination_row_index]): NO COMMAS, just spaces, or  deal or quit ")

        if move == 'quit':
            gameRunning = False
        elif move == 'deal':
            nextDeal(tableau, deck)
        elif move == 'undo':
            tableau = undoCopy
        elif move == 'pick' or len(move.split()) == 3:
            undoCopy = copy.deepcopy(tableau)
            if move == 'pick':
                source_row, source_card, destination_row = makeRandomMove(tableau)
            else:
            # Parse the user input
                source_row, source_card, destination_row = map(int, move.split())

            if source_row > 10 or destination_row > 10 or source_card >= len(tableau[source_row]):
                print ("Move is not valid 1")
            else:
            # Perform the move
                card = tableau[source_row][source_card]
                print ("first card to move", card)

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
                    print ("Not a correct source or destination")

                #rowComplete = isRowComplete(tableau, destination_row)
                if isRowComplete(tableau, destination_row):
                    tableau = removeRow(tableau, destination_row)
                    if checkForWin(tableau):
                        print ("WINNER WINNER CHICKEN DINNER")
                        gameRunning = False


        else:
            print("Not enough inputs, or not a valid input")
                #else:
                #    print ("Move is not valid, choose again")





def check_valid_source(tableau, source_row, source_card):
    valid_move = True
    for i in range(source_card, len(tableau[source_row]) - 1):
        if integer_rank(tableau[source_row][i][:-1]) != integer_rank(tableau[source_row][i + 1][:-1]) + 1 or \
            tableau[source_row][i][-1] != tableau[source_row][i + 1][-1]:
            valid_move = False
            #print ("Not a valid source")

    #print ("valid source ", valid_move )

    return valid_move

def check_valid_destination(tableau, destination_row, card):
    valid_move = True

    if len(tableau[destination_row]) == 0:
        return valid_move

    #print (integer_rank(card[:-1]), integer_rank(tableau[destination_row][-1][:-1]))

    if integer_rank(card[:-1]) != integer_rank(tableau[destination_row][-1][:-1]) - 1:
        valid_move = False
        #print ("Not a valid destination")

    #print ("valid destination ", valid_move)

    return valid_move

def isRowComplete(tableau, destination_row):
    if len(tableau[destination_row]) < 13 or integer_rank(tableau[destination_row][-1][:-1]) != 1:
        return False


    for i in range(len(tableau[destination_row]) - 1, len(tableau[destination_row]) - 13, -1):

        print (tableau[destination_row][i], tableau[destination_row][i - 1])

        if tableau[destination_row][i][-1] != tableau[destination_row][i - 1][-1]:
            return False
        elif integer_rank(tableau[destination_row][i][-1]) != integer_rank(tableau[destination_row][i - 1][-1]) - 1:
            return False

    return True

def removeRow(tableau, destination_row):
    for i in range(13):
        tableau[destination_row].pop()

    return tableau

def checkForWin(tableau):
    win = True
    for row in tableau:
        if len(row) > 0:
            win = False
    return win

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

def nextDeal(tableau, deck):
    if len(deck) != 0:
        for i in range(10):
            tableau[i].append(deck.pop(0))
    else:
        print ("Deck is empty")
    return tableau, deck

def makeRandomMove(tableau):
    choosingMove = True
    while choosingMove:
        randomSourceRow = random.randint(0, 9)
        randomSourceCard = random.randint(0, len(tableau[randomSourceRow]) - 1)
        choosingDestination = True
        while choosingDestination:
            randomDestinationRow = random.randint(0, 9)
            if randomDestinationRow != randomSourceRow:
                choosingDestination = False

        #print (randomSourceRow, randomSourceCard, randomDestinationRow)

        card = tableau[randomSourceRow][randomSourceCard]
        if check_valid_destination(tableau, randomDestinationRow, card) and \
                check_valid_source(tableau, randomSourceRow, randomSourceCard):
            choosingMove = False

    print (randomSourceRow, randomSourceCard, randomDestinationRow)
    return randomSourceRow, randomSourceCard, randomDestinationRow


# Start the game
play_spider_solitaire()
