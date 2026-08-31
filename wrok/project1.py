#creating a strong password.
import random
lower="abcdefghjiklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="!@#$%^&*'"
all=lower+upper+symbols
length=16
passwords=''.join(random.sample(all,length))
print(passwords)
