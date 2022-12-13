file = open("input.txt", "r")
file1 = open("input.txt", "r")
Contents = []
ans = 0


for item in file:
    Contents.append(list(item.replace("\n", "")))

lenLine = len(Contents[0])
lenFile = len(file1.readlines())


def Left(xPos, yPos):
    for i in range(xPos - 1, 0-int(lenLine+xPos), -1):
        if (Contents[yPos][xPos] <= Contents[yPos][i]):
            return False
    return True


def Right(xPos, yPos):
    for i in range(xPos + 1, lenLine):
        if (Contents[yPos][xPos] <= Contents[yPos][i]):
            return False
    return True


def Down(xPos, yPos):
    for i in range(yPos + 1, lenFile):
        if (Contents[yPos][xPos] <= Contents[i][xPos]):
            return False
    return True


def Up(xPos, yPos):
    for i in range(yPos - 1, -1, -1):
        if (Contents[yPos][xPos] <= Contents[i][xPos]):
            return False
    return True


for y in range(lenFile):
    for x in range(lenLine):
        if (y == 0):
            ans += lenLine
            # print("lenline", x)
            break
        if (y == lenFile - 1):
            ans += lenLine
            # print("lenfile")
            break
        if (x % lenLine == 0):
            ans += 1
            # print("Mod l", x)
            continue
        if (int(x + 1) % lenLine == 0):
            ans += 1
            # print("-------------------->", x)
            continue

        if (Right(x, y) or Left(x, y) or Up(x, y) or Down(x, y)):
            print(Contents[y][x], "(",x,y,")")
            ans += 1

print(ans)