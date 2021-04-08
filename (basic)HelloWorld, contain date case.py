print("Hello world")

# Case 1:
"""
date = '---January 1 2021---'   # A string variables that contain a date
print("Today is "+date)     # Display the data on date variable
print("What is special about " + date+"?")   # There is concatenate string, you can do this if only the variable contain string
special = input("-> ")  # This is an input function, which technically works same with 'scanf' on c/cpp
print(special)

print("\n")
date = '---January 2 2021---'   # Date has been reset and change to a new string
print("Today is " + date) # Display the data on date variable
print("What is special about " + date+"?")   # There is concatenate string, you can do this if only the variable contain string
special = input("-> ")  # This is an input function, which technically works same with 'scanf' on c/cpp
print(special)
"""
# Case 2:
# Count the day!

month = input("This month is: ")
day_date = int(input("Today date is: "))
year = int(input("This year is: "))
today_date = month + ' ' + str(day_date) + ' ' + str(year)
print(today_date)
count_day = int(input("How many you want to count the day?: "))

what_is_special_journal = []
date_journal = []

for i in range(count_day):
    today_date = month + ' ' + str(day_date) + ' ' + str(year)
    date_journal.append(today_date)
    print("Today is", today_date)
    what_is_special = input("What's special about this day?: ")
    what_is_special_journal.append(what_is_special)
    print("--------Separate the day--------")
    day_date += 1


# Added feature, journal:
print("\n\n")
print('-------->"Your Journal"<--------')
for i in range(count_day):
    print(date_journal[i])
    print("-", what_is_special_journal[i])
    print("--------Separate the day--------")
