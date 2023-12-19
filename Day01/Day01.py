file1 = open('input.txt', 'r')
Lines = file1.readlines()


def getPartOne(line):
    l = ""
    r = ""
    found = False
    i = 0
    while i < len(line) and not found:
        if line[i].isdigit():
            l = line[i]
            found = True
        i += 1

    found = False
    i = len(line)-1
    while i >= 0 and not found:
        if line[i].isdigit():
            r = line[i]
            found = True
        i -= 1

    res = int(l+r)
    return res

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getPartTwo(line):
    for n in numbers:
        line = line.replace(n, n + str(numbers.index(n)) + n)

    return getPartOne(line)


pOneTotal = 0
pTwoTotal = 0
for line in Lines:
    pOneTotal += getPartOne(line)
    pTwoTotal += getPartTwo(line)

print(pOneTotal)
print(pTwoTotal)