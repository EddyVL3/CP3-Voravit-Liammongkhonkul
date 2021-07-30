Rice_per_kg = 90
Meat_per_kg = 300
Pork_per_kg = 200
Chicken_per_kg = 150

if username == "Voravit" and password == "9301":
    print ("---Welcome to Khunchiang Khamkhan shop---")
    print ("--------Plase enjoy your shopping--------")
    print ("----------------Our product--------------")
    print ("Rice",Rice_per_kg ,"Per kg")
    print("Meat", Meat_per_kg , "Per kg")
    print("Pork", Pork_per_kg , "Per kg")
    print("Chicken", Chicken_per_kg, "Per kg")
    print("---------------Please order---------------")
    Rice = int(input("Rice Qty : "))*Rice_per_kg
    Meat = int(input("Meat Qty : "))*Meat_per_kg
    Pork = int(input("Pork Qty : "))*Pork_per_kg
    Chicken = int(input("Chicken Qty : "))*Chicken_per_kg
    print("----------------Your Order----------------")
    print ("Rice",Rice_per_kg, "=" ,Rice)
    print("Meat", Meat_per_kg, "=" ,Meat)
    print("Pork", Pork_per_kg, "=" ,Pork)
    print("Chicken", Chicken_per_kg, "=" ,Chicken)
    print("---------------------------------------------")
    print("Grand total" , Rice+Meat+Pork+Chicken , "Baht")
    print("---------------------------------------------")
    print("----------Thank you for shopping-------------")
else:
    print("Login Failure")



