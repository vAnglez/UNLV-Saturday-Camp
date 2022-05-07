#Zion - Password Encryption
password = input("What is your Password?")
print("Your Password is: " + password) 
encryptedPassword = ''


for index in range(len(password)):
    char = password[index]
    if (122 > (ord(char))):
        encryptedPassword += chr(ord(char) - 13)
    else:
        encryptedPassword += chr(ord(char) + 13)


print("Your Password is: " + encryptedPassword)