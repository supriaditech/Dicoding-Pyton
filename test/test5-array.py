nilaiArray = [1, 5, 7, 8, 4, 24, 6, 33, 4]
leftPointer = nilaiArray[0]

for i in range(1, len(nilaiArray)):
    rightPointer = nilaiArray[i]
    print(rightPointer)
    if rightPointer > leftPointer:
        leftPointer = rightPointer

print(leftPointer)
