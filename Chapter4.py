# Chapter 4 - working with lists

#This is how you use for loop in python
Magicians = ['alice', 'david', 'carolina']
for Magican in Magicians:
    print(Magican)

#Now we are going to print a message in a for loop
Cars = ['BMW', 'Audi', 'Mercedes']
for Car in Cars:
    print(f"\n{Car.title()}, is a cool car!")
    print(f"I cant wait for the next model of, {Car.title()}!")

#After finishing for loop, the program will move on to the next code and execute that once without repetition
print("\nThank You, everyone. That was a great magic show!")

#One common error one should avoid is forgetting to indent(ha riktig mellomrom på print)
Languages = ['English', 'Spanish', 'Russian']
#for Language in Languages:
#print (Language)
#Here you will get a error message because the print line is not correctly intended. you need to have the print
#line right bellow the variable as you have seen in my previous codes.

#the last print you see in line 29 needs to be intended but python sees that at least one print is intended thats why
#it does not give an error. But since the last value associated with Leopards, it only prints that and not those others
#This is what you call logical error
Animals = ['Tigers', 'Lions', 'Leopards']
for Animal in Animals:
    print(f"{Animal}, belongs to the cat family")
print(f"\n{Animal}, is the smallest among those 3\n")

#you need to only indent when you have to do it otherwise it will print an error. If you indent in a normal list
#It will print indetation error, because you can only do it in for loops and other places.
#So the key is to only do it when you have a specific reason and never forget the colon at the end after the for loop sytnax
#for example For Car in Cars:

#TRY IT YOURSELF 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
#and then use a for loop to print the name of each pizza.
Pizzas = ['Chicken piza', 'Beef pizza', 'Veggie pizza']
for Pizza in Pizzas:
    print(f"I really love {Pizza.title()}!")
print(f"\nMy personal favorite must be {Pizzas[0]}. The {Pizzas[1]} is also delicious but it just cant beat {Pizzas[0]}."
      f"\tI am not so big fan of {Pizzas[2]}, because it can get boring sometimes because it doesnt contain any meat ")
print("\nI really love pizza!\n")

#4-2. Animals: Think of at least three diffrent animals that have a common charachteristic. Store the names of these
#animals in a list, and then use a for loop to print out the name of each animal
Animals = ['Hamster', 'Cat', 'Dog']
for Animal in Animals:
    print (f"{Animal}, is a cute and a lovely pet to have!")
print("\nAll these Animals i mentioned are lovely and would make a great pet!\n")

#There are many reasons to store a set of numbers. For ex. when you need to track the positon of each player in a game
#or you might want to keep track of a players high scores as well.
#USING THE RANGE FUNCTION: Pythons range function makes it easy to generate a series of numbers. This is how you do it:
print("Range function:")
for value in range (1,5):
    print(value)
#It does not print to 5 because the first number starts at 0 like we learned in the previous chapters. in order to print
#to 5 you have to set the range to (1,6):

#Use range to make a list of numbers:
Numbers = list(range(1,6))
print(Numbers)
#How to use range to skip a number and add to a certain number to a value
even_numbers = list(range(2,13,2))
print(even_numbers)
#The firs number in the paranthes is which number you want to start at, the second number is which number your value
#will go up to. so in this case the value will go up to 12 and stop there because it can not surpass 13 because thats
#the number i wrote down that i do not want to surpass. The third number is how much you want to add, in this case: 2
#So the answer will be [2, 4, 6, 8, 10, 12]

