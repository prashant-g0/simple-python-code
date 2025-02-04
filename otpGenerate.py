import random
#otp generate function
def generateotp(length):
    #otp variable with striing datatype
    otp = " "
    #loop to ensure length of otp
    for i in range(length):
        #generating otp in range of decimal number
        otp += str(random.randint(0,9))
    return otp
#function call
print(generateotp(4))

#Looking for a more easy code? I got you buddy :)

#otp generating function
def generateotp():
    #for 4 digit otp set the range between min & max 4 digit number
    #you can use range as 100000, 999999 for 6 digit otp
    otp = str(random.randint(1000, 9999))
    return otp
#function call
print(generateotp())