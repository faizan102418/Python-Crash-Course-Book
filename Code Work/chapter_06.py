# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['color'] = 'red'
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# print(alien_0)
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")




# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
#  # Move the alien to the right.
#  # Determine how far to move the alien based on its current speed.
# alien_0['speed'] = 'fast'
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3
#  # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# person = {
#     'first_name': 'Faizan',
#     'last_name': 'Khan',
#     'age': 22,
#     'city': 'Lahore'
# }

# print(f"My name is {person['first_name']}")
# print(person['last_name'])
# print(person['age'])
# print(person['city'])


# # favorite_numbers = {
# #     'faizan': 5,
# #     'sarah': 7,
# #     'edward': 9,
# #     'phil': 12,
# #     'zain': 11
# #     }

# # faizan_number = favorite_numbers['faizan']
# # sarah_number = favorite_numbers['sarah']
# # edward_number = favorite_numbers['edward']
# # phil_number = favorite_numbers['phil']
# # zain_number = favorite_numbers['zain']

# # print(f"Faizan's favorite number is {faizan_number}")
# # print(f"Sarah's favorite number is {sarah_number}")
# # print(f"Edward's favorite number is {edward_number}")
# print(f"Phil's favorite number is {phil_number}")
# print(f"Zain's favorite number is {zain_number}")

words = {
    'key': 'value',
    'python' : 'programming language',
    'peter' : 'python programmer',
    'favorite' : 'python',
    'programming' : 'python',
}

for key, value in words.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")