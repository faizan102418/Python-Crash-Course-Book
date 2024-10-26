# #  Working with lists 

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
    
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

# pizzas = ["peporoni" , "margareta" , " Hawaiion"]
# for pizza in pizzas:
#     print(f"i like {pizza.title()}  pizza")
# print("\n")
# print("I really love pizza ")

# animals = ["Dog" , "Cat" ,"Horse"]
# for animal in animals:
#     print(f"A {animal} would make a great pet ")
# print("Any of these  animals would make a great pet!")\
    
# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
# #    squares.append(value ** 2)
#    squares.append(f"{value} : : {value**2}")
# print(squares)

# squares = [value**2 for value in range(1, 11)]
# print(squares)
# for num in range(1,20):
#     print(num)

# numbers = [1,2,3,4,4,5,3,6,3,67,68,5,8,9,0,6,7,1,112,3,4,555,6,66,788,899,9,97,676,909,789,0,9999,999999]
# for num in numbers:
#     print(num)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for num in range(1,20,2):
#     print(num)
# multipl = []
# for num in range(3,31):
#     if num % 3 ==0:
#         multipl.append(num)
# print(multipl)    
# cubes = []
# for num in range(1,10): 
#     cubes.append(num**3)
# print(cubes)
    
# cube = [num**3 for num in range(1,10)]
# print(cube)

# ********** SLICING  **************
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[1:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
