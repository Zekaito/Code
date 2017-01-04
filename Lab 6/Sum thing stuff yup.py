say="yes"

while say=="yes":
    x=int(input("Please enter your first integer"))
    y=int(input("Please enter your second integer"))

    print('The sum of ',x,' and ',y,' is ',x+y)

    say=input('Would you like to do another calculation?')
    say=say.lower()
