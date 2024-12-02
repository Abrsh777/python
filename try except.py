try:
    number= int (input("enter a number"))
    print(number)
except:
      print("Invalid Input")   # if z fun is in integer and if we give z input of char it will give Invalid Input





try:
    value=10/0
    number= int (input("enter a number"))
    print(number)
except ZeroDivisionError:
        print("divided by zero")
except ValueError:
        print("invalid input")



try:
    answer=10/0
    number= int (input("enter a number"))
    print(number)
except ZeroDivisionError as err:
        print(err)
except ValueError:
        print("invalid input")