# Logical operators
"""
    Logical operators is about AND, OR, and NOT.
    It is pretty much same with how we use them in a real life.
"""
is_newYear = False
is_firstDay = False

# if is_newYear and is_firstDay:
#     print("Today is the first day of the year!")
# else:
#     print("Today is not the first day of the year.")


# if is_newYear and not is_firstDay:
#     print("Today is the first day of the year!")
# else:
#     print("Today is 'not' the first day of the year.")
#
#
# if is_newYear or is_firstDay:
#     print("This is new year but not the first day of the year.")
# else:
#     print("This is new year and is the first day of the year")


# Comparison operators
"""
   Comparison operators is about <, >, <=, >=, ==, !=. 
"""

the_weather = 18
# is cold if the weather is under 20 celsius degrees    (<20)
# is hot if the weather is above 30 celsius degrees (>30)
# is mild if the weather is about 21 to 29 celsius degrees (>20 and <30)
if the_weather < 20:
    print("Today is a cold day")
elif the_weather > 30:
    print("Today is a hot day")
else:
    print("Today is either hot nor cold ")
