"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    # Section 1
    # DEfine a string
    myStr = "Hello Workd"
    '''

    print()
    print(myStr)
    print(myStr[6])
    print(myStr[len(myStr)-1])
    print(myStr[10])
    print(myStr[11])
    print(myStr[0])
    print(myStr[-1])
    print(myStr[-5])
    print(myStr[-len(myStr)])
    


    word1 = "Hello"
    word2 = "world"
    myStr2 = word1 + " " + word2
    print(myStr2)
    myStr3 = word1 + word2
    print(myStr3)

    print(myStr2[6:len(myStr2)])

    print()

    

    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("Enter a month number (1 - 12): "))
    pos = (n-1) * 3
    monthAbr = months[pos:pos+3]
    print(monthAbr)

    print(months[(n-1)*3:(n-1)*3+3])

    print()

    

    # lists
    # create an empty list
    myList1 = []
    print("myList:", myList1)

    myList2 = [1, 2, 3, 4]
    print("myLiost2:", myList2)
    
    myList3 = [42, "Forty-two", 3.14]
    print("myList3: ", myList3)
    
    print('third element of myList2:', myList2[2])

    # initialization example
    for i in range(1,6):
        myList1.append(i)
    print("myListL:", myList1)

    # illustrated insert()
    myList1.insert(2, 3.14)
    print("myList1:", myList1)

    # illustrate sort()
    myList1.sort()
    print('myList:', myList1)

    
    
    print("A: ", ord('A'))
    '''
    myStr = "test  \n"
    print("*", myStr, "*", sep="")
    print()
    myStr = myStr.rstrip()
    print("*", myStr, "*", sep="")

    myStr = "CamelCase"
    print(myStr)
    s1 = myStr.upper()
    print(s1)
    s2 = myStr.lower()
    print(s2)

    myStr = "Marry had a little lamb"
    myList = myStr.split()
    print(myList)

    print()


main()    