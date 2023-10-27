import random

lower_case = "abcdfgasdasldksa"
upper_case = "AIKGSADFBAS"
symbols ="!@#$%^&*"
num = "0123456789"

all = lower_case + upper_case + symbols + num

lenght = 8
password ="".join(random.sample(all,lenght))
print("Generator Password Is",password)