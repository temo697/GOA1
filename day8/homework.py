# #შექმენით სია, ამ სიაში ჩაწერეთ სხვადასხვა ციფრები (1, 2, 3, 4, ასე არა, რამე მაგ: 45, 23, 87, 55,) და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი, ასევე ამავე სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე, და მიუწეროთ ლუწია თუ კენტი.

# list= [20,54,67,25,8,6,5]
# print([20+54+64+25])

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])

# for num in list:
#     if num % 2 == 0:
#         print(str(num) + "number is odd")
# else:
#     print(str(num) + "number is even")




# ბილეთი ღირს 25 ლარი,
# მაგრამ ბავშვებისთვის უფასოა,
# გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, 
# გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 

# tkt = 25
# people = 13
# child = 3
# chief = 10
# print(str(tkt * chief) + str(" gel"))


#  მომხმარებელს შემოატანინეთ სახელი,
#  და დაპრინტეთ ეს სახელი იმდენჯერ, რამდენი ასოც არის სახელში.  

# user = input("enter your name ") 
# for i in range(len(user)):
#     print(user)



#GOA ში ყოველ შემოყვანილ ადამიანზე გეძლევა 100ლ.
#მომხმარებელს შემოატანინეთ თუ რამდენი ადამიანი შემოიყვანა ხოლო თითო შემოყვანილ ადამიანზე დაერიცხოს 100ლ

#1) რამდენი დაგერიცხება თუ შემოიყვან 10 ბავშვს?  15 ბავშცს?

#2) რამდენი დაგერიცხება თუ შემოიყვან 100 ბავშვს გამოკლებული 37 დამატებული 13 გაყოფილი 10 და გამრავებული 264 ზე

# price = 100
# user = int(input("How many children were brought to Goa? "))
# print(user * price)

# print(100*(100-37+13)/10*264)


# HARDEST BOSS:

# დაპრინტეთ hello world (ოღონდ არა ასე print("hello world")  )

# list = ["giant","chaqapuli", "hello", "number", "world"]

# my_word = "we love goa and we think we are real chads"
# print(my_word[20],my_word[1],my_word[3],my_word[3], my_word[4]  + "   " + my_word[0],my_word[4],my_word[29],my_word[3],my_word[40])


# message = ["Hello, world!"]
# for i in message:
#     print(i)

# 2 way to print Hello world.
# message = "Hello,"
# message1 = "world!"
# print(message + " " + message1)

# 3 way to print Hello world.
# world = ["Hello, world!"]
# msg = "".join(world)
# print(msg)

# 4 way to print Hello world.
# hello = "Hello, world!"
# time = int(input("Enter the current time: "))
# a = 6 
# b = 18
# if time >=a and time <=b:
#     print(hello)
# else:
#     print("Good Bye, world!!!")