#მომხმარებელს შეეკითხეთ ხელფასი

# მომხმარებელს შეეკითხეთ ხელფასი

# თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?

# თუ 1000----10000 -ია , დაუპრინტეთ you mid

# თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

salary = int(input("enter your salary "))

if salary > 10000:
    print("გოაში სწავლობდი")
elif salary > 1000:
    if salary < 10000:
     print("you mid")
if salary < 1000:
    print("შემოსულიყავი გოაში")

#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you (edited)

first = 10
second = 5
third = 7
fourth = 8
fifth = 9
yvela = first + second + third + fourth + fifth
sashualo_aritmetikuli = yvela / 5
print(sashualo_aritmetikuli)

if sashualo_aritmetikuli == 10:
    if sashualo_aritmetikuli > 10:
        print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")

if sashualo_aritmetikuli < 5:
        print("დაუპრინტე გილოცავ გაექეცი მატრიცას")
if sashualo_aritmetikuli > 5:
    if sashualo_aritmetikuli < 9 :
     print("you are mid")
if sashualo_aritmetikuli > 10:
    print(" there is something wrong with you ")
if sashualo_aritmetikuli < 0:
        print(" there is something wrong with you ")