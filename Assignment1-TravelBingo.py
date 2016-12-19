# This program lets up to three players play Travel Bingo! Each player is assigned
# a grid-card with random items commonly seen from a car, and the first player
# to reach the chosen bingo goal will win. Players can keep playing until they choose to stop.

import random

def loadItems() :
    '''Read file of potential items and store as a list of strings. Return list of strings.'''
    stringList = []
    with open("C:/Python27/Scripts/travelItemList.txt", "r") as in_file :
        for line in in_file :
            line = line.strip()
            stringList.append(line)

    return stringList

def getNum(prompt, low, high ):
    '''Asks user for number input and checks validity based on upper and lower limits.
    Will loop until the user provides valid input.
    Parameters: prompt = text to ask user for input; low = lower limit; high = upper limit.'''
    checkFlag = False
    while not checkFlag :
        num = int(raw_input(prompt)) 
        if num < low :
            print "You need to provide a number higher than {}. Please try again.".format(low)
        elif num > high :
            print "You need to provide a number lower than {}. Please try again.".format(high)
        else :
            checkFlag = True

    return num

def getGrid() :
    '''Ask user for grid size and return list of column and row length'''
    grid = []

    rows = getNum("Number of rows: ", 0, 54)
    columns = getNum("Number of columns: ", 0, (54 - rows))
    
    grid.append(rows)
    grid.append(columns)

    return grid

def getGoal(grid) :
    '''Asks user for goal, prints description of goal, and returns a number signifying that goal.
    Parameter: grid = a list of two numbers, # of rows and columns.
    This is only needed to validate user's selection of Goal 3 (Diagonal), where the grid must be n x n.'''
    goal = getNum("Please select your goal for this round!\n1\tFull Card\n2\tSingle Line\n3\tDiagonal\n4\tFour Corners\n", 1, 4)

    # Check if the goal is valid.
    checkFlag = False
    while not checkFlag :
        if goal == 3 and grid[0] != grid[1] :
            print "You can't use Diagonal as your goal because your grid is not n X n."
            goal = getNum("Please select your goal for this round!\n1\tFull Card\n2\tSingle Line\n3\tDiagonal\n4\tFour Corners\n", 1, 4)
        else :
            checkFlag = True

    # Print goal for user.             
    if goal == 1 :
        print "\nYour goal is Full Card - all items must be found."
    elif goal == 2 :
        print "\nYour goal is Single Line - all items in a horizontal or vertical line must be found."
    elif goal == 3 :
        print "\nYour goal is Diagonal - all items in a diagonal line must be found."
    else :
        print "\nYour goal is Four Corners - the items in each of the four corners must be found."

    return goal

def getName(num) :
    '''Ask user for player name and return name as a string
    Parameter: num = total number of players, used to identify which player is being named'''
    name = raw_input("What is Player {}'s name? ".format(num))

    return name
        
def makeCard(grid, itemList) :
    '''Create a card for a player and reurn list of card items
    Parameters: grid = list of row and column lengths; itemList = list of all available items to place in card'''
    # For this function, column and row totals need to be at least 1 for the loop
    # to fill card with items (even if user may have selected 0 rows or columns for their grid)
    if grid[0] == 0 :
        grid[0] = 1
    elif grid[1] == 0 :
        grid[1] == 1

    # create list of unique, random numbers to randomly select items from ItemList
    numList = []
    for i in range(0, grid[0] * grid[1]) :
        numList.append(random.choice(range(0, 54)))

    card = []
    k = 0 # to iterate through numList
    for i in range(0, grid[0]) : # outer loop determines row
        card.append([])
        for j in range(0, grid[1]) : # inner loop populates each column within row        
            card[i].append(j)
            card[i][j] = itemList[numList[k]]
            k = k + 1
    return card 

def printCard(name, card) :
    '''Print player card to screen with a tab between each item in a row and a break between each row
    Parameters: name = string of player's name; card = list of lists (that is, rows -> columns) containing player's items'''
    print "{}'s card:\n".format(name)

    for i in range(0, len(card)) :
        for j in range(0, len(card[i])) :
            print "{}\t".format(card[i][j]), 
        print "\n"

