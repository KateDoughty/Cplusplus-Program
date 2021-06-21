import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def freqOfItems():
    #read file
    lines = []
    f = open('GroceryList.txt')
    lines = f.readlines()
    f.close()

    #count frequency of each item
    count = 0
    items = []
    found_duplication = False
    for line in lines:
        for item in items:
            if item.strip("\n") == line.strip("\n"):
                found_duplication = True
            if not found_duplication:
                items.append(line)

                for line_check in lines:
                    if line.strip("\n") == line_check.strip("\n"):
                        count += 1
                print("".join([line.strip("\n")," x",str(count)]))

            else:
                found_duplication = False

            count = 0
            
            #save to data file
            fileName = "freq.dat"
            outputFile = open(fileName, 'w')

            for key, value in data.items():
                outputFile.write(key)
                outputFile.write(' ')
                outputFile.write(str(value))
                outputFile.write("\n")

            outputFile.close()
        print()

def specificItem(itemToCount):
    #count amount of certain item
    lines = []
    f = open('GroceryList.txt')
    lines = f.readlines()
    f.close()
    numItems = 0
    numItems = lines.count(itemToCount)
    print(itemsToCount, ': ', numItems)
