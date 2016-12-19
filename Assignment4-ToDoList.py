# This program creates, updates and prints a to-do list based on items and instructions provided
# in a .txt file. It demonstrates the 'linked list' concept from class (which is super awkward in Python,
# but that's just the language we used in class). The program has three main
# functions, with some smaller helper functions for ease of reading and condensing the code. The three main
# functions are

# 1. newItem(data, node, head=None), which adds a new item to anywhere in the list and returns the head
# 2. removeItem(head, node) which removes an item from anywhere in the linked list and returns the head
# 3. printList(head), which prints the entire linked list.

# In the main function, the program also opens and reads a .txt file line-by-line.

# It expects a .txt file 

def newItem(data, node, head=None) :
    ''' Add data to the middle or end of the linked list. Provides warning if the user attempts
    to add to a place that doesn't yet exist, but then defaults to the end of the list if that's the
    case. Always returns the head of linked list (regardless of whether head has been modified).
    Parameters: head = start of linked list; data=information to be added; node = location of info'''
    ptr = head
    newNode = {}
    newNode['data'] = data
    newNode['next'] = None # default 'next' is None in case instruction is to put it at the end of list

    # if the head hasn't been determined yet, or if user wants to insert item at head
    if node == 0 or (node == -1 and head == None) :
        newNode['next'] = head
        head = newNode
        
    # if the node is in the middle of the list
    elif node != -1 :
        # traverse thru list from beginning to the given node
        for i in range(1, node) :
            # check if node provided is bigger than length of list; if so, provide error message
            # and add new item to the end of the list
            if ptr['next'] == None and i < (node - 1) :
                print "You are attempting to add to a place that doesn't exist yet!"
                break
            ptr = ptr['next']
            
        afterNode = ptr['next']
        newNode['next'] = afterNode
        ptr['next'] = newNode       
            
    # if the node is at the end of the list (assume nodes are >= -1)
    else :
        while ptr['next'] != None :
            ptr = ptr['next']
        ptr['next'] = newNode
    
    return head

def removeItem(head, node) :
    ''' Remove an item from the linked list. Prints error if the user asks to remove information that does not exist.
    Always returns the head (even if head did not get modified).
    Parameters: head = start of linked list; node = location of information to be deleted.'''
    ptrBefore = head

    # if requested, remove first item
    if node == 0 :
        head = head['next']

    # otherwise, remove item from the middle of the list
    else :
        for i in range(1, node) :
            
            # check if user has asked to remove an item that does not exist
            if ptrBefore['next'] == None :
                print "No items to remove!"
                return
            else :
                ptrBefore = ptrBefore['next']

        # connect the two items that were on either side of removed item
        ptrAfter = ptrBefore['next']
        temp = ptrAfter['next']
        ptrAfter = temp
        ptrBefore['next'] = ptrAfter

    return head

def printList(head) :
    ''' Traverse and print entire linked list. Prints error if the list is empty.
    Parameters: head = start of linked list.'''
    ptr = head

    # check if list is empty; print error message and leave function if it is
    if not ptr :
        print "List is empty!"
        return

    # if list exists, print each item while there are still items
    while ptr != None :
        print ptr['data']
        ptr = ptr['next']

    print "**********" # print a separating line between each time list gets printed

def getData(line) :
    ''' Return new string with the extracted info inside quotation marks from line.
    Parameters: line = one line string from text file'''
    start = line.index("\"") + 1
    return line[start:-1]

def getNode(line) :
    ''' Convenient little function that extracts the node from the line.
    Parameters: line = string from text file with instructions'''
    node = int(line[3:5])
    return node

def checkInstructions(head, line) :
    ''' Checks which function to execute based on line's instructions. Returns the head (even if it
    wasn't modified).
    Parameters: head = start of list; line = one line string from text file'''
    # check if line is empty
    if line == "" :
        pass
                
    # check if line asks to print entire to-do list
    elif "PL" in line :
        printList(head)

    # check if line asks to remove an item from the to-do list
    elif "RI" in line :
        node = getNode(line)                
        head = removeItem(head, node)

    # check if line asks to add a new item to the to-do list
    else :
        data = getData(line)
        node = getNode(line)
        head = newItem(data, node, head)

    return head
                
def main():
    ''' Main program driver. Reads file for instructions and executes instructions line-by-line.
    Tracks head of list throughout.'''
    
    # initialize head with None (since list doesn't exist yet!)
    head = None

    # open file and read instructions by line
    with open("C:/Python27/Scripts/toDoListInstructions.txt", "r") as in_file :
        for line in in_file :
            line = line.strip()
            head = checkInstructions(head, line)

main()

  
  
