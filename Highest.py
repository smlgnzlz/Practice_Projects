
num1 = float(input("Enter your 3 numbers to compare them.\n Enter a number: "))
num2 = float(input("Enter another number: "))
num3 = float(input("Enter another number: "))

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(num1, num2, num3))
