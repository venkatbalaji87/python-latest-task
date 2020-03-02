getDictionary={}
inputRange = int(input("Enter the range : "))
for x in range(1, inputRange+1):
    getDictionary[x] = x*x
print(getDictionary)
