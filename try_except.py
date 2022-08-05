# TRY-EXCEPT

# x = int(input("Input an integer : "))
# print(x)


# Run the block of code inside'try;. If any error is encountered, goto 'except'
try:
    x = int(input("Input an integer : "))
    print(x)
except: # runs when there is any kind of error in try
    print("There is an error")

# ValueError

# If I input a string instead of int, python gives this specific error - ValueError: invalid literal for int() with base 10: 'abc'
# Adding an except for ValueError
try:
    x = int(input("Input an integer : "))
    print(x)
except ValueError: # runs only when ValueError occurs
    print("Value not an integer")


# NameError 
try:
    x = int(input("Input an integer : "))
    print(x)
except ValueError:
    try:
        print("Value not an integer" + name) # NameError: name 'name' is not defined
    except NameError: # runs only when NameError occurs
        print("Variable name is not defined")


# else : runs only if try is successful
try:
    x = int(input("Input an integer : "))
    print(x)
except:
    print("Something went wrong")
else: # when nothing goes wrong
    print("Nothing went wrong")


# finally : runs anyway. Either there is an error or not
try:
    x = int(input("Input an integer : "))
    print(x)
except:
    print("Something went wrong")
finally: # will runs irrespective of an error in try
    print("try except ends")