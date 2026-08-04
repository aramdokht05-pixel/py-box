name = input("what is your name?")
print(" hello "  + name +  " welcome! ")
print("my name is neven!")

print(" i can print your expression")
choice = str(input("do you want it? (y/n)"))
if choice == "y":
   while True:
        print("oky! writing your expression")
        expression = input(" your expression:")
        print(expression)
        again = input("do you want again?(y/n)")
        if again == "y":
            print("oky!")
            continue
        if again == "n":
            print("oky!")
        break
if choice ==  "n":
    print("oky! good by...")

input("press enter to exit...")