def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("user or password wrong")
        return False
def showMenu():
    print("+++++++NineShop+++++++")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    return menuSelect()
def menuSelect():
    userselected = int(input("select 1 or 2 :"))
    if userselected == 1:
        return vatCalculate((int(input("totalprice:"))))
    elif userselected == 2:
        return priceCalculate()
    else:
        return showmenu()
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    print("Result", result)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)
login()