def callItem(itemList) :
    '''Call new item and then remove that item from the item list so it cannot be called again.
    Returns the called item so that each player card can then be checked to see if it contains
    that item.
    Parameters: itemList = list of all available items to place in card'''
    checkFlag = False
    while checkFlag == False :
        callItem = raw_input("Type 'y' to call a new item!")
        if callItem == "y" :
            checkFlag = True

    num = random.randint(0, len(itemList) - 1)  # random.randint generates a <= N <= b, so it requires
                                                # len(itemList) - 1 to ensure it doesn't generate something too high
    item = itemList.pop(num)
    print "The new call item is {}!".format(item)

    return item

def checkCard(item, card) :
    '''Check if a card contains given item, and if so, replace that card item with "FOUND!". Returns updated card.
    Parameters: item = string containing the called item; card = list of lists (i.e. rows -> columns) containing player's items'''
    for i in range(0, len(card)) :
        for j in range(0, len(card[i])) :
            if card[i][j] == item :
                card[i][j] = "FOUND!"

    return card            

def checkWinner(goal, card) :
    '''Check if the card meets established goal condition. Returns Boolean signifying if player has won or not.
    Parameters: goal = number signifying goal type, must be 1-4; card = list of lists (i.e. rows -> columns) containing player's items'''
    winner = True
    # Entire card
    if goal == 1 :
        for i in range(0, len(card)) :
            for j in range(0, len(card[i])) :
                if card[i][j] != "FOUND!" :
                    winner = False
    
    # Single vertical or horizontal line        
    elif goal == 2 :
        # check horizontal lines first
        for i in range(0, len(card)) :
            winner = True
            for j in range(0, len(card[i])) :
                if card[i][j] != "FOUND!" :
                    winner = False
            if winner == True : 
                return winner
            
        # then check vertical lines
        row = 0
        for j in range(len(card[row])) :
            winner = True
            for i in range(len(card)) :
                if card[i][j] != "FOUND!" :
                    winner = False
                row = row + 1
            if winner == True :
                return winner
                
    # Diagonal line
    elif goal == 3 :
        for i in range(len(card)) : # check top left to bottom right diagonal
            if card[i][i] != "FOUND!" :
                winner = False
        if winner == True :
            return winner
        for i in range(1, len(card) + 1) : # check top right to bottom left diagonal
            if card[-i][-i] != "FOUND!" :
                winner = False
    
    # Four corners
    elif goal == 4 :
        if card[0][0] != "FOUND!" or card[0][-1] != "FOUND!" or card[-1][0] != "FOUND!" or card[-1][-1] != "FOUND!" :
            winner = False

    return winner

def declareWinners(winners, playerNames) :
    ''' Print winners.
    Parameters: winners = list of True/False indicating winners; playerNames = list of player names.'''
    for i in range(0, len(winners)) :
        if winners[i] == True :
            print "{} is a winner! Hooray!".format(playerNames[i])

def playAgain() :
    ''' Ask user if they would like to play again. Return Boolean.'''
    playAgain = ""
    keepPlaying = True
    while playAgain != "y" and playAgain != "n" :
        playAgain = raw_input("Would you like to play again? y/n")

    if playAgain == "n" :
        keepPlaying = False
        print "Have a good trip!"

    return keepPlaying

def main() :
    ''' main() drives the entire game. Execution begins here.'''
    originalItems = loadItems()

    # Loop for continuing play if desired
    keepPlaying = True
    while keepPlaying == True :
        callerItems = originalItems[:] # create duplicate item list to preserve originals

        # Game set-up: # of players, grid size, goal
        numPlayers = getNum("Number of players (between 1-3): ", 1, 3)
        grid = getGrid()
        goal = getGoal(grid)

        # Set player names, cards, win status
        playerNames = []
        playerCards = []
        winners = []
        for i in range(0, numPlayers) :
            playerNames.append(getName(i + 1))
            playerCards.append(makeCard(grid, callerItems))
            printCard(playerNames[i], playerCards[i])
            winners.append(False)

        # Play until someone wins
        while True not in winners :
            item = callItem(callerItems)
            for i in range(0, len(playerCards)) :
                playerCards[i] = checkCard(item, playerCards[i])
                printCard(playerNames[i], playerCards[i])
                winners[i] = checkWinner(goal, playerCards[i])

        declareWinners(winners, playerNames)
        keepPlaying = playAgain()
    
main()
