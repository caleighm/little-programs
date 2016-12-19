# This program sorts a list of numbers by breaking it into smaller lists and then merging those tiny lists
# into sorted, slightly bigger lists (and continuing that iteratively until only one big list remains).
# It includes a test function for the sorting process, as well as functions to test the sorting
# process's efficiency. It also includes a modified bubble sort function and a test function for that,
# as well.

import random

def mergeSort(aList) :
    ''' Break a list of elements into smaller lists, and then
    return the sorted list of one fully sorted list.
    Paramters: aList = list of elements'''
    # skip the sorting process if list contains 1 element or fewer
    if len(aList) <= 1 :
        return aList

    # outer loop determines how long each sub-list will be per pass
    for length in range(1, len(aList)) :
        length = length * 2 # multiples of 2 -- sub-list grows from 2 elements, to 4, to 8 ...
        
        # inner loop creates sub-lists, uses mergeLists() to merge each two adjacent sub-lists
        # and then replaces all those elements in aList with the new, merged list
        for start in range(0, len(aList), length) :
            list1 = aList[start : start + (length / 2)]
            list2 = aList[start + (length / 2) : start + length]

            # replace those elements in aList with the new, merged, sorted list
            aList[start : start + length] = mergeLists(list1, list2)
    
    return aList

def mergeLists(list1, list2) :
    ''' Compare elements from two lists and merge lowest element by turn
    into new, merged list. Return new list.
    Parameters: list1 = first list; list2 = second list'''
    mergedList = []

    # continue until both lists are empty
    while list1 or list2 :
        if not list1 :
            mergedList.append(list2.pop(0))
        elif (not list2) or (list1[0] < list2[0]) :
            mergedList.append(list1.pop(0))
        else :
            mergedList.append(list2.pop(0))

    return mergedList
        
def testMerge(aList) :
    ''' Test mergeSort() by printing initial unsorted list, then sorting, then printing
    sorted list.
    Parameters: aList = list with which to test mergeSort'''
    print "Unsorted: \n", aList
    sortedList = mergeSort(aList)
    print "\nSorted: \n", sortedList, "\n*****\n"

def generateRandom(N) :
    ''' Return list of random numbers of given size.
    Parameters: N = size of list to create'''
    aList = []
    for i in range(0, N) :
        aList.append(random.choice(range(-1000000, 1000000)))

    return aList

def mergeStepCounter(aList) :
    '''Return number of times mergeSort() will loop through a fundamental step
    for a particular list size.
    Parameters: aList = list of elements'''
    counter = 0
    
    if len(aList) <= 1 :
        return aList

    for length in range(1, len(aList)) :
        length = length * 2
        
        # this is the fundamental step to count
        for start in range(0, len(aList), length) :
            list1 = aList[start : start + (length / 2)]
            list2 = aList[start + (length / 2) : start + length]
            aList[start : start + length] = mergeLists(list1, list2)

            counter = counter + 1
    
    return counter

def mergeComplexity(N) :
    ''' Test and print number of steps needed for mergeSort() to execute
    depending on problem size.
    Parameters: N = size of unsorted list'''
    aList = generateRandom(N)
    print "N =", N, "; steps =", mergeStepCounter(aList)

def bubbleSort(aList) :
    ''' Use bubble sort algorithm to sort list, with added modification of moving
    forwards then backwards through the list during one pass.
    Parameters: aList = list of elements'''
    end = len(aList) - 1
    switch = True
    while switch :
        switch = False

        # pass 1: move forwards through the list
        for i in range(0, end) :
            if aList[i] > aList[i + 1] :
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                switch = True

        # pass 2: move backwards through the list
        for i in range(end, 0, -1) :
            if aList[end] < aList[end - 1] :
                aList[end], aList[end - 1] = aList[end - 1], aList[end]
                switch = True
                
        end = end - 1

    return aList

def testBubble(aList) :
    ''' Test bubbleSort() by printing initial unsorted list, then sorting, then printing
    sorted list.
    Parameters: aList = list with which to test bubbleSort'''
    print "Unsorted: \n", aList
    sortedList = mergeSort(aList)
    print "\nSorted: \n", sortedList, "\n*****\n"

def main() :
    ''' Driver of entire program and includes testing.'''
    # Sample lists
    evenList = [5, 9, 13, 12, 8, 2, 1, 100]
    oddList = [5, 9, 13, 12, 4, 0, 8, 7, 4]
    tinyList = [1]
    emptyList = []
    sortedList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    longList = [5, 9, 13, 12, 4, 0, 8, 7, 4, 8, 2, 1, 100, 99, 15, 54, 78, 29, 38, 10, 2000, 2093, 381, 33, 398, 48, 41, 23, 800, 381]

    print "Testing merge sort\n------------------"
    testMerge(evenList)
    testMerge(oddList)
    testMerge(tinyList)
    testMerge(emptyList)
    testMerge(sortedList)
    testMerge(longList)

    print "Testing bubble sort\n------------------"
    testBubble(evenList)
    testBubble(oddList)
    testBubble(tinyList)
    testBubble(emptyList)
    testBubble(sortedList)
    testBubble(longList)

main()
