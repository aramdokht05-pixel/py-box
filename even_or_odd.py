print("""hello,
      welcome...""")
while True:
    num = float(input("enter the number to determine whether it is even or odd:"))
    if num == 0:
        print(" it's zero")
    elif num % 2 == 0:
        print("it's even")
    else:
        print("it's odd")
    opinion = str(input("do you want again?(y/n)"))
    if opinion == "y":
        continue
    elif opinion == "n":
        print("good by")
        break