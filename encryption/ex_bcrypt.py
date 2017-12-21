import bcrypt

password1 = b"admin123"
hashed = bcrypt.hashpw(password1, bcrypt.gensalt())

password2 = b"admin123"

print("1: {0}".format(password1))
print("2: {0}".format(hashed))
if(bcrypt.checkpw(password2, hashed)):
  print("Passwords Match")
else:
  print("ERROR")
