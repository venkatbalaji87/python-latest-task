startValue = int(input("Enter the start range :"))
endValue = int(input("Enter the end range : "))
emptyList=[]
for inputValue in range(startValue, endValue+1):
    if((inputValue % 7==0) and (inputValue%5!=0)):
        emptyList.append(inputValue)
print(emptyList)
