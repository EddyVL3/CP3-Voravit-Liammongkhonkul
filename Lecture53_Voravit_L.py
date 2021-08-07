Total_Price = int(input("Total Price : "))
Vat = int(input("Tax rate : "))
def Vatcalculate(Total_Price):
    result = Total_Price*((100+Vat)/100)
    return result
print (Vatcalculate(Total_Price))