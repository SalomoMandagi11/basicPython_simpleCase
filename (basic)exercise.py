"""
    1st exercise:
    Convert user weight either it's on kilograms or lbs, if it is kilograms the convert it to lbs, and vice versa.
"""

# print("Weight converter.")
# user_weight = int(input("Your weight: "))
# print("Convert to:")
# print("1. Lbs")
# print("2. Kg")
# user_choose = int(input("-> "))
#
# if user_choose == 1:
#     converter_lbs = 2.2 * user_weight   # formula for convert kilogram to lbs
#     print(f"Your weight on lbs: {converter_lbs} pounds")
# else:
#     converter_kg = 0.4 * user_weight    # formula for convert lbs to kilogram
#     print(f"Your weight on kg: {converter_kg} kilograms")

"""
    2nd exercise
    Buat sebuah program untuk menjalankan sebuah mobil. Di dalamnya terdapat perintah:
    - start, untuk menjalankan mobil
    - stop, untuk menghentikan mobil
    - quit, untuk menghentikan program
    
    Jika, user memasukan perintah selain 3 perintah diatas, maka berikan info bahwa mesin tidak mengerti.
    
    Untuk memasukan perintah, user harus memasukan dulu kata 'menu'
    
    Yang akan digunakan:
    - input()
    - while
"""

menu = '''_> start\n_> stop\n_>quit'''
command = " "
print("Please type 'menu' to see the right commands.")
while True:     # this will repeatedly until it reach 'break' statement
    command = input("> ")
    if command.lower() == 'start':
        print("Start the car, let's go ridin'!")
    elif command.lower() == 'stop':
        print("Stop the car, let's have some rest~")
    elif command.lower() == 'menu':
        print(menu)
    elif command.lower() == 'quit':
        print("Thank you for use or not using this car.")
        break
    else:
        print("I don't understand your command.")
        print("Please type 'menu' to see the right commands.")
