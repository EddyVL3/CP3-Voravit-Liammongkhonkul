row = int(input("Input row  :  "))
for x in range (row):
    print((" "*(row-(x+1)))+("*"*x)+"*"+("*"*x))