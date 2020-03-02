row = int(input("Enter the rowValue : "))
column = int(input("Enter the ColumnValue : "))
resultOutput = [[i*j for j in range(column)] for i in range(row)]
print("Result 2-D array is : ",resultOutput)
