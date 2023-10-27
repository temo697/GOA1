import random 

my_students = ["nika", "gabrieli", "dato", "luka", "sandro","oto"]
arr_of_cars = ["BMW", "mercedes", "prius","subaru","porsche", "bughati"]


for i in range(len(my_students)):
    winner = random.choice(my_students)
    lucky_car = random.choice(arr_of_cars)
    print(winner, "won the car: ", lucky_car)
    my_students.remove(winner)
    arr_of_cars.remove(lucky_car)