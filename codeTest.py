import sys

''' Reads in a file in format:
    'BIRTH_YEAR DEATH_YEAR \n'
    and finds the rate of change each year
'''
def inputValues(f):
    popChange = [0] * 101
    for line in f:
        years = line.split()
        popChange[int(years[0]) - 1900] += 1
        popChange[int(years[1]) - 1900] -= 1
    return popChange

# Integrates the change in population to find which year had the greatest population
def integratePop(popChange):
    bestPop = 0
    bestYear = 0
    curPop = 0
    for i in range(len(popChange)):
        curPop += popChange[i]
        if (curPop > bestPop):
            bestPop = curPop
            bestYear = i 
    return bestYear
    
# Uses a brute force method, good as a backup
def backupCheck(f):
    popLevel = [0] * 101
    for line in f:
        years = line.split()
        for i in range(int(years[0]), int(years[1])):
            popLevel[i - 1900] += 1
    bestPop = 0
    bestYear = 0
    for i in range(len(popLevel)):
        if (popLevel[i] > bestPop):
            bestPop = popLevel[i]
            bestYear = i
    return bestYear
        
''' Solves the highest pop question. Runs in O(0) space and O(m) time
    where 'm' is the number of people whos births/deaths are considered
'''
def main():
    f = open(str(sys.argv[1]), 'r')
    popChange = inputValues(f)
    f.close()
    bestValue = integratePop(popChange)
    print(popChange)
    print("The year with the largest population is " + str(1900 + bestValue))
    ''' Backup test code
    f = open(str(sys.argv[1]), 'r')
    backupValue = backupCheck(f)
    f.close()
    print("The backup value was " + str(1900 + backupValue))
    '''
    
main()