#This is how we work with square numbers. First you define which number you want to start with and end with.
#After that you define how many exponents you want by using two asterisks(**). In our case we used 2 because we are just
#gonna multiply 2 number with eachother, if we wrote 3 it woul have been 2 * 2 * 2 but by using 2 it will be:
# 1*1 = 1   2*2 = 4 and so on. This is how we do it:
squares = []
for value in range (1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#Simple statistics with a list of numbers
Digits = [1,2,3,4,5,6,7,8,9,10]
min(Digits)
print("")
print(min(Digits))
print(max(Digits))
print(sum(Digits))

#Bruker du en tredje tall i parantesen bruker python den til hvor mange ganger
#du ønsker å plusse det første tallet ditt med.
even_numbers = list(range(2,13,2))
print(even_numbers)
#Skal man bruke kvadrattall, gjør man det på denne måten
Kvadrattall = []
for verdi in range (1,11):
    Ktall = verdi ** 2
    Kvadrattall.append(Ktall)
print(Kvadrattall)
#En annen måte du kan gjøre dette på men kun en linje kode er på denne måten:
Kvadrattall = [verdi**2 for verdi in range(1,11)]
print(Kvadrattall)

#TRY IT YOURSELF 4-3. COUNTING TO TWENTY: use a for loop to print the numbers
#from 1 to 20, inclusive.
numbers = list(range(1,21))
for number in numbers:

     print(number)

#One million: make a list of the numbers from one to one million, and then use
#a for loop to print the numbers.
#One_Million = list(range(1, 1_000_001))
#for million in One_Million:
    #print(million)

#4-5. Summing a million: Make a list of the numbers from one to one million
#and then use min() and max() to make sure your list actually starts at one
#and ends at one million, also use the sum() function.
One_hundred = list(range(1,101))
for hundred in One_hundred:
    print(hundred)
    print("")
print(min(One_hundred))
print(max(One_hundred))
print(sum(One_hundred))

#4-6. Odd Numbers: Use the third argument of the range() function to make a list
#of the odd numbers from 1 to 20. Use a for loop to print each number:
Oddetall = list(range(1,21,2))
for Odd in Oddetall:
    print(Odd)
#4-7. Threes: make a list of the multiplies of 3 from 3 to 30. Use a for loop
#to print the numbers in your list.
Threes = list(range(3,31,3))
for Three in  Threes:
    print(Three)
#4-8 Cubes: Make a list of the first 10 cube numbers from 1 to 10
Kube = []
for verdi in range(1,11):
    Kubetall = verdi ** 3
    Kube.append(Kubetall)
    print(Kubetall)

#4-9. Cube Comrehension: Use a list comprehension to generate a list of the
#first 10 cubes:
print(f"\nNå skal jeg benytte list comprehension:")
Kuber2 = [verdi**3 for verdi in range(1,11)]
for cube in Kuber2:
    print(cube)

#Working with a part of a list (slice) - slicing a list
print(f"\nIt will only print Tyson, Ali and Floyd, because 0:3 means the three first elements in a list ")
Boxers = ['Tyson', 'Ali', 'Floyd', 'Joshua', 'Usyk',]
print(Boxers[0:3])
print(Boxers[1:4])

print(f"\nIf you write [:4], Python will automatically start your slice at the beginning of the list")
print(Boxers[:4])
#But if you write [2:], Python will start from the third element and continue till the last item
#For example:
print("")
print(Boxers[2:])
#If you want to print the names of the last three players, you can do it this way:
print(Boxers[-3:])

#Looping through a Slice: Instead of looping throgh the entire list, Python loops onlye through the three first
Players = ['Charles', 'Martina', 'Michael', 'Florence', 'Eli']
print("\nHere are the first three players on my team:")
for Player in Players[:3]:
    print(Player)
#Slices are very useful in a number of situations. For instance, when you are creating a game, you could add a players final score to a list
#every time that player finishes playing. You could then get a players top three scores by sorting the list in decreasing order and taking
# a slice that includes just the first three scores.

#Copying a List
My_Favorite_food = ['Pizza', 'Biryani', 'Hamburger']
Friends_favorite = My_Favorite_food[:]
print("\nMy favorite foods are:")
print(My_Favorite_food)

print("\nMy friends favorite foods are:")
print(Friends_favorite)
#Now we are gonna make a change ans see if each list keeps track
My_Favorite_food.append('Falafel')
Friends_favorite.append('Kebab')
print()
#But if you want the two lists to become one so that one change in the first list, also appears in the second, you have to do following:
Friends_favorite = My_Favorite_food
print(Friends_favorite)

#TRY IT YOURSELF. 4-10. Slices:










