class getPrintString():
    def __init__(inputValue):
        inputValue.str1 = ""

    def getString(inputValue):
        inputValue.str1 = input("Enter the string to make UpperCase : ")

    def printString(inputValue):
        print(inputValue.str1.upper())

getString = getPrintString()
getString.getString()
getString.printString()
