#Take input list of marks and ask which index to print the mark of that index. If the index is out of range, print "ERROR : CAUGHT A RUN TIME ERROR ENTER PROPERLY".Using try and except block syntax method.    
marks = list(map(int, input("Enter marks separated by spaces: ").split()))

try:
    index = int(input("Enter the index to print the mark: "))
    print("Mark:", marks[index])

except IndexError:
    print("Index out of range : Error a run time error is caught.")