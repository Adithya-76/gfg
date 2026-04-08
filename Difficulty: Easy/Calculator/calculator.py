def utility(a, b, opr):
    #code here
    if opr ==1:
        print(a+b,end="")
    if opr == 2:
        print(a-b,end="")
    if opr == 3:
        print(a*b,end="")
    if opr<1 or opr>3:
        print("Invalid Input",end="")