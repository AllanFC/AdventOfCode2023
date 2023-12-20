file1 = open('testinput.txt', 'r')
Lines = file1.readlines()

def partOne(winningNumbers, myNumbers):
    total = 0

    for n in myNumbers:
        if n in winningNumbers:
            if total == 0:
                total = 1
            else:
                total *= 2
    return total

def partTwo(dict, lineNumber, winningNumbers, myNumbers):
    k = str(lineNumber)
    print(dict.get(k)+1)
    for i in range(dict.get(k)+1):
        copies = 1
        for n in myNumbers:
            if n in winningNumbers:
                key = str(lineNumber+copies)
                if dict.get(key) is None:
                    dict[key] = 1
                else:
                    dict[key] += 1
                copies += 1




sum = 0
sum2 = 0
dict = {"1" : 0}
lineNumber = 1
for line in Lines:
    numbers = line[line.index(":") + 1:].strip().split("|")
    winningNumbers = numbers[0].strip().replace("  ", " ").split(" ")
    myNumbers = numbers[1].strip().replace("  ", " ").split(" ")

    sum += partOne(winningNumbers, myNumbers)
    partTwo(dict, lineNumber, winningNumbers, myNumbers)
    lineNumber += 1



print(sum)
print(dict)
for k, v in dict.items():
    sum2 += v

print(sum2)

