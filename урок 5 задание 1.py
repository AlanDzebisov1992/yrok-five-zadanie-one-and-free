



# задание 1

number = int(input())
if number > 0:
    if number % 2 == 0:
        print("положительное четное число")
    else:
        print("положительное нечетное число")
elif number == 0:
    print("нулевое число")
else:
    if number < 0:
        if number % 2 == 0:
            print("отриц.четное")
       else:
            print("отриц. не четное")


# задание 3

Mike = int(input())
Ivan = int(input())
invest = int(input())

if (Mike >= invest) and (Ivan >= invest):
    print(2)
elif (Mike >= invest) and (Ivan <= invest):
    print("Mike")
elif (Mike <= invest) and (Ivan >= invest):
    print("Ivan")
elif (Mike <= invest) and (Ivan <= invest) and ((Mike + Ivan) >=invest):
    print(1)
else:
    print(0)