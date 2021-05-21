'''
Create a python program to secure an existing password by replacing a set of characters with corrosponding -
'Password-secure' character (provided as tuple).
Example:
        SECURE = (('s','$'),('and','&'),('a','@'),('o','0'),('i','1'),('I','|'))

        Input:
        password = "Indians123"

        output:
        password = "|nd1@n$123"
'''

SECURE = (('s','$'),('and','&'),('a','@'),('o','0'),('i','1'),('I','|'))
def secure_Password(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

if __name__ == "__main__":    
    password = input("Enter your password : ")
    password = secure_Password(password)
    print(f"Your secure password is {password}")

