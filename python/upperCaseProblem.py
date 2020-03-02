NumberOflines =[]
while(True):
    getInput = input()
    if(getInput):
        NumberOflines.append(getInput.upper())
    else:
        break
print("Upper Case Values : \n")
for getInput in NumberOflines:
    print(getInput)
