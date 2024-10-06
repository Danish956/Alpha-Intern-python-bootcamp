cp=float(input("enter the cost price: "))
sp=float(input("enter the selling price: "))
if(sp>cp):
    print(f"its a profit of {sp-cp}")
else:
    print(f"is a loss of {sp-cp}")