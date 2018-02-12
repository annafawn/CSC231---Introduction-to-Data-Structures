# Anna Phan
# Lab 01 - Compute Average
# 01/10/18

numList = open("numbers.txt").read().splitlines()

numbersList = []
for num in numList:
    numbersList.append(int(num))

print("Count: ", len(numbersList))

sum = 0
for x in numbersList:
    sum += x
print("Average: ", sum/len(numbersList))

numbersList.sort()
minimum = numbersList[0]
print("Min: ", minimum)

maximum = numbersList[len(numbersList)-1]
print("Max: ", maximum)