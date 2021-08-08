def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("----- iShop -----")
        priceCalculator()
        print("-----------------")
        print("Thank you for your shopping")
    else:
        print("Login failure")
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print("Total price    :",(price1+price2)*((100+7)/100),"Baht")
login()