import string 
import random 

print("Welcome to the Passwod Generator !\n")
ptotal=int(input("entrer the total  number of characters in the password : "))
letters=int(input("entrer the  number of letters the password :  "))
symbol=int(input("entrer the number of symbols in the password : "))
sd=int(input("entrer the  number of numbers the password :  "))
po=+int(letters+symbol+sd)
if po>ptotal :
    print("eror") 
else :
    ilet=random.choices(string.ascii_letters, k=letters)
    isymb=random.choices(string.punctuation, k=sd)
    inumb=random.choices(string.digits, k=letters)
    poq=ilet+isymb+inumb
    random.shuffle(poq)
    
    password="".join(poq)
    
    print("generated password is :")

    print(password)
    