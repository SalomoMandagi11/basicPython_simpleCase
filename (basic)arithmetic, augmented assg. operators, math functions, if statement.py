"""
    Arithmetic assignment operations:
    1. Addition (third) -> precedence   +
    2. Subtraction  (third) -> precedence   -
    3. Multiplication   (second) -> precedence  *
    4. Division (second) -> precedence  /
    5. Floor division   (second) -> precedence  //
    6. Exponential  (first) -> precedence   **


    ^^^But you can change the precedence using parentheses ().

    Augmented assignment operations:
    - Increment: x = x + 2 --> equal to x += 2
    - Decrement: x = x - 2 --> equal to x -= 2

    Some built in math method that often use:
    - round()
    This method is use to rounded a float value.
    - abs()
    This method is use to change a negative value to positive.
    - max()
    This method is use to give a value of the highest number between numbers
    - min()
    This method is use to give a value of the lowest number between numbers
    - pow()
    This method is use to make a exponential

    Math module:
    Using with -> import math
    List of method on math module:
    1.
"""

# x = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# -> x = x[0], x[1], x[2], and so on.

# max(x)  # ini untuk mencari nilai tertinggi dari kumpulan angka
# pow(2, 5)  # ini perpangkatan, jadi 2 pangkat 5
# round(3.788)    # ini untuk membulatkan, bisa juga ditentukan angka yang ingin dibulatkan, seperti round(3.788, 2)
# abs(-89)

# Q: Kenapa bisa menggunakan {}, saya tahu itu digunakan hanya untuk string.
# A(sementara): Ternyata bisa, contohnya pada beberapa kasus dalam code ini.

# print(f"Hasil perpangkatan dari {x[0]}^{x[1]} = {pow(x[0], x[1])}")
# print(f"Nilai tertinggi yang ada dalam list {x}, ialah {max(x)}")
# print(f"Nilai terendah yang ada dalam list{x}, ialah {min(x)}")

# case 1:
"""
    Mini calculator--
    Membuat sebuah program yang didalamnya terdapat beberapa metode yang bisa dilakukan dengan angka, misal pertambahan,
    dan pengurangan.
"""

x = []
y = []


def int_list():
    global x
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # x is a list of integer numbers
    print(f"List of integer numbers: {x}")


def float_list():
    global y
    y = [0.5, 0.66667, 0.75, 0.8, 0.83333, 0.857, 0.875, 0.88888]  # y is a list of float numbers
    print(f"List of float numbers: {y}")


print("Let's start!")
int_list()
float_list()

print("What do you want to do? ")
print("1. Addition")
print("2. Subtraction")
print("3. Rounded")
choose = int(input("-> "))


x_new = []  # this void list is use later in loop, to store the new value
y_new = []

if choose == 1:
    n_add = int(input("With what number you want to add for all of the numbers of integer and float? "))
    for i in range(len(x)):
        x_new.append(x[i] + n_add)
    for j in range(len(y)):
        y_new.append(y[j] + n_add)
    print(x_new)
    print(y_new)

elif choose == 2:
    n_subtract = int(input("With what number you want to subtract for all of the numbers of integers and float? "))
    for i in range(len(x)):
        x_new.append(x[i] - n_subtract)
    for j in range(len(y)):
        y_new.append(y[j] - n_subtract)
    print(x_new)
    print(y_new)

elif choose == 3:
    rounded_point = int(input("Rounded to what number ahead the point? "))  # berapa angka di depan koma atau titik
    for i in range(len(y)):
        y_new.append(round(y[i], rounded_point))
    print(y_new)
