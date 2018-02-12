# Anna Phan
# Lab 01 - Compute Average
# 01/10/18

numList = open("numbers5.txt").read().splitlines()

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

if len(numbersList) % 2 == 1:
    oddmedIndex = len(numbersList) // 2
    oddMedian = numbersList[oddmedIndex]
    print("Median: ", oddMedian)
else:
    evenIndex = len(numbersList) // 2
    evenIndex2 = (len(numbersList) - 1) // 2
    evenMedian = (numbersList[evenIndex] + numbersList[evenIndex2]) / 2
    print("Median: ", evenMedian)