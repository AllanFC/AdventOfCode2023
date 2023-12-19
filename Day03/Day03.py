file1 = open('input.txt', 'r')
Lines = file1.readlines()


arr = []
for line in Lines:
    arr.append([*line])

rows = len(arr)
cols = len(arr[0])-1

directions = [(-1,-1), (-1,0), (-1, 1), (0,1), (1,1), (1,0), (1, -1), (0,-1)]

chars = ["0","1","2","3","4","5","6","7","8","9","."]

def isValid(x, y):
    return 0 <= x < rows and 0 <= y < cols

def getNum(x, y):
    num = str(arr[y][x])
    if isValid(x-1,y):
        try:
            if arr[y][x-1] == "0" or int(arr[y][x-1]):
                num = str(arr[y][x-1]) + num
                if isValid(x-2, y) and (arr[y][x-2] == "0" or int(arr[y][x - 2])):
                    num = str(arr[y][x - 2]) + num
        except:
            pass

    if isValid(x+1,y):
        try:
            if arr[y][x+1] == "0" or int(arr[y][x+1]):
                num = num + str(arr[y][x+1])
                if isValid(x+2, y) and (arr[y][x+2] == "0" or int(arr[y][x + 2])):
                    num = num + str(arr[y][x+2])
        except:
            pass

    return int(num)


total = []
tdict = {}


for i in range(rows):
    for j in range(cols):
        if arr[i][j] not in chars:
            for dy, dx in directions:
                newy = i+dy
                newx = j+dx
                if isValid(newx,newy):
                    try:
                        if arr[newy][newx] == "0" or int(arr[newy][newx]):
                            blah = getNum(newx, newy)
                            if len(total) == 0 or blah != total[-1]:
                                total.append(blah)
                                if arr[i][j] == "*":
                                    key = "(" + str(i)+","+str(j)+")"
                                    if not tdict.get(key):
                                        tdict[key] = [blah]
                                    else:
                                        tdict[key].append(blah)

                    except:
                        pass


print(total)
print(sum(total))
print(tdict)
bigsum = 0
for k, v in tdict.items():
    if len(v) == 2:
        bigsum += v[0]*v[1]
print(bigsum)

