def divNum(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You can't divide to zero!"


while True:

    nextDiv = input("Do you want to continue?(y/n): ")

    if nextDiv.lower() == 'y':

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = divNum(a, b)

        print(result)

    elif nextDiv.lower() == 'n':

        break
