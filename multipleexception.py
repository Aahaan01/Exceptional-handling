try:
    num=int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Check the values!")
except NameError:
    print("Check The name!")
finally:
    print("done")