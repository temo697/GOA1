import random 
arr_list = ["lobjanidze","xaratishvili","abashidze","miladze","papava"]
arr_of_point = [1,2,3,4,5]
answer = input("did the student answer correctly: ")
if arr_of_point == "yes":
    print(arr_list + 5)
elif arr_of_point == "no":
        print(arr_of_point - 5)

for i in range(len(arr_list)):
    winner = random.choice(arr_list)
    lucky_point = random.choice (arr_of_point)
    print(winner,"mopemata",lucky_point)
    arr_list.remove(winner)
    arr_of_point.remove(lucky_point)

