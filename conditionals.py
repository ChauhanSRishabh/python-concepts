#  CONDITIONAL STATEMENTS

# input() takes all that is entered as a string
# we need to typecast input() according to our need

age=int(input("Enter you age : ")) # add \n for input in other line
if(age<18):
    print("No License allowed")
elif(age==18):
    # BOOLEAN Data Types
    a = True
    b = False
    print("Apply for license")
else:
    print("Drive the car bro!")
