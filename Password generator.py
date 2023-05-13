import random
x="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_sandi=int(input("masukan panjang password:"))
password=""
for i in range(panjang_sandi):
    password = password + random.choice(x)

print (password)