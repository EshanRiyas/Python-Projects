celcius=float(input("Please enter the temperature in celcius: "))
fahrenhiet = celcius * 1.8 + 32
print("The temperature in Fahrenhiet is: ", fahrenhiet)
if(fahrenhiet >= 104):
    print("It's hot")
elif(fahrenhiet <= 50):
    print("It's cold")
else:
    print("It's a nice day!")