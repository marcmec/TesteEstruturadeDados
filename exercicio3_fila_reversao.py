

def invertArr(arr: list) -> list:
    newArr = []
    length = len(arr)
    for i in range(length):
        newArr.append(arr[(length-1) - i])
    return newArr

arr = [3, 5, 6, 1]
invertedArr = invertArr(arr)

print(invertedArr)