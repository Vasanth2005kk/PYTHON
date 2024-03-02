import random
import string

asscii_letters=string.ascii_letters+string.punctuation+string.digits
password=""

for i in range(10):
    password+=random.choice(asscii_letters)

print(password)