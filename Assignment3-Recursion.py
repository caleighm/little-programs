# A series of recursive functions:
# replaceString: replaces all instances of one type of separator with another type of separator

# countSiblings: count total siblings based on number of elves (each odd elf has 3 siblings while
# even elves have 1 sibling)

# extractor: extracts information from a string only if info is inside parentheses

# sameSums: return True if it is possible to divide a list of integers into two groups where
# the groups' sums are equal

def replaceSep(myString, sep1, sep2) :
    ''' Replace all instances of sep1 in a string with sep2 using recursion. Return new string.
    Parameters: myString = a string; sep1 = separator to replace; sep2 = replacement separator'''
    # base case: sep1 no longer in myString
    if sep1 not in myString:
        return myString

    # work backwards through myString and check if last character is sep1 or not. if it is, replace.
    # either way, re-call function until sep1 is no longer present.
    else :
        if myString[-1] == sep1 :
            return replaceSep(myString[:-1] + sep2, sep1, sep2)
        else :
            return replaceSep(myString[:-1], sep1, sep2) + myString[-1]

def countSiblings(numberElves) :
    ''' Count how many siblings a total number of elves has using recursion. Odd-numbered elves
    have 3 siblings. Even-numbered elves have 2. Return total sibling count.
    Parameters: numberElves = total number of elves'''
    if numberElves < 1 :
        return 0
    else :
        if numberElves % 2 == 0 :   # even-numbered elves
            return 1 + countSiblings(numberElves - 1)
        else :                      # odd-numbered elves
            return 3 + countSiblings(numberElves - 1)

def extractor(string) :
    ''' Extract information from a string if the information is inside parentheses.
    Return new string with extracted info.
    Parameters: string = a string (with or without parenthetical info)'''
    if "(" not in string or ")" not in string :
        return string
    elif string[0] == "(" and string[-1] == ")" :
        return string

    # check and modify the string forwards and backwards simultaneously until a 
    # parenthesis is found
    if string[0] != "(" and string[-1] != ")":
        return extractor(string[1:-1])

    # once a parenthesis is found, start checking from front or end (depending on
    # if found parenthesis is closer to beginning or end)
    elif string[0] == "(" :
        return extractor(string[:-1])
    elif string[-1] == ")" :
        return extractor(string[1:])

def sameSums(aList, sum1=0, sum2=0) :
    ''' Determine recursively if it is possible to divide a list of integers into two groups 
    so that the sums of the two groups are the same. Return True or False.
    Parameters: aList = list of integers; sum1 = default set to 0, but updates with sum
    of group 1 numbers; sum2 = default set to 0, but updates with sum of group 2 numbers'''
    # check if list exists before continuing
    if not aList and sum1 == 0 and sum2 == 0 :
        return False

    # this carries the Boolean values returned by function as it calls itself
    flag = None

    # update sum1 or sum2, depending on which is the smaller sum
    if sum1 < sum2 :
        sum1 = sum1 + aList.pop()  
    elif sum1 > sum2 :
        sum2 = sum2 + aList.pop()  
    else :
        sum1 = sum1 + aList.pop() # if sum1 = sum2, default to giving sum1 the value

    # if list continues to exist, call sameSums again recursively!
    if aList :
        flag = sameSums(aList, sum1, sum2)
        if sum1 == sum2 or flag == True :
            return True
        else :
            return False
    
def tester():
    '''Tester function provided for assignment by professor.'''
    print replaceSep("hope*you*are*enjoying*the*course", "*", " ")
    print replaceSep("Hi.  I am having fun.  Are you?", ".", "!!")
    print replaceSep("popopopopo", "p", "x")
    print replaceSep("xxxxx", "o", "b")
    print countSiblings(0)
    print countSiblings(100)
    print countSiblings(2)
    print countSiblings(5)
    print countSiblings(-9)
    print extractor("(hello world)")
    print extractor("My country (of origin) is Canada")
    print extractor("I do not have any parenthesis")
    print sameSums([1, 7, 2, 4, 3, 6])
    print sameSums([10, 0])
    print sameSums([1, 9, 5, 9])
    print sameSums([2, 2, 3, 3, 4, 4, 1, 1])
    print sameSums([])
    print sameSums([9, 1, 10])

tester()
