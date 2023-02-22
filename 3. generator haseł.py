import random
lowercase = 'abcdefghijklmnopersuwxyz'
uppercase = 'ABCDEFGHIJKLMNOPRSTUWXYZ'
number = '1234567890'
symbol = '@#$%&*/\?'
ciag = lowercase+uppercase+number+symbol
length = random.choice(range(8,15))
password = "".join(random.sample(ciag, length))
print(password)
