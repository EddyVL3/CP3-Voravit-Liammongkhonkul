Menu = {"สเต็กหมู":120,"สเต็กไก่":100,"สเต็กปลา":180,"สเต็กเนื้อ":350}
menulist = []
def showbill():
    print ("------ VL Steak house------")
    for number in range (len(menulist)):
        print (menulist [number][0],menulist [number][1])
def totalbill():
    price = 0
    for x in range (len(menulist)):
        price += menulist [x][1]
    print("รวม  :  ",price)

while True:
    Menuname = input("Enter your order : ")
    if(Menuname.lower() == "exit"):
        break
    else:
        menulist.append([Menuname,Menu[Menuname]])
showbill()
totalbill()