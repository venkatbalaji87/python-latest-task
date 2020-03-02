import math
constCValue= 50
constHValue=30
splitList=[]
resultList=[]
dinputValues = input("Enter the values : ")
splitList = dinputValues.split(',')
splitList = [int(intialValue) for intialValue in splitList]
intialValue=0
while(intialValue<len(splitList)):
    resultOutput = round(math.sqrt((2*constCValue*splitList[intialValue])/constHValue))
    resultList.append(resultOutput)
    intialValue+=1
print("Output Result =", resultList)
