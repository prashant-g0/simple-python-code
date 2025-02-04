import random
import time
#random 6 digit otp generation
otp = str(random.randint(100000, 999999))
#setting expiration time (30 sec)
expiration_time = time.time() + 30
#output: OTP
print(f"OTP: {otp}")
#USer-input: OTP
user_input = input("Enter the OTP you received: ")
#condition check and relative output
if user_input == otp and time.time() < expiration_time:
    print("OTP verified successfully!")
else:
    print("Invalid OTP or OTP expired!")